"""Exercise actual HTTP fallback behavior without calling paid services."""
import unittest
from unittest.mock import patch

import httpx

from xocto.brief import BriefError, _PROVIDER_COOLDOWN, _request


class TransportTests(unittest.TestCase):
    def setUp(self):
        # 冷却是模块级状态，跨测试残留会让供应商被误跳过。
        _PROVIDER_COOLDOWN.clear()

    def call_with(self, handler):
        client = httpx.Client(transport=httpx.MockTransport(handler))
        return patch('xocto.brief.httpx.Client', return_value=client)

    def test_long_rate_limit_switches_provider_and_starts_cooling(self):
        attempts = []
        def handler(request):
            attempts.append(request.url.host)
            if request.url.host == 'first.example':
                return httpx.Response(429, headers={'retry-after': '45'})
            return httpx.Response(200, json={'choices': [{'message': {'content': '{"ok":true}'}}]})
        factory = httpx.Client
        providers = [('glm','https://first.example','secret','m'),('groq','https://second.example','secret','m')]
        with patch('xocto.brief._model_providers', return_value=providers), patch('xocto.brief.httpx.Client', side_effect=lambda **kw: factory(transport=httpx.MockTransport(handler))), patch('xocto.brief.time.sleep') as sleep:
            self.assertEqual(_request([]), {'ok': True})
            self.assertEqual(attempts, ['first.example', 'second.example'])
            sleep.assert_not_called()
            # 冷却生效：下一次请求不再撞第一个供应商。
            self.assertEqual(_request([]), {'ok': True})
            self.assertEqual(attempts, ['first.example', 'second.example', 'second.example'])

    def test_transient_failure_retries_before_fallback(self):
        attempts = []
        def handler(request):
            attempts.append(request)
            if len(attempts) == 1:
                return httpx.Response(503, headers={'retry-after': '0'})
            return httpx.Response(200, json={'choices': [{'message': {'content': '{"ok":true}'}}]})
        # A fresh client per attempt, matching production context-manager lifetime.
        factory = httpx.Client
        with patch('xocto.brief._model_providers', return_value=[('gemini','https://example.com','secret','model')]), patch('xocto.brief.httpx.Client', side_effect=lambda **kw: factory(transport=httpx.MockTransport(handler))), patch('xocto.brief.time.sleep') as sleep:
            self.assertEqual(_request([]), {'ok': True})
            self.assertEqual(len(attempts), 2)
            sleep.assert_called_once_with(0)

    def test_permanent_error_falls_back_without_exposing_body(self):
        attempts = []
        def handler(request):
            attempts.append(request.url.host)
            if request.url.host == 'first.example':
                return httpx.Response(402, text='secret private billing details')
            return httpx.Response(200, json={'choices': [{'message': {'content': '{"ok":true}'}}]})
        factory = httpx.Client
        with patch('xocto.brief._model_providers', return_value=[('deepseek','https://first.example','secret','m'),('groq','https://second.example','secret','m')]), patch('xocto.brief.httpx.Client', side_effect=lambda **kw: factory(transport=httpx.MockTransport(handler))):
            self.assertEqual(_request([]), {'ok': True})
        self.assertEqual(attempts, ['first.example','second.example'])

    def test_payload_error_only_reports_numeric_quota(self):
        def handler(request):
            return httpx.Response(413, text='secret org-id Limit 8000, Requested 12345')
        with patch('xocto.brief._model_providers', return_value=[('groq','https://example.com','secret','m')]), self.call_with(handler):
            with self.assertRaises(BriefError) as error:
                _request([])
        self.assertIn('8000/12345', str(error.exception))
        self.assertNotIn('secret', str(error.exception))
        self.assertNotIn('org-id', str(error.exception))
