# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import (
    web_screenshot_params,
    web_web_crawl_md_params,
    web_web_scrape_md_params,
    web_web_scrape_html_params,
    web_web_scrape_images_params,
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
from ..types.web_web_scrape_md_response import WebWebScrapeMdResponse
from ..types.web_web_scrape_html_response import WebWebScrapeHTMLResponse
from ..types.web_web_scrape_images_response import WebWebScrapeImagesResponse
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

    def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Either 'domain'
        or 'directUrl' must be provided as a query parameter, but not both. Returns a
        URL to the uploaded screenshot image hosted on our CDN.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/screenshot",
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
                        "page": page,
                        "prioritize": prioritize,
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
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages. Only follows links within the same
        domain as the starting URL. Costs 1 credit per successful page crawled.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

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
                    "include_images": include_images,
                    "include_links": include_links,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "shorten_base64_images": shorten_base64_images,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
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
        max_age_ms: int | Omit = omit,
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

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

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
                        "max_age_ms": max_age_ms,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

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
                query=maybe_transform({"url": url}, web_web_scrape_images_params.WebWebScrapeImagesParams),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to Markdown, and returns the
        result.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

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
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "shorten_base64_images": shorten_base64_images,
                        "use_main_content_only": use_main_content_only,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

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

    async def screenshot(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        prioritize: Literal["speed", "quality"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """Capture a screenshot of a website.

        Supports both viewport (standard browser
        view) and full-page screenshots. Can also screenshot specific page types (login,
        pricing, etc.) by using heuristics to find the appropriate URL. Either 'domain'
        or 'directUrl' must be provided as a query parameter, but not both. Returns a
        URL to the uploaded screenshot image hosted on our CDN.

        Args:
          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          prioritize: Optional parameter to prioritize screenshot capture. If 'speed', optimizes for
              faster capture with basic quality. If 'quality', optimizes for higher quality
              with longer wait times. Defaults to 'quality' if not provided.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/screenshot",
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
                        "page": page,
                        "prioritize": prioritize,
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
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages. Only follows links within the same
        domain as the starting URL. Costs 1 credit per successful page crawled.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

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
                    "include_images": include_images,
                    "include_links": include_links,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "shorten_base64_images": shorten_base64_images,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
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
        max_age_ms: int | Omit = omit,
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

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

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
                        "max_age_ms": max_age_ms,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeImagesResponse:
        """Scrapes all images from the given URL.

        Extracts images from img, svg,
        picture/source, link, and video elements including inline SVGs, base64 data
        URIs, and standard URLs.

        Args:
          url: Full URL to scrape images from (must include http:// or https:// protocol)

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
                query=await async_maybe_transform({"url": url}, web_web_scrape_images_params.WebWebScrapeImagesParams),
            ),
            cast_to=WebWebScrapeImagesResponse,
        )

    async def web_scrape_md(
        self,
        *,
        url: str,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        max_age_ms: int | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """
        Scrapes the given URL, converts the HTML content to Markdown, and returns the
        result.

        Args:
          url: Full URL to scrape and convert to markdown (must include http:// or https://
              protocol)

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Set to 0 to always scrape fresh.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

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
                        "include_images": include_images,
                        "include_links": include_links,
                        "max_age_ms": max_age_ms,
                        "shorten_base64_images": shorten_base64_images,
                        "use_main_content_only": use_main_content_only,
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """
        Crawls the sitemap of the given domain and returns all discovered page URLs.
        Supports sitemap index files (recursive), parallel fetching with concurrency
        control, deduplication, and filters out non-page resources (images, PDFs, etc.).

        Args:
          domain: Domain name to crawl sitemaps for (e.g., 'example.com'). The domain will be
              automatically normalized and validated.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

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
                    },
                    web_web_scrape_sitemap_params.WebWebScrapeSitemapParams,
                ),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

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
