import importlib.util
from pathlib import Path
import tempfile
import unittest
from unittest.mock import MagicMock, patch

spec = importlib.util.spec_from_file_location('check_deployment', Path(__file__).parents[1] / 'scripts/check_deployment.py')
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)


class DeploymentTests(unittest.TestCase):
    def test_stale_english_edition_fails_even_when_chinese_is_current(self):
        with tempfile.TemporaryDirectory() as tmp:
            root = Path(tmp)
            for path in ('index.html', 'en/index.html', 'r/2026-09-05.html', 'en/r/2026-09-05.html'):
                output = root / path
                output.parent.mkdir(parents=True, exist_ok=True)
                output.write_bytes(b'current')
            def response(request, **kwargs):
                context = MagicMock()
                context.__enter__.return_value.read.return_value = b'stale' if '/en/r/' in request.full_url else b'current'
                return context
            with patch.object(module, 'urlopen', side_effect=response):
                self.assertFalse(module.matches('https://example.com', root, '2026-09-05'))
            context = MagicMock()
            context.__enter__.return_value.read.return_value = b'current'
            with patch.object(module, 'urlopen', return_value=context):
                self.assertTrue(module.matches('https://example.com', root, '2026-09-05'))
