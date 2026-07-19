# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    WebSearchResponse,
    WebExtractResponse,
    WebScreenshotResponse,
    WebWebCrawlMdResponse,
    WebWebScrapeMdResponse,
    WebExtractFontsResponse,
    WebWebScrapeHTMLResponse,
    WebWebScrapeImagesResponse,
    WebWebScrapeSitemapResponse,
    WebExtractStyleguideResponse,
    WebExtractCompetitorsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract(self, client: ContextDev) -> None:
        web = client.web.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        )
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_with_all_params(self, client: ContextDev) -> None:
        web = client.web.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
            fact_check=True,
            follow_subdomains=True,
            include_frames=True,
            instructions="instructions",
            max_age_ms=0,
            max_depth=0,
            max_pages=1,
            pdf={
                "end": 1,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            stop_after_ms=10000,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
            wait_for_ms=0,
        )
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebExtractResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_competitors(self, client: ContextDev) -> None:
        web = client.web.extract_competitors(
            domain="xxx",
        )
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_competitors_with_all_params(self, client: ContextDev) -> None:
        web = client.web.extract_competitors(
            domain="xxx",
            num_competitors=1,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_competitors(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.extract_competitors(
            domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_competitors(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.extract_competitors(
            domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_fonts(self, client: ContextDev) -> None:
        web = client.web.extract_fonts()
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_fonts_with_all_params(self, client: ContextDev) -> None:
        web = client.web.extract_fonts(
            direct_url="https://example.com",
            domain="xxx",
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_fonts(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.extract_fonts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_fonts(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.extract_fonts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebExtractFontsResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_styleguide(self, client: ContextDev) -> None:
        web = client.web.extract_styleguide()
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_extract_styleguide_with_all_params(self, client: ContextDev) -> None:
        web = client.web.extract_styleguide(
            color_scheme="light",
            direct_url="https://example.com",
            domain="xxx",
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_extract_styleguide(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.extract_styleguide()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_extract_styleguide(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.extract_styleguide() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot(self, client: ContextDev) -> None:
        web = client.web.screenshot()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_screenshot_with_all_params(self, client: ContextDev) -> None:
        web = client.web.screenshot(
            color_scheme="light",
            country="de",
            direct_url="https://example.com",
            domain="xxx",
            full_screenshot="true",
            handle_cookie_popup="true",
            max_age_ms=0,
            page="login",
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_ms=1,
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_screenshot(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.screenshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_screenshot(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.screenshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebScreenshotResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search(self, client: ContextDev) -> None:
        web = client.web.search(
            query="x",
        )
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: ContextDev) -> None:
        web = client.web.search(
            query="x",
            country="af",
            exclude_domains=["string"],
            freshness="last_24_hours",
            include_domains=["string"],
            markdown_options={
                "enabled": True,
                "include_frames": True,
                "include_images": True,
                "include_links": True,
                "max_age_ms": 0,
                "pdf": {
                    "end": 1,
                    "should_parse": True,
                    "start": 1,
                },
                "shorten_base64_images": True,
                "timeout_ms": 1000,
                "use_main_content_only": True,
                "wait_for_ms": 0,
            },
            num_results=10,
            query_fanout=True,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebSearchResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_crawl_md(self, client: ContextDev) -> None:
        web = client.web.web_crawl_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_crawl_md_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_crawl_md(
            url="https://example.com",
            country="de",
            exclude_selectors=["string"],
            follow_subdomains=True,
            include_frames=True,
            include_images=True,
            include_links=True,
            include_selectors=["string"],
            max_age_ms=0,
            max_depth=0,
            max_pages=1,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            shorten_base64_images=True,
            stop_after_ms=10000,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
            url_regex="^https?://[^/]+/blog/",
            use_main_content_only=True,
            wait_for_ms=0,
        )
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_crawl_md(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_crawl_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_crawl_md(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_crawl_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_html(self, client: ContextDev) -> None:
        web = client.web.web_scrape_html(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_html_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_html(
            url="https://example.com",
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames="true",
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": "true",
                "should_parse": "true",
                "start": 1,
            },
            settle_animations="true",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            use_main_content_only="true",
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_html(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_html(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_html(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_html(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_images(self, client: ContextDev) -> None:
        web = client.web.web_scrape_images(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_images_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_images(
            url="https://example.com",
            dedupe="true",
            enrichment={
                "classification": "true",
                "hosted_url": "true",
                "max_time_per_ms": 1,
                "resolution": "true",
            },
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1,
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_images(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_images(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_images(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_images(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_md(self, client: ContextDev) -> None:
        web = client.web.web_scrape_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_md_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_md(
            url="https://example.com",
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames="true",
            include_images="true",
            include_links="true",
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": "true",
                "should_parse": "true",
                "start": 1,
            },
            settle_animations="true",
            shorten_base64_images="true",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            use_main_content_only="true",
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_md(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_md(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_sitemap(self, client: ContextDev) -> None:
        web = client.web.web_scrape_sitemap(
            domain="xxx",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_sitemap_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_sitemap(
            domain="xxx",
            headers={"foo": "J!"},
            max_links=1,
            sitemap_url="https://example.com",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            url_regex="^https?://[^/]+/blog/",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_sitemap(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_sitemap(
            domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_sitemap(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_sitemap(
            domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        )
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
            fact_check=True,
            follow_subdomains=True,
            include_frames=True,
            instructions="instructions",
            max_age_ms=0,
            max_depth=0,
            max_pages=1,
            pdf={
                "end": 1,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            stop_after_ms=10000,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
            wait_for_ms=0,
        )
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebExtractResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.extract(
            schema={
                "type": "bar",
                "properties": "bar",
                "required": "bar",
                "additionalProperties": "bar",
            },
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebExtractResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_competitors(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_competitors(
            domain="xxx",
        )
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_competitors_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_competitors(
            domain="xxx",
            num_competitors=1,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_competitors(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.extract_competitors(
            domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_competitors(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.extract_competitors(
            domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebExtractCompetitorsResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_fonts(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_fonts()
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_fonts_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_fonts(
            direct_url="https://example.com",
            domain="xxx",
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_fonts(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.extract_fonts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebExtractFontsResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_fonts(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.extract_fonts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebExtractFontsResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_styleguide()
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_extract_styleguide_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.extract_styleguide(
            color_scheme="light",
            direct_url="https://example.com",
            domain="xxx",
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.extract_styleguide()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_extract_styleguide(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.extract_styleguide() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebExtractStyleguideResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.screenshot()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_screenshot_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.screenshot(
            color_scheme="light",
            country="de",
            direct_url="https://example.com",
            domain="xxx",
            full_screenshot="true",
            handle_cookie_popup="true",
            max_age_ms=0,
            page="login",
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_ms=1,
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
        )
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_screenshot(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.screenshot()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_screenshot(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.screenshot() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebScreenshotResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.search(
            query="x",
        )
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.search(
            query="x",
            country="af",
            exclude_domains=["string"],
            freshness="last_24_hours",
            include_domains=["string"],
            markdown_options={
                "enabled": True,
                "include_frames": True,
                "include_images": True,
                "include_links": True,
                "max_age_ms": 0,
                "pdf": {
                    "end": 1,
                    "should_parse": True,
                    "start": 1,
                },
                "shorten_base64_images": True,
                "timeout_ms": 1000,
                "use_main_content_only": True,
                "wait_for_ms": 0,
            },
            num_results=10,
            query_fanout=True,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.search(
            query="x",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebSearchResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.search(
            query="x",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebSearchResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_crawl_md(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_crawl_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_crawl_md_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_crawl_md(
            url="https://example.com",
            country="de",
            exclude_selectors=["string"],
            follow_subdomains=True,
            include_frames=True,
            include_images=True,
            include_links=True,
            include_selectors=["string"],
            max_age_ms=0,
            max_depth=0,
            max_pages=1,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            shorten_base64_images=True,
            stop_after_ms=10000,
            tags=["production", "team-alpha"],
            timeout_ms=1000,
            url_regex="^https?://[^/]+/blog/",
            use_main_content_only=True,
            wait_for_ms=0,
        )
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_crawl_md(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_crawl_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_crawl_md(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_crawl_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebCrawlMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_html(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_html_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_html(
            url="https://example.com",
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames="true",
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": "true",
                "should_parse": "true",
                "start": 1,
            },
            settle_animations="true",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            use_main_content_only="true",
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_html(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_html(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_html(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeHTMLResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_images(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_images_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_images(
            url="https://example.com",
            dedupe="true",
            enrichment={
                "classification": "true",
                "hosted_url": "true",
                "max_time_per_ms": 1,
                "resolution": "true",
            },
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_ms=1,
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_images(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_images(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_images(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeImagesResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_md(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_md_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_md(
            url="https://example.com",
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames="true",
            include_images="true",
            include_links="true",
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": "true",
                "should_parse": "true",
                "start": 1,
            },
            settle_animations="true",
            shorten_base64_images="true",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            use_main_content_only="true",
            wait_for_ms=0,
        )
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_md(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_md(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_md(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeMdResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_sitemap(
            domain="xxx",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_sitemap_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_sitemap(
            domain="xxx",
            headers={"foo": "J!"},
            max_links=1,
            sitemap_url="https://example.com",
            tags=["production", "team-alpha"],
            timeout_ms=1,
            url_regex="^https?://[^/]+/blog/",
        )
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_sitemap(
            domain="xxx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_sitemap(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_sitemap(
            domain="xxx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeSitemapResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True
