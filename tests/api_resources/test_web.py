# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    WebScrapeResponse,
    WebSearchResponse,
    WebAnswersResponse,
    WebExtractResponse,
    WebScreenshotResponse,
    WebWebCrawlMdResponse,
    WebWebScrapeMdResponse,
    WebExtractFontsResponse,
    WebWebScrapeHTMLResponse,
    WebWebScrapeBytesResponse,
    WebWebScrapeImagesResponse,
    WebWebScrapeSitemapResponse,
    WebExtractStyleguideResponse,
    WebExtractCompetitorsResponse,
    WebWebScrapeScreenshotResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_answers(self, client: ContextDev) -> None:
        web = client.web.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        )
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_answers_with_all_params(self, client: ContextDev) -> None:
        web = client.web.answers(
            task="Find the pricing page URL and plan names for context.dev.",
            json_format={
                "pricing_page_url": "bar",
                "plans": "bar",
            },
            mode="fast",
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
        )
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_answers(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_answers(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebAnswersResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
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
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            zdr="enabled",
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
    def test_method_scrape(self, client: ContextDev) -> None:
        web = client.web.scrape(
            formats={},
            url="https://example.com",
        )
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_scrape_with_all_params(self, client: ContextDev) -> None:
        web = client.web.scrape(
            formats={
                "bytes": True,
                "html": True,
                "images": True,
                "markdown": True,
                "parse": True,
                "screenshot": True,
            },
            url="https://example.com",
            image_params={
                "dedupe": "none",
                "enrich": ["dimensions"],
            },
            markdown_params={
                "include_images": True,
                "include_links": True,
                "inline_images": "placeholder",
            },
            max_age_ms=0,
            parse_params={
                "rules": {
                    "title": "h1",
                    "links": {
                        "selector": "a",
                        "output": "@href",
                        "type": "list",
                    },
                }
            },
            screenshot_params={
                "area": "viewport",
                "format": "png",
            },
            shared_params={
                "actions": [
                    {
                        "action": "Click the product details tab",
                        "type": "perform",
                    }
                ],
                "country": "US",
                "dismiss_cookies": True,
                "dismiss_popups": True,
                "exclude_selectors": ["P"],
                "headers": {"Accept-Language": "en-US"},
                "include_frames": True,
                "include_selectors": ["P"],
                "main_content_only": True,
                "parsers": {
                    "pdf": {
                        "end_page": 1,
                        "ocr": "off",
                        "start_page": 1,
                    }
                },
                "settle_animations": True,
                "theme": "light",
                "viewport": {
                    "height": 240,
                    "width": 240,
                },
                "wait_for": 500,
            },
            tags=["production", "team-alpha"],
            timeout_ms=1,
            zdr="enabled",
        )
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_scrape(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.scrape(
            formats={},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_scrape(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.scrape(
            formats={},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebScrapeResponse, web, path=["response"])

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
            clear_popups=True,
            color_scheme="light",
            country="de",
            direct_url="https://example.com",
            domain="xxx",
            full_screenshot="true",
            handle_cookie_popup=True,
            headers={"foo": "J!"},
            max_age_ms=0,
            page="login",
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
            zdr="enabled",
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
                "timeout_opts": {
                    "milliseconds": 1,
                    "behavior": "fail",
                },
                "use_main_content_only": True,
                "wait_for_ms": 0,
            },
            num_results=10,
            query_fanout=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            url_regex="^https?://[^/]+/blog/",
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
    def test_method_web_scrape_bytes(self, client: ContextDev) -> None:
        web = client.web.web_scrape_bytes(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_bytes_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_bytes(
            url="https://example.com",
            country="de",
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
        )
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_bytes(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_bytes(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_bytes(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_bytes(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            exclude_selectors=["x"],
            extract_rules={"foo": "x"},
            headers={"foo": "J!"},
            include_frames=True,
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            dedupe=True,
            enrichment={
                "classification": True,
                "hosted_url": True,
                "max_time_per_ms": 1,
                "resolution": True,
            },
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames=True,
            include_html=True,
            include_images=True,
            include_links=True,
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            shorten_base64_images=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
    def test_method_web_scrape_screenshot(self, client: ContextDev) -> None:
        web = client.web.web_scrape_screenshot(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_web_scrape_screenshot_with_all_params(self, client: ContextDev) -> None:
        web = client.web.web_scrape_screenshot(
            url="https://example.com",
            clear_popups=True,
            color_scheme="light",
            country="de",
            full_screenshot="true",
            handle_cookie_popup=True,
            headers={"foo": "J!"},
            max_age_ms=0,
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
            zdr="enabled",
        )
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_web_scrape_screenshot(self, client: ContextDev) -> None:
        response = client.web.with_raw_response.web_scrape_screenshot(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = response.parse()
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_web_scrape_screenshot(self, client: ContextDev) -> None:
        with client.web.with_streaming_response.web_scrape_screenshot(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = response.parse()
            assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

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
            include_subdomains=True,
            max_links=1,
            search="help center and troubleshooting articles",
            sitemap_url="https://example.com",
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            url_regex="^https?://[^/]+/blog/",
            zdr="enabled",
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
    async def test_method_answers(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        )
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_answers_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.answers(
            task="Find the pricing page URL and plan names for context.dev.",
            json_format={
                "pricing_page_url": "bar",
                "plans": "bar",
            },
            mode="fast",
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
        )
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_answers(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebAnswersResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_answers(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.answers(
            task="Find the pricing page URL and plan names for context.dev.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebAnswersResponse, web, path=["response"])

        assert cast(Any, response.is_closed) is True

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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
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
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            zdr="enabled",
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
    async def test_method_scrape(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.scrape(
            formats={},
            url="https://example.com",
        )
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_scrape_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.scrape(
            formats={
                "bytes": True,
                "html": True,
                "images": True,
                "markdown": True,
                "parse": True,
                "screenshot": True,
            },
            url="https://example.com",
            image_params={
                "dedupe": "none",
                "enrich": ["dimensions"],
            },
            markdown_params={
                "include_images": True,
                "include_links": True,
                "inline_images": "placeholder",
            },
            max_age_ms=0,
            parse_params={
                "rules": {
                    "title": "h1",
                    "links": {
                        "selector": "a",
                        "output": "@href",
                        "type": "list",
                    },
                }
            },
            screenshot_params={
                "area": "viewport",
                "format": "png",
            },
            shared_params={
                "actions": [
                    {
                        "action": "Click the product details tab",
                        "type": "perform",
                    }
                ],
                "country": "US",
                "dismiss_cookies": True,
                "dismiss_popups": True,
                "exclude_selectors": ["P"],
                "headers": {"Accept-Language": "en-US"},
                "include_frames": True,
                "include_selectors": ["P"],
                "main_content_only": True,
                "parsers": {
                    "pdf": {
                        "end_page": 1,
                        "ocr": "off",
                        "start_page": 1,
                    }
                },
                "settle_animations": True,
                "theme": "light",
                "viewport": {
                    "height": 240,
                    "width": 240,
                },
                "wait_for": 500,
            },
            tags=["production", "team-alpha"],
            timeout_ms=1,
            zdr="enabled",
        )
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_scrape(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.scrape(
            formats={},
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebScrapeResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_scrape(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.scrape(
            formats={},
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebScrapeResponse, web, path=["response"])

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
            clear_popups=True,
            color_scheme="light",
            country="de",
            direct_url="https://example.com",
            domain="xxx",
            full_screenshot="true",
            handle_cookie_popup=True,
            headers={"foo": "J!"},
            max_age_ms=0,
            page="login",
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
            zdr="enabled",
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
                "timeout_opts": {
                    "milliseconds": 1,
                    "behavior": "fail",
                },
                "use_main_content_only": True,
                "wait_for_ms": 0,
            },
            num_results=10,
            query_fanout=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            zdr="enabled",
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
            timeout_opts={
                "milliseconds": 1000,
                "behavior": "fail",
            },
            url_regex="^https?://[^/]+/blog/",
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
    async def test_method_web_scrape_bytes(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_bytes(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_bytes_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_bytes(
            url="https://example.com",
            country="de",
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
        )
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_bytes(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_bytes(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_bytes(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_bytes(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeBytesResponse, web, path=["response"])

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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            exclude_selectors=["x"],
            extract_rules={"foo": "x"},
            headers={"foo": "J!"},
            include_frames=True,
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            dedupe=True,
            enrichment={
                "classification": True,
                "hosted_url": True,
                "max_time_per_ms": 1,
                "resolution": True,
            },
            headers={"foo": "J!"},
            max_age_ms=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            wait_for_ms=0,
            zdr="enabled",
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
            actions=[
                {
                    "do": "wait",
                    "time_ms": 0,
                }
            ],
            country="de",
            exclude_selectors=["x"],
            headers={"foo": "J!"},
            include_frames=True,
            include_html=True,
            include_images=True,
            include_links=True,
            include_selectors=["x"],
            max_age_ms=0,
            pdf={
                "end": 1,
                "ocr": True,
                "should_parse": True,
                "start": 1,
            },
            settle_animations=True,
            shorten_base64_images=True,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            use_main_content_only=True,
            wait_for_ms=0,
            zdr="enabled",
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
    async def test_method_web_scrape_screenshot(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_screenshot(
            url="https://example.com",
        )
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_web_scrape_screenshot_with_all_params(self, async_client: AsyncContextDev) -> None:
        web = await async_client.web.web_scrape_screenshot(
            url="https://example.com",
            clear_popups=True,
            color_scheme="light",
            country="de",
            full_screenshot="true",
            handle_cookie_popup=True,
            headers={"foo": "J!"},
            max_age_ms=0,
            scroll_offset=0,
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            viewport={
                "height": 240,
                "width": 240,
            },
            wait_for_ms=0,
            zdr="enabled",
        )
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_web_scrape_screenshot(self, async_client: AsyncContextDev) -> None:
        response = await async_client.web.with_raw_response.web_scrape_screenshot(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web = await response.parse()
        assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_web_scrape_screenshot(self, async_client: AsyncContextDev) -> None:
        async with async_client.web.with_streaming_response.web_scrape_screenshot(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web = await response.parse()
            assert_matches_type(WebWebScrapeScreenshotResponse, web, path=["response"])

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
            include_subdomains=True,
            max_links=1,
            search="help center and troubleshooting articles",
            sitemap_url="https://example.com",
            tags=["production", "team-alpha"],
            timeout_opts={
                "milliseconds": 1,
                "behavior": "fail",
            },
            url_regex="^https?://[^/]+/blog/",
            zdr="enabled",
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
