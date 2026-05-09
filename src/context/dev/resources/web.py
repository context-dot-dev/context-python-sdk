# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    web_screenshot_params,
    web_web_crawl_md_params,
    web_extract_fonts_params,
    web_web_scrape_md_params,
    web_web_scrape_html_params,
    web_web_scrape_images_params,
    web_extract_styleguide_params,
    web_web_scrape_sitemap_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.web_screenshot_response import WebScreenshotResponse
from ..types.web_web_crawl_md_response import WebWebCrawlMdResponse
from ..types.web_extract_fonts_response import WebExtractFontsResponse
from ..types.web_web_scrape_md_response import WebWebScrapeMdResponse
from ..types.web_web_scrape_html_response import WebWebScrapeHTMLResponse
from ..types.web_web_scrape_images_response import WebWebScrapeImagesResponse
from ..types.web_extract_styleguide_response import WebExtractStyleguideResponse
from ..types.web_web_scrape_sitemap_response import WebWebScrapeSitemapResponse

__all__ = ["WebResource", "AsyncWebResource"]


class WebResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> WebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return WebResourceWithStreamingResponse(self)

    def extract_fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractFontsResponse:
        """
        Scrape font information from a website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          direct_url: A specific URL to fetch fonts from directly, bypassing domain resolution (e.g.,
              'https://example.com/design-system'). When provided, fonts are extracted from
              this exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_fonts_params.WebExtractFontsParams,
                ),
            ),
            cast_to=WebExtractFontsResponse,
        )

    def extract_styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractStyleguideResponse:
        """
        Extract a comprehensive design system from a website including colors,
        typography, spacing, shadows, and UI components.

        Args:
          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_styleguide_params.WebExtractStyleguideParams,
                ),
            ),
            cast_to=WebExtractStyleguideResponse,
        )

    def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        max_age_ms: int | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        viewport: web_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """
        Capture a screenshot of a website.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "timeout_ms": timeout_ms,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    def web_crawl_md(
        self,
        *,
        url: str,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          parse_pdf: When true (default), PDF pages are fetched and their text layer is extracted and
              converted to Markdown alongside HTML pages. When false, PDF pages are skipped
              entirely (not included in results and not counted as failures).

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load for each
              crawled page. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web/crawl",
            body=maybe_transform(
                {
                    "url": url,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "parse_pdf": parse_pdf,
                    "shorten_base64_images": shorten_base64_images,
                    "timeout_ms": timeout_ms,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
                    "wait_for_ms": wait_for_ms,
                },
                web_web_crawl_md_params.WebWebCrawlMdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebWebCrawlMdResponse,
        )

    def web_scrape_html(
        self,
        *,
        url: str,
        include_frames: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """
        Scrapes the given URL and returns the raw HTML content of the page.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          include_frames: When true, iframes are rendered inline into the returned HTML.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          parse_pdf: When true (default), PDF URLs are fetched and their text layer is extracted and
              returned wrapped in <html><pdf>…</pdf></html>. When false, PDF URLs are skipped
              and a 400 WEBSITE_ACCESS_ERROR is returned.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "include_frames": include_frames,
                        "max_age_ms": max_age_ms,
                        "parse_pdf": parse_pdf,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_html_params.WebWebScrapeHTMLParams,
                ),
            ),
            cast_to=WebWebScrapeHTMLResponse,
        )

    def web_scrape_images(
        self,
        *,
        url: str,
        enrichment: web_web_scrape_images_params.Enrichment | Omit = omit,
        max_age_ms: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """
        Extract image assets from a web page, including standard URLs, inline SVGs, data
        URIs, responsive image sources, metadata, CSS backgrounds, video posters, and
        embeds. The base request costs 1 credit; enrichment costs 1 credit per returned
        image.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              collecting images. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "enrichment": enrichment,
                        "max_age_ms": max_age_ms,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_images_params.WebWebScrapeImagesParams,
                ),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    def web_scrape_md(
        self,
        *,
        url: str,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL into LLM usable Markdown.

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          parse_pdf: When true (default), PDF URLs are fetched and their text layer is extracted and
              converted to Markdown. When false, PDF URLs are skipped and a 400
              WEBSITE_ACCESS_ERROR is returned.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "url": url,
                        "include_frames": include_frames,
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "parse_pdf": parse_pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_md_params.WebWebScrapeMdParams,
                ),
            ),
            cast_to=WebWebScrapeMdResponse,
        )

    def web_scrape_sitemap(
        self,
        *,
        domain: str,
        max_links: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawl an entire website's sitemap and return all discovered page URLs.

        Args:
          domain: Domain to build a sitemap for

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "max_links": max_links,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                    },
                    web_web_scrape_sitemap_params.WebWebScrapeSitemapParams,
                ),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class AsyncWebResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncWebResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncWebResourceWithStreamingResponse(self)

    async def extract_fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractFontsResponse:
        """
        Scrape font information from a website including font families, usage
        statistics, fallbacks, and element/word counts.

        Args:
          direct_url: A specific URL to fetch fonts from directly, bypassing domain resolution (e.g.,
              'https://example.com/design-system'). When provided, fonts are extracted from
              this exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to extract fonts from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/fonts",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_fonts_params.WebExtractFontsParams,
                ),
            ),
            cast_to=WebExtractFontsResponse,
        )

    async def extract_styleguide(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractStyleguideResponse:
        """
        Extract a comprehensive design system from a website including colors,
        typography, spacing, shadows, and UI components.

        Args:
          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/styleguide",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_styleguide_params.WebExtractStyleguideParams,
                ),
            ),
            cast_to=WebExtractStyleguideResponse,
        )

    async def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        max_age_ms: int | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        timeout_ms: int | Omit = omit,
        viewport: web_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """
        Capture a screenshot of a website.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/screenshot",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "timeout_ms": timeout_ms,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    async def web_crawl_md(
        self,
        *,
        url: str,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          parse_pdf: When true (default), PDF pages are fetched and their text layer is extracted and
              converted to Markdown alongside HTML pages. When false, PDF pages are skipped
              entirely (not included in results and not counted as failures).

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load for each
              crawled page. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web/crawl",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "parse_pdf": parse_pdf,
                    "shorten_base64_images": shorten_base64_images,
                    "timeout_ms": timeout_ms,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
                    "wait_for_ms": wait_for_ms,
                },
                web_web_crawl_md_params.WebWebCrawlMdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebWebCrawlMdResponse,
        )

    async def web_scrape_html(
        self,
        *,
        url: str,
        include_frames: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """
        Scrapes the given URL and returns the raw HTML content of the page.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          include_frames: When true, iframes are rendered inline into the returned HTML.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          parse_pdf: When true (default), PDF URLs are fetched and their text layer is extracted and
              returned wrapped in <html><pdf>…</pdf></html>. When false, PDF URLs are skipped
              and a 400 WEBSITE_ACCESS_ERROR is returned.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/html",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "include_frames": include_frames,
                        "max_age_ms": max_age_ms,
                        "parse_pdf": parse_pdf,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_html_params.WebWebScrapeHTMLParams,
                ),
            ),
            cast_to=WebWebScrapeHTMLResponse,
        )

    async def web_scrape_images(
        self,
        *,
        url: str,
        enrichment: web_web_scrape_images_params.Enrichment | Omit = omit,
        max_age_ms: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """
        Extract image assets from a web page, including standard URLs, inline SVGs, data
        URIs, responsive image sources, metadata, CSS backgrounds, video posters, and
        embeds. The base request costs 1 credit; enrichment costs 1 credit per returned
        image.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              collecting images. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/images",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "enrichment": enrichment,
                        "max_age_ms": max_age_ms,
                        "timeout_ms": timeout_ms,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_images_params.WebWebScrapeImagesParams,
                ),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    async def web_scrape_md(
        self,
        *,
        url: str,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_pdf: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL into LLM usable Markdown.

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          parse_pdf: When true (default), PDF URLs are fetched and their text layer is extracted and
              converted to Markdown. When false, PDF URLs are skipped and a 400
              WEBSITE_ACCESS_ERROR is returned.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/markdown",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "url": url,
                        "include_frames": include_frames,
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "parse_pdf": parse_pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                    },
                    web_web_scrape_md_params.WebWebScrapeMdParams,
                ),
            ),
            cast_to=WebWebScrapeMdResponse,
        )

    async def web_scrape_sitemap(
        self,
        *,
        domain: str,
        max_links: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawl an entire website's sitemap and return all discovered page URLs.

        Args:
          domain: Domain to build a sitemap for

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/scrape/sitemap",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "max_links": max_links,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                    },
                    web_web_scrape_sitemap_params.WebWebScrapeSitemapParams,
                ),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.extract_fonts = to_raw_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = to_raw_response_wrapper(
            web.extract_styleguide,
        )
        self.screenshot = to_raw_response_wrapper(
            web.screenshot,
        )
        self.web_crawl_md = to_raw_response_wrapper(
            web.web_crawl_md,
        )
        self.web_scrape_html = to_raw_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = to_raw_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = to_raw_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = to_raw_response_wrapper(
            web.web_scrape_sitemap,
        )


class AsyncWebResourceWithRawResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.extract_fonts = async_to_raw_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = async_to_raw_response_wrapper(
            web.extract_styleguide,
        )
        self.screenshot = async_to_raw_response_wrapper(
            web.screenshot,
        )
        self.web_crawl_md = async_to_raw_response_wrapper(
            web.web_crawl_md,
        )
        self.web_scrape_html = async_to_raw_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = async_to_raw_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = async_to_raw_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_raw_response_wrapper(
            web.web_scrape_sitemap,
        )


class WebResourceWithStreamingResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.extract_fonts = to_streamed_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = to_streamed_response_wrapper(
            web.extract_styleguide,
        )
        self.screenshot = to_streamed_response_wrapper(
            web.screenshot,
        )
        self.web_crawl_md = to_streamed_response_wrapper(
            web.web_crawl_md,
        )
        self.web_scrape_html = to_streamed_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = to_streamed_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = to_streamed_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = to_streamed_response_wrapper(
            web.web_scrape_sitemap,
        )


class AsyncWebResourceWithStreamingResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.extract_fonts = async_to_streamed_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = async_to_streamed_response_wrapper(
            web.extract_styleguide,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            web.screenshot,
        )
        self.web_crawl_md = async_to_streamed_response_wrapper(
            web.web_crawl_md,
        )
        self.web_scrape_html = async_to_streamed_response_wrapper(
            web.web_scrape_html,
        )
        self.web_scrape_images = async_to_streamed_response_wrapper(
            web.web_scrape_images,
        )
        self.web_scrape_md = async_to_streamed_response_wrapper(
            web.web_scrape_md,
        )
        self.web_scrape_sitemap = async_to_streamed_response_wrapper(
            web.web_scrape_sitemap,
        )
