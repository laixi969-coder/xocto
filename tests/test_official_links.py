from dataclasses import replace
from pathlib import Path
import unittest

from jinja2 import Environment, FileSystemLoader, select_autoescape

from xocto.i18n import EN, ZH
from xocto.models import Product, Sighting
from xocto.official_links import official_site_url
from xocto.site import _public_page_url, _schema, md_inline, product_view


def product(url: str, sightings: tuple = ()) -> Product:
    return Product(
        slug="example", name="Example", url=url, canonical_url=url,
        summary="Example product", summary_zh="产品说明", summary_en="Example product",
        first_seen="2026-09-01T00:00:00Z", last_seen="2026-09-01T00:00:00Z",
        sightings=sightings, status="watching",
    )


class OfficialLinksTests(unittest.TestCase):
    def test_third_party_pages_are_never_labelled_as_official(self) -> None:
        for url in (
            "https://www.aicpb.com/product/example", "https://www.aicpb.cn/product/example",
            "https://www.similarweb.com/website/example.com/",
            "https://app.sensortower.com/overview/example",
            "https://www.toolify.ai/tool/example", "https://trustmrr.com/startup/example",
            "https://news.crunchbase.com/example", "https://news.google.com/rss/articles/abc",
            "https://www.techcrunch.com/example", "https://github.com/owner/example",
            "https://huggingface.co/spaces/owner/example", "https://www.npmjs.com/package/example",
            "https://apps.apple.com/app/example", "https://www.v2ex.com/t/123",
            "https://WWW.SIMILARWEB.COM./website/example.com/",
            "", "javascript:alert(1)", "https://", "https://[invalid",
        ):
            for locale in (ZH, EN):
                with self.subTest(url=url, locale=locale.key):
                    view = product_view(product(url), locale)
                    self.assertEqual(view["url"], "")
                    schema = _schema(
                        locale=locale, canonical="https://xocto.vercel.app/p/example.html",
                        description=view["summary"], page="products", title="Example", product=view,
                    )
                    software = next(x for x in schema["@graph"] if x["@type"] == "SoftwareApplication")
                    self.assertNotIn("sameAs", software)

    def test_unknown_news_publishers_and_company_customer_stories_are_not_official(self) -> None:
        for source, kind, url in (
            ("marketfeeds", "news", "https://new-publisher.example/story"),
            ("officialfeeds", "news", "https://aws.amazon.com/blogs/customer-story"),
            ("hackernews", "news", "https://unknown.example/story"),
            ("newssearch", "product", "https://unknown.example/legacy-story"),
        ):
            with self.subTest(source=source):
                sighting = Sighting(source, url, "2026-09-01T00:00:00Z", {}, kind=kind)
                item = product(url, (sighting,))
                self.assertEqual(official_site_url(item), "")
                # A third-party story about the product must not hide its own site.
                self.assertEqual(official_site_url(replace(item, url="https://example.com")), "https://example.com")

    def test_product_sites_and_owned_hosting_subdomains_are_preserved(self) -> None:
        for url in (
            "https://example.com", "https://docs.example.com/start",
            "https://example.vercel.app", "https://example.pages.dev",
            "https://example.github.io", "https://similarweb.com.example.org",
        ):
            with self.subTest(url=url):
                self.assertEqual(official_site_url(product(url)), url)

    def test_source_urls_remain_available_as_evidence(self) -> None:
        for url in ("https://news.crunchbase.com/example", "https://github.com/owner/example"):
            self.assertEqual(_public_page_url(url), url)
            self.assertEqual(product(url).url, url)

    def test_missing_site_omits_the_entire_website_row_in_both_languages(self) -> None:
        env = Environment(
            loader=FileSystemLoader(Path(__file__).parents[1] / "templates"),
            autoescape=select_autoescape(["html"]),
        )
        env.filters["md_inline"] = md_inline
        for locale, alternate in ((ZH, EN), (EN, ZH)):
            for url, visible in (("https://www.similarweb.com/website/example.com/", False),
                                 ("https://example.com", True)):
                with self.subTest(locale=locale.key, url=url):
                    rendered = env.get_template("product.html").render(
                        product=product_view(product(url), locale), locale=locale, t=locale.t,
                        alt_locale=alternate, stats={"total": 1, "analysed": 0},
                    )
                    self.assertEqual(f"<dt>{locale.t['product']['link']}</dt>" in rendered, visible)
                    self.assertEqual(f'href="{url}"' in rendered, visible)


if __name__ == "__main__":
    unittest.main()
