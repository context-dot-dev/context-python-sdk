# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    web_scrape_params,
    web_search_params,
    web_answers_params,
    web_map_urls_params,
    web_screenshot_params,
    web_web_crawl_md_params,
    web_extract_styleguide_params,
    web_extract_competitors_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.web_scrape_response import WebScrapeResponse
from ..types.web_search_response import WebSearchResponse
from ..types.web_answers_response import WebAnswersResponse
from ..types.web_map_urls_response import WebMapURLsResponse
from ..types.web_screenshot_response import WebScreenshotResponse
from ..types.web_web_crawl_md_response import WebWebCrawlMdResponse
from ..types.web_extract_styleguide_response import WebExtractStyleguideResponse
from ..types.web_extract_competitors_response import WebExtractCompetitorsResponse

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

    def answers(
        self,
        *,
        task: str,
        controls: web_answers_params.Controls | Omit = omit,
        json_format: Dict[str, object] | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_answers_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebAnswersResponse:
        """
        Research a task across the live web and Context.dev's company and people data,
        and get the answer in the JSON shape you provide, with the URLs it used. `fast`
        (10 credits) suits short lookups; `ultra` (100 credits, the default) reads more
        sources for deeper research.

        Args:
          task: What to research, in plain language, up to 2000 characters. Include domains or
              URLs to focus the research.

          controls: Limit which sites the research can search, read, and cite.

          json_format: Example of the answer object to return, not a JSON Schema. Up to 8 levels deep,
              500 values, and 16,000 characters. Values that cannot be found come back as
              `null`. Defaults to `{ "result": "" }`.

          mode: `fast` prioritizes speed and adds extra verification for people and companies;
              `ultra` searches and reads more sources for deeper research. Defaults to
              `ultra`.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web/answers",
            body=maybe_transform(
                {
                    "task": task,
                    "controls": controls,
                    "json_format": json_format,
                    "mode": mode,
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_answers_params.WebAnswersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebAnswersResponse,
        )

    def extract_competitors(
        self,
        *,
        domain: str,
        num_competitors: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_extract_competitors_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractCompetitorsResponse:
        """
        Find a company's direct competitors from its website and web search results.
        Each competitor comes with a confidence level and the search results behind it.

        Args:
          domain: Company domain, such as `stripe.com`. Full URLs are reduced to their domain.

          num_competitors: Exact number of direct competitors to return.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/competitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "num_competitors": num_competitors,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "zdr": zdr,
                    },
                    web_extract_competitors_params.WebExtractCompetitorsParams,
                ),
            ),
            cast_to=WebExtractCompetitorsResponse,
        )

    def extract_styleguide(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_extract_styleguide_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractStyleguideResponse:
        """
        Extract a website's design system: colors, typography, spacing, shadows, button
        and card styles, and downloadable font files. Every component style includes
        ready-to-use CSS.

        Args:
          color_scheme: Emulate a light or dark color scheme. Each scheme is cached separately.

          direct_url: Exact page URL to analyze. Provide either `domain` or `directUrl`, not both.

          domain: Domain to analyze, such as `stripe.com`. Provide either `domain` or `directUrl`,
              not both.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 90 days (7776000000 ms). Values above 1 year (31536000000 ms) are
              capped at 1 year.

          policies: Comma-separated access policy IDs to apply; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns off request logs and traces and keeps request and response
              content out of usage logs. Brand data and hosted assets may still be stored.
              Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.

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
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "policies": policies,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "zdr": zdr,
                    },
                    web_extract_styleguide_params.WebExtractStyleguideParams,
                ),
            ),
            cast_to=WebExtractStyleguideResponse,
        )

    def map_urls(
        self,
        *,
        domain: str,
        exclude_url_regex: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_subdomains: bool | Omit = omit,
        max_links: int | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_map_urls_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebMapURLsResponse:
        """
        Map up to 100,000 URLs on a domain, with titles, descriptions, keywords, and
        language when available. Filter with regex patterns, or rank by topic with
        `search` for 1 extra credit. Newly discovered URLs can lack metadata.

        Args:
          domain: Domain to map, such as `stripe.com`.

          exclude_url_regex: Leave out URLs matching this regex, even when they match `urlRegex`.

          headers: HTTP headers to send to the target site. Requests with headers skip the cache.

          include_subdomains: Include URLs on subdomains.

          max_links: Maximum number of URLs to return.

          policies: Comma-separated access policy IDs to apply; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          search: Filter URLs by a topic or phrase, most relevant first.

          sitemap_url: Fetch this sitemap instead of discovering sitemaps. Must belong to the domain or
              a subdomain.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Only return URLs matching this regex. Only matches count toward `maxLinks`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/web/urls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "exclude_url_regex": exclude_url_regex,
                        "headers": headers,
                        "include_subdomains": include_subdomains,
                        "max_links": max_links,
                        "policies": policies,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "url_regex": url_regex,
                        "zdr": zdr,
                    },
                    web_map_urls_params.WebMapURLsParams,
                ),
            ),
            cast_to=WebMapURLsResponse,
        )

    def scrape(
        self,
        *,
        formats: web_scrape_params.Formats,
        url: str,
        highlights_params: web_scrape_params.HighlightsParams | Omit = omit,
        image_params: web_scrape_params.ImageParams | Omit = omit,
        json_params: web_scrape_params.JsonParams | Omit = omit,
        markdown_params: web_scrape_params.MarkdownParams | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_params: web_scrape_params.ParseParams | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        product_params: web_scrape_params.ProductParams | Omit = omit,
        screenshot_params: web_scrape_params.ScreenshotParams | Omit = omit,
        shared_params: web_scrape_params.SharedParams | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_scrape_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScrapeResponse:
        """
        Turn any URL into Markdown, HTML, a screenshot, images, raw bytes, parsed
        fields, product data, highlights, or schema-matched JSON in one request. Choose
        the outputs in `formats`; each one succeeds or fails on its own. Handles PDF,
        Word, Excel, PowerPoint, and 40 other file formats.

        Args:
          formats: Outputs to return. Set at least one to `true`.

          url: Public HTTP or HTTPS URL to scrape.

          highlights_params: Query for the `highlights` output. Required when `formats.highlights` is `true`,
              and allowed only then.

          image_params: Options for the `images` output. Requires `formats.images: true`.

          json_params: Schema and instructions for the `json` output. Required when `formats.json` is
              `true`, and allowed only then.

          markdown_params: Options for the `markdown` output. Requires `formats.markdown: true`.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms).

          parse_params: Custom rules or a prebuilt parser for the `parsed` output. Required when
              `formats.parse` is `true`, and allowed only then.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          product_params: Options for the `product` output. Requires `formats.product: true`.

          screenshot_params: Options for the `screenshot` output. Requires `formats.screenshot: true`.

          shared_params: Browser and content settings shared by all outputs.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web/scrape",
            body=maybe_transform(
                {
                    "formats": formats,
                    "url": url,
                    "highlights_params": highlights_params,
                    "image_params": image_params,
                    "json_params": json_params,
                    "markdown_params": markdown_params,
                    "max_age_ms": max_age_ms,
                    "parse_params": parse_params,
                    "policies": policies,
                    "product_params": product_params,
                    "screenshot_params": screenshot_params,
                    "shared_params": shared_params,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_scrape_params.WebScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebScrapeResponse,
        )

    def screenshot(
        self,
        *,
        clear_popups: bool | Omit = omit,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        handle_cookie_popup: bool | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_screenshot_params.TimeoutOpts | Omit = omit,
        viewport: web_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """
        Capture a screenshot of a website's home page, a page type such as pricing, or
        an exact URL. Returns the visible viewport, a scroll slice, or the full page.

        Args:
          clear_popups: Dismiss cookie banners and close other popups and overlays before capture.

          color_scheme: Emulate a light or dark color scheme.

          country: Country to fetch from, as an ISO 3166-1 alpha-2 code.

          direct_url: Exact URL to capture, such as `https://example.com/pricing`. Provide either
              `domain` or `directUrl`, not both.

          domain: Domain to capture, such as `stripe.com`. Provide either `domain` or `directUrl`,
              not both.

          full_screenshot: Capture the full scrollable page instead of only the viewport.

          handle_cookie_popup: Dismiss cookie consent banners before capture.

          headers: HTTP headers to send to the target origin, such as
              `headers[Authorization]=Bearer token`. Requests with headers skip the cache and
              return the image as a data URL.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 1 day (86400000 ms). Maximum: 30 days (2592000000 ms).

          page: Capture this type of page instead of the home page. Context.dev finds it among
              the domain's links, in 30 languages. Only with `domain`.

          scroll_offset: Return the viewport-sized slice of the full page that starts this many pixels
              from the top. Step by the viewport height, such as `0`, `1080`, `2160`, to walk
              a long page. The last slice can be shorter. Overrides `fullScreenshot`.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          viewport: Browser viewport size in pixels.

          wait_for_ms: Time to wait after the page loads before capturing, in milliseconds. `0` waits
              500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus 10000 ms,
              or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
                        "clear_popups": clear_popups,
                        "color_scheme": color_scheme,
                        "country": country,
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "handle_cookie_popup": handle_cookie_popup,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    def search(
        self,
        *,
        query: str,
        country: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        description_max_characters: Optional[int] | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"] | Omit = omit,
        highlights_options: Optional[web_search_params.HighlightsOptions] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        languages: Union[
            Literal["all"],
            List[
                Literal[
                    "am",
                    "ar",
                    "az",
                    "be",
                    "bg",
                    "bn",
                    "ca",
                    "ceb",
                    "cs",
                    "cy",
                    "da",
                    "de",
                    "el",
                    "en",
                    "es",
                    "et",
                    "eu",
                    "fa",
                    "fi",
                    "fr",
                    "gu",
                    "ha",
                    "haw",
                    "he",
                    "hi",
                    "hr",
                    "hu",
                    "hy",
                    "id",
                    "is",
                    "it",
                    "ja",
                    "ka",
                    "kk",
                    "kn",
                    "ko",
                    "ku",
                    "ky",
                    "lo",
                    "lt",
                    "lv",
                    "mk",
                    "ml",
                    "mn",
                    "mr",
                    "ms",
                    "ne",
                    "nl",
                    "no",
                    "or",
                    "pa",
                    "pl",
                    "ps",
                    "pt",
                    "ro",
                    "ru",
                    "sk",
                    "sl",
                    "so",
                    "sq",
                    "sr",
                    "sv",
                    "sw",
                    "ta",
                    "te",
                    "th",
                    "tl",
                    "tr",
                    "uk",
                    "ur",
                    "uz",
                    "vi",
                    "yo",
                    "zh",
                ]
            ],
        ]
        | Omit = omit,
        markdown_options: Optional[web_search_params.MarkdownOptions] | Omit = omit,
        num_results: int | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_search_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResponse:
        """
        Search the web and get ranked results, with optional page Markdown or
        query-relevant passages for each one. Supports search operators and filters for
        domain, freshness, country, and language.

        Args:
          query: Search query. Accepts natural language and search operators such as `site:`,
              `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Localize results to this country, as an ISO 3166-1 alpha-2 code such as `us` or
              `de`.

          description_max_characters: Maximum length of each result's `description`, in characters.

          exclude_domains: Leave out results from these domains, such as `pinterest.com`.

          freshness: Restrict results to content published within this window.

          highlights_options: Return passages from each result page that are relevant to the query. Pages are
              read with the `markdownOptions` settings.

          include_domains: Only return results from these domains, such as `arxiv.org`.

          languages: Languages to return results in, as BCP 47 codes such as `en` or `de`, or `all`
              for any language.

          markdown_options: Scrape each result page to Markdown. Set `enabled` to `true` to turn it on.

          num_results: Number of results to return.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web/search",
            body=maybe_transform(
                {
                    "query": query,
                    "country": country,
                    "description_max_characters": description_max_characters,
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "highlights_options": highlights_options,
                    "include_domains": include_domains,
                    "languages": languages,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_search_params.WebSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchResponse,
        )

    def web_crawl_md(
        self,
        *,
        url: str,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_url_regex: str | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: Union[bool, Literal["auto"]] | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_web_crawl_md_params.Pdf | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        source_preference: List[Literal["html-conversion", "markdown-direct"]] | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_web_crawl_md_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Crawl up to 500 pages from a start URL and get each page back as Markdown with
        metadata. Control scope with depth limits, regex patterns, and subdomain rules.
        For larger crawls, use a batch.

        Args:
          url: Start URL, including `http://` or `https://`.

          country: Country to fetch from, as an ISO 3166-1 alpha-2 code.

          exclude_selectors: Remove elements matching these CSS selectors. Overrides `includeSelectors`.

          exclude_url_regex: Never follow or scrape URLs matching this regex, even when they match
              `urlRegex`. The start URL is always scraped.

          follow_subdomains: Follow links to subdomains of the start URL's domain, such as `docs.example.com`
              from `example.com`. `www` and the apex domain always count as the same site.

          include_frames: Which iframe contents to include in each page's Markdown. `auto` inlines only
              iframes that hold page content, such as same-site documents, framesets, job
              boards, forms, and embedded documents, and skips ads and widgets. `true` inlines
              every iframe; `false` inlines none.

          include_images: Include image references in the Markdown (`html-conversion` only).

          include_links: Keep link URLs in the Markdown (`html-conversion` only).

          include_selectors: Keep only elements matching these CSS selectors.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 1 day (86400000 ms). Maximum: 30 days (2592000000 ms).

          max_depth: Maximum link depth from the start URL. `0` crawls only the start URL. Omit for
              no depth limit.

          max_pages: Maximum number of pages to crawl.

          pdf: Whether to parse PDFs and which pages to read.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          settle_animations: Wait briefly for CSS animations and transitions to settle before reading each
              page.

          shorten_base64_images: Shorten inline base64 image data (`html-conversion` only).

          source_preference: Markdown sources in order of preference: `html-conversion` converts the page
              HTML, `markdown-direct` uses Markdown the site publishes.

          stop_after_ms: Soft time budget for the crawl, in milliseconds. When it runs out, the crawl
              returns the pages collected so far. Larger values are capped at 110 seconds.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Only follow and scrape URLs matching this regex. A prefix pattern of the form
              `^<start URL>` also follows a redirect of the start page.

          use_main_content_only: Keep only the main content, without navigation, headers, footers, or sidebars.

          wait_for_ms: Time to wait after each page loads before reading it, in milliseconds. `0` waits
              500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus 10000 ms,
              or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
                    "country": country,
                    "exclude_selectors": exclude_selectors,
                    "exclude_url_regex": exclude_url_regex,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "include_selectors": include_selectors,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "policies": policies,
                    "settle_animations": settle_animations,
                    "shorten_base64_images": shorten_base64_images,
                    "source_preference": source_preference,
                    "stop_after_ms": stop_after_ms,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
                    "wait_for_ms": wait_for_ms,
                    "zdr": zdr,
                },
                web_web_crawl_md_params.WebWebCrawlMdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebWebCrawlMdResponse,
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

    async def answers(
        self,
        *,
        task: str,
        controls: web_answers_params.Controls | Omit = omit,
        json_format: Dict[str, object] | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_answers_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebAnswersResponse:
        """
        Research a task across the live web and Context.dev's company and people data,
        and get the answer in the JSON shape you provide, with the URLs it used. `fast`
        (10 credits) suits short lookups; `ultra` (100 credits, the default) reads more
        sources for deeper research.

        Args:
          task: What to research, in plain language, up to 2000 characters. Include domains or
              URLs to focus the research.

          controls: Limit which sites the research can search, read, and cite.

          json_format: Example of the answer object to return, not a JSON Schema. Up to 8 levels deep,
              500 values, and 16,000 characters. Values that cannot be found come back as
              `null`. Defaults to `{ "result": "" }`.

          mode: `fast` prioritizes speed and adds extra verification for people and companies;
              `ultra` searches and reads more sources for deeper research. Defaults to
              `ultra`.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web/answers",
            body=await async_maybe_transform(
                {
                    "task": task,
                    "controls": controls,
                    "json_format": json_format,
                    "mode": mode,
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_answers_params.WebAnswersParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebAnswersResponse,
        )

    async def extract_competitors(
        self,
        *,
        domain: str,
        num_competitors: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_extract_competitors_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractCompetitorsResponse:
        """
        Find a company's direct competitors from its website and web search results.
        Each competitor comes with a confidence level and the search results behind it.

        Args:
          domain: Company domain, such as `stripe.com`. Full URLs are reduced to their domain.

          num_competitors: Exact number of direct competitors to return.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/competitors",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "num_competitors": num_competitors,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "zdr": zdr,
                    },
                    web_extract_competitors_params.WebExtractCompetitorsParams,
                ),
            ),
            cast_to=WebExtractCompetitorsResponse,
        )

    async def extract_styleguide(
        self,
        *,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_extract_styleguide_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractStyleguideResponse:
        """
        Extract a website's design system: colors, typography, spacing, shadows, button
        and card styles, and downloadable font files. Every component style includes
        ready-to-use CSS.

        Args:
          color_scheme: Emulate a light or dark color scheme. Each scheme is cached separately.

          direct_url: Exact page URL to analyze. Provide either `domain` or `directUrl`, not both.

          domain: Domain to analyze, such as `stripe.com`. Provide either `domain` or `directUrl`,
              not both.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 90 days (7776000000 ms). Values above 1 year (31536000000 ms) are
              capped at 1 year.

          policies: Comma-separated access policy IDs to apply; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns off request logs and traces and keeps request and response
              content out of usage logs. Brand data and hosted assets may still be stored.
              Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.

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
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "policies": policies,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "zdr": zdr,
                    },
                    web_extract_styleguide_params.WebExtractStyleguideParams,
                ),
            ),
            cast_to=WebExtractStyleguideResponse,
        )

    async def map_urls(
        self,
        *,
        domain: str,
        exclude_url_regex: str | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        include_subdomains: bool | Omit = omit,
        max_links: int | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_map_urls_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebMapURLsResponse:
        """
        Map up to 100,000 URLs on a domain, with titles, descriptions, keywords, and
        language when available. Filter with regex patterns, or rank by topic with
        `search` for 1 extra credit. Newly discovered URLs can lack metadata.

        Args:
          domain: Domain to map, such as `stripe.com`.

          exclude_url_regex: Leave out URLs matching this regex, even when they match `urlRegex`.

          headers: HTTP headers to send to the target site. Requests with headers skip the cache.

          include_subdomains: Include URLs on subdomains.

          max_links: Maximum number of URLs to return.

          policies: Comma-separated access policy IDs to apply; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          search: Filter URLs by a topic or phrase, most relevant first.

          sitemap_url: Fetch this sitemap instead of discovering sitemaps. Must belong to the domain or
              a subdomain.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Only return URLs matching this regex. Only matches count toward `maxLinks`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/web/urls",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "exclude_url_regex": exclude_url_regex,
                        "headers": headers,
                        "include_subdomains": include_subdomains,
                        "max_links": max_links,
                        "policies": policies,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "url_regex": url_regex,
                        "zdr": zdr,
                    },
                    web_map_urls_params.WebMapURLsParams,
                ),
            ),
            cast_to=WebMapURLsResponse,
        )

    async def scrape(
        self,
        *,
        formats: web_scrape_params.Formats,
        url: str,
        highlights_params: web_scrape_params.HighlightsParams | Omit = omit,
        image_params: web_scrape_params.ImageParams | Omit = omit,
        json_params: web_scrape_params.JsonParams | Omit = omit,
        markdown_params: web_scrape_params.MarkdownParams | Omit = omit,
        max_age_ms: int | Omit = omit,
        parse_params: web_scrape_params.ParseParams | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        product_params: web_scrape_params.ProductParams | Omit = omit,
        screenshot_params: web_scrape_params.ScreenshotParams | Omit = omit,
        shared_params: web_scrape_params.SharedParams | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_scrape_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScrapeResponse:
        """
        Turn any URL into Markdown, HTML, a screenshot, images, raw bytes, parsed
        fields, product data, highlights, or schema-matched JSON in one request. Choose
        the outputs in `formats`; each one succeeds or fails on its own. Handles PDF,
        Word, Excel, PowerPoint, and 40 other file formats.

        Args:
          formats: Outputs to return. Set at least one to `true`.

          url: Public HTTP or HTTPS URL to scrape.

          highlights_params: Query for the `highlights` output. Required when `formats.highlights` is `true`,
              and allowed only then.

          image_params: Options for the `images` output. Requires `formats.images: true`.

          json_params: Schema and instructions for the `json` output. Required when `formats.json` is
              `true`, and allowed only then.

          markdown_params: Options for the `markdown` output. Requires `formats.markdown: true`.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms).

          parse_params: Custom rules or a prebuilt parser for the `parsed` output. Required when
              `formats.parse` is `true`, and allowed only then.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          product_params: Options for the `product` output. Requires `formats.product: true`.

          screenshot_params: Options for the `screenshot` output. Requires `formats.screenshot: true`.

          shared_params: Browser and content settings shared by all outputs.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web/scrape",
            body=await async_maybe_transform(
                {
                    "formats": formats,
                    "url": url,
                    "highlights_params": highlights_params,
                    "image_params": image_params,
                    "json_params": json_params,
                    "markdown_params": markdown_params,
                    "max_age_ms": max_age_ms,
                    "parse_params": parse_params,
                    "policies": policies,
                    "product_params": product_params,
                    "screenshot_params": screenshot_params,
                    "shared_params": shared_params,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_scrape_params.WebScrapeParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebScrapeResponse,
        )

    async def screenshot(
        self,
        *,
        clear_popups: bool | Omit = omit,
        color_scheme: Literal["light", "dark"] | Omit = omit,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        full_screenshot: Literal["true", "false"] | Omit = omit,
        handle_cookie_popup: bool | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_screenshot_params.TimeoutOpts | Omit = omit,
        viewport: web_screenshot_params.Viewport | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebScreenshotResponse:
        """
        Capture a screenshot of a website's home page, a page type such as pricing, or
        an exact URL. Returns the visible viewport, a scroll slice, or the full page.

        Args:
          clear_popups: Dismiss cookie banners and close other popups and overlays before capture.

          color_scheme: Emulate a light or dark color scheme.

          country: Country to fetch from, as an ISO 3166-1 alpha-2 code.

          direct_url: Exact URL to capture, such as `https://example.com/pricing`. Provide either
              `domain` or `directUrl`, not both.

          domain: Domain to capture, such as `stripe.com`. Provide either `domain` or `directUrl`,
              not both.

          full_screenshot: Capture the full scrollable page instead of only the viewport.

          handle_cookie_popup: Dismiss cookie consent banners before capture.

          headers: HTTP headers to send to the target origin, such as
              `headers[Authorization]=Bearer token`. Requests with headers skip the cache and
              return the image as a data URL.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 1 day (86400000 ms). Maximum: 30 days (2592000000 ms).

          page: Capture this type of page instead of the home page. Context.dev finds it among
              the domain's links, in 30 languages. Only with `domain`.

          scroll_offset: Return the viewport-sized slice of the full page that starts this many pixels
              from the top. Step by the viewport height, such as `0`, `1080`, `2160`, to walk
              a long page. The last slice can be shorter. Overrides `fullScreenshot`.

          tags: Comma-separated labels for this request, such as `production,team-alpha`. Filter
              usage and request logs by them.

          timeout_opts: Request deadline and what to return when it passes.

          viewport: Browser viewport size in pixels.

          wait_for_ms: Time to wait after the page loads before capturing, in milliseconds. `0` waits
              500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus 10000 ms,
              or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
                        "clear_popups": clear_popups,
                        "color_scheme": color_scheme,
                        "country": country,
                        "direct_url": direct_url,
                        "domain": domain,
                        "full_screenshot": full_screenshot,
                        "handle_cookie_popup": handle_cookie_popup,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_opts": timeout_opts,
                        "viewport": viewport,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
                    },
                    web_screenshot_params.WebScreenshotParams,
                ),
            ),
            cast_to=WebScreenshotResponse,
        )

    async def search(
        self,
        *,
        query: str,
        country: Literal[
            "af",
            "al",
            "dz",
            "as",
            "ad",
            "ao",
            "ai",
            "aq",
            "ag",
            "ar",
            "am",
            "aw",
            "au",
            "at",
            "az",
            "bs",
            "bh",
            "bd",
            "bb",
            "by",
            "be",
            "bz",
            "bj",
            "bm",
            "bt",
            "bo",
            "ba",
            "bw",
            "bv",
            "br",
            "io",
            "bn",
            "bg",
            "bf",
            "bi",
            "kh",
            "cm",
            "ca",
            "cv",
            "ky",
            "cf",
            "td",
            "cl",
            "cn",
            "cx",
            "cc",
            "co",
            "km",
            "cg",
            "cd",
            "ck",
            "cr",
            "ci",
            "hr",
            "cu",
            "cy",
            "cz",
            "dk",
            "dj",
            "dm",
            "do",
            "ec",
            "eg",
            "sv",
            "gq",
            "er",
            "ee",
            "et",
            "fk",
            "fo",
            "fj",
            "fi",
            "fr",
            "gf",
            "pf",
            "tf",
            "ga",
            "gm",
            "ge",
            "de",
            "gh",
            "gi",
            "gr",
            "gl",
            "gd",
            "gp",
            "gu",
            "gt",
            "gn",
            "gw",
            "gy",
            "ht",
            "hm",
            "va",
            "hn",
            "hk",
            "hu",
            "is",
            "in",
            "id",
            "ir",
            "iq",
            "ie",
            "il",
            "it",
            "jm",
            "jp",
            "jo",
            "kz",
            "ke",
            "ki",
            "kp",
            "kr",
            "kw",
            "kg",
            "la",
            "lv",
            "lb",
            "ls",
            "lr",
            "ly",
            "li",
            "lt",
            "lu",
            "mo",
            "mk",
            "mg",
            "mw",
            "my",
            "mv",
            "ml",
            "mt",
            "mh",
            "mq",
            "mr",
            "mu",
            "yt",
            "mx",
            "fm",
            "md",
            "mc",
            "mn",
            "ms",
            "ma",
            "mz",
            "mm",
            "na",
            "nr",
            "np",
            "nl",
            "an",
            "nc",
            "nz",
            "ni",
            "ne",
            "ng",
            "nu",
            "nf",
            "mp",
            "no",
            "om",
            "pk",
            "pw",
            "ps",
            "pa",
            "pg",
            "py",
            "pe",
            "ph",
            "pn",
            "pl",
            "pt",
            "pr",
            "qa",
            "re",
            "ro",
            "ru",
            "rw",
            "sh",
            "kn",
            "lc",
            "pm",
            "vc",
            "ws",
            "sm",
            "st",
            "sa",
            "sn",
            "rs",
            "sc",
            "sl",
            "sg",
            "sk",
            "si",
            "sb",
            "so",
            "za",
            "gs",
            "es",
            "lk",
            "sd",
            "sr",
            "sj",
            "sz",
            "se",
            "ch",
            "sy",
            "tw",
            "tj",
            "tz",
            "th",
            "tl",
            "tg",
            "tk",
            "to",
            "tt",
            "tn",
            "tr",
            "tm",
            "tc",
            "tv",
            "ug",
            "ua",
            "ae",
            "gb",
            "us",
            "um",
            "uy",
            "uz",
            "vu",
            "ve",
            "vn",
            "vg",
            "vi",
            "wf",
            "eh",
            "ye",
            "zm",
            "zw",
        ]
        | Omit = omit,
        description_max_characters: Optional[int] | Omit = omit,
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"] | Omit = omit,
        highlights_options: Optional[web_search_params.HighlightsOptions] | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        languages: Union[
            Literal["all"],
            List[
                Literal[
                    "am",
                    "ar",
                    "az",
                    "be",
                    "bg",
                    "bn",
                    "ca",
                    "ceb",
                    "cs",
                    "cy",
                    "da",
                    "de",
                    "el",
                    "en",
                    "es",
                    "et",
                    "eu",
                    "fa",
                    "fi",
                    "fr",
                    "gu",
                    "ha",
                    "haw",
                    "he",
                    "hi",
                    "hr",
                    "hu",
                    "hy",
                    "id",
                    "is",
                    "it",
                    "ja",
                    "ka",
                    "kk",
                    "kn",
                    "ko",
                    "ku",
                    "ky",
                    "lo",
                    "lt",
                    "lv",
                    "mk",
                    "ml",
                    "mn",
                    "mr",
                    "ms",
                    "ne",
                    "nl",
                    "no",
                    "or",
                    "pa",
                    "pl",
                    "ps",
                    "pt",
                    "ro",
                    "ru",
                    "sk",
                    "sl",
                    "so",
                    "sq",
                    "sr",
                    "sv",
                    "sw",
                    "ta",
                    "te",
                    "th",
                    "tl",
                    "tr",
                    "uk",
                    "ur",
                    "uz",
                    "vi",
                    "yo",
                    "zh",
                ]
            ],
        ]
        | Omit = omit,
        markdown_options: Optional[web_search_params.MarkdownOptions] | Omit = omit,
        num_results: int | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_search_params.TimeoutOpts | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResponse:
        """
        Search the web and get ranked results, with optional page Markdown or
        query-relevant passages for each one. Supports search operators and filters for
        domain, freshness, country, and language.

        Args:
          query: Search query. Accepts natural language and search operators such as `site:`,
              `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Localize results to this country, as an ISO 3166-1 alpha-2 code such as `us` or
              `de`.

          description_max_characters: Maximum length of each result's `description`, in characters.

          exclude_domains: Leave out results from these domains, such as `pinterest.com`.

          freshness: Restrict results to content published within this window.

          highlights_options: Return passages from each result page that are relevant to the query. Pages are
              read with the `markdownOptions` settings.

          include_domains: Only return results from these domains, such as `arxiv.org`.

          languages: Languages to return results in, as BCP 47 codes such as `en` or `de`, or `all`
              for any language.

          markdown_options: Scrape each result page to Markdown. Set `enabled` to `true` to turn it on.

          num_results: Number of results to return.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web/search",
            body=await async_maybe_transform(
                {
                    "query": query,
                    "country": country,
                    "description_max_characters": description_max_characters,
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "highlights_options": highlights_options,
                    "include_domains": include_domains,
                    "languages": languages,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "zdr": zdr,
                },
                web_search_params.WebSearchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebSearchResponse,
        )

    async def web_crawl_md(
        self,
        *,
        url: str,
        country: Literal[
            "ad",
            "ae",
            "af",
            "ag",
            "ai",
            "al",
            "am",
            "ao",
            "ar",
            "at",
            "au",
            "aw",
            "az",
            "ba",
            "bb",
            "bd",
            "be",
            "bf",
            "bg",
            "bh",
            "bi",
            "bj",
            "bm",
            "bn",
            "bo",
            "bq",
            "br",
            "bs",
            "bw",
            "by",
            "bz",
            "ca",
            "cd",
            "cf",
            "cg",
            "ch",
            "ci",
            "cl",
            "cm",
            "cn",
            "co",
            "cr",
            "cv",
            "cw",
            "cy",
            "cz",
            "de",
            "dj",
            "dk",
            "dm",
            "do",
            "dz",
            "ec",
            "ee",
            "eg",
            "es",
            "et",
            "fi",
            "fj",
            "fr",
            "ga",
            "gb",
            "gd",
            "ge",
            "gf",
            "gg",
            "gh",
            "gm",
            "gn",
            "gp",
            "gq",
            "gr",
            "gt",
            "gu",
            "gw",
            "gy",
            "hk",
            "hn",
            "hr",
            "ht",
            "hu",
            "id",
            "ie",
            "il",
            "im",
            "in",
            "iq",
            "ir",
            "is",
            "it",
            "je",
            "jm",
            "jo",
            "jp",
            "ke",
            "kg",
            "kh",
            "kn",
            "kr",
            "kw",
            "ky",
            "kz",
            "la",
            "lb",
            "lc",
            "lk",
            "lr",
            "ls",
            "lt",
            "lu",
            "lv",
            "ly",
            "ma",
            "mc",
            "md",
            "me",
            "mf",
            "mg",
            "mk",
            "ml",
            "mm",
            "mn",
            "mo",
            "mq",
            "mr",
            "mt",
            "mu",
            "mv",
            "mw",
            "mx",
            "my",
            "mz",
            "na",
            "nc",
            "ne",
            "ng",
            "ni",
            "nl",
            "no",
            "np",
            "nz",
            "om",
            "pa",
            "pe",
            "pf",
            "pg",
            "ph",
            "pk",
            "pl",
            "pr",
            "ps",
            "pt",
            "py",
            "qa",
            "re",
            "ro",
            "rs",
            "ru",
            "rw",
            "sa",
            "sc",
            "sd",
            "se",
            "sg",
            "si",
            "sk",
            "sl",
            "sm",
            "sn",
            "so",
            "sr",
            "ss",
            "st",
            "sv",
            "sx",
            "sy",
            "sz",
            "tc",
            "td",
            "tg",
            "th",
            "tj",
            "tl",
            "tm",
            "tn",
            "tr",
            "tt",
            "tw",
            "tz",
            "ua",
            "ug",
            "us",
            "uy",
            "uz",
            "vc",
            "ve",
            "vg",
            "vi",
            "vn",
            "ye",
            "yt",
            "za",
            "zm",
            "zw",
        ]
        | Omit = omit,
        exclude_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        exclude_url_regex: str | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: Union[bool, Literal["auto"]] | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_web_crawl_md_params.Pdf | Omit = omit,
        policies: SequenceNotStr[str] | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        source_preference: List[Literal["html-conversion", "markdown-direct"]] | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_web_crawl_md_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """
        Crawl up to 500 pages from a start URL and get each page back as Markdown with
        metadata. Control scope with depth limits, regex patterns, and subdomain rules.
        For larger crawls, use a batch.

        Args:
          url: Start URL, including `http://` or `https://`.

          country: Country to fetch from, as an ISO 3166-1 alpha-2 code.

          exclude_selectors: Remove elements matching these CSS selectors. Overrides `includeSelectors`.

          exclude_url_regex: Never follow or scrape URLs matching this regex, even when they match
              `urlRegex`. The start URL is always scraped.

          follow_subdomains: Follow links to subdomains of the start URL's domain, such as `docs.example.com`
              from `example.com`. `www` and the apex domain always count as the same site.

          include_frames: Which iframe contents to include in each page's Markdown. `auto` inlines only
              iframes that hold page content, such as same-site documents, framesets, job
              boards, forms, and embedded documents, and skips ads and widgets. `true` inlines
              every iframe; `false` inlines none.

          include_images: Include image references in the Markdown (`html-conversion` only).

          include_links: Keep link URLs in the Markdown (`html-conversion` only).

          include_selectors: Keep only elements matching these CSS selectors.

          max_age_ms: Maximum age of a cached result, in milliseconds. `0` always fetches fresh.
              Defaults to 1 day (86400000 ms). Maximum: 30 days (2592000000 ms).

          max_depth: Maximum link depth from the start URL. `0` crawls only the start URL. Omit for
              no depth limit.

          max_pages: Maximum number of pages to crawl.

          pdf: Whether to parse PDFs and which pages to read.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          settle_animations: Wait briefly for CSS animations and transitions to settle before reading each
              page.

          shorten_base64_images: Shorten inline base64 image data (`html-conversion` only).

          source_preference: Markdown sources in order of preference: `html-conversion` converts the page
              HTML, `markdown-direct` uses Markdown the site publishes.

          stop_after_ms: Soft time budget for the crawl, in milliseconds. When it runs out, the crawl
              returns the pages collected so far. Larger values are capped at 110 seconds.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Only follow and scrape URLs matching this regex. A prefix pattern of the form
              `^<start URL>` also follows a redirect of the start page.

          use_main_content_only: Keep only the main content, without navigation, headers, footers, or sidebars.

          wait_for_ms: Time to wait after each page loads before reading it, in milliseconds. `0` waits
              500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus 10000 ms,
              or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
                    "country": country,
                    "exclude_selectors": exclude_selectors,
                    "exclude_url_regex": exclude_url_regex,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "include_selectors": include_selectors,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "policies": policies,
                    "settle_animations": settle_animations,
                    "shorten_base64_images": shorten_base64_images,
                    "source_preference": source_preference,
                    "stop_after_ms": stop_after_ms,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "url_regex": url_regex,
                    "use_main_content_only": use_main_content_only,
                    "wait_for_ms": wait_for_ms,
                    "zdr": zdr,
                },
                web_web_crawl_md_params.WebWebCrawlMdParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebWebCrawlMdResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.answers = to_raw_response_wrapper(
            web.answers,
        )
        self.extract_competitors = to_raw_response_wrapper(
            web.extract_competitors,
        )
        self.extract_styleguide = to_raw_response_wrapper(
            web.extract_styleguide,
        )
        self.map_urls = to_raw_response_wrapper(
            web.map_urls,
        )
        self.scrape = to_raw_response_wrapper(
            web.scrape,
        )
        self.screenshot = to_raw_response_wrapper(
            web.screenshot,
        )
        self.search = to_raw_response_wrapper(
            web.search,
        )
        self.web_crawl_md = to_raw_response_wrapper(
            web.web_crawl_md,
        )


class AsyncWebResourceWithRawResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.answers = async_to_raw_response_wrapper(
            web.answers,
        )
        self.extract_competitors = async_to_raw_response_wrapper(
            web.extract_competitors,
        )
        self.extract_styleguide = async_to_raw_response_wrapper(
            web.extract_styleguide,
        )
        self.map_urls = async_to_raw_response_wrapper(
            web.map_urls,
        )
        self.scrape = async_to_raw_response_wrapper(
            web.scrape,
        )
        self.screenshot = async_to_raw_response_wrapper(
            web.screenshot,
        )
        self.search = async_to_raw_response_wrapper(
            web.search,
        )
        self.web_crawl_md = async_to_raw_response_wrapper(
            web.web_crawl_md,
        )


class WebResourceWithStreamingResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.answers = to_streamed_response_wrapper(
            web.answers,
        )
        self.extract_competitors = to_streamed_response_wrapper(
            web.extract_competitors,
        )
        self.extract_styleguide = to_streamed_response_wrapper(
            web.extract_styleguide,
        )
        self.map_urls = to_streamed_response_wrapper(
            web.map_urls,
        )
        self.scrape = to_streamed_response_wrapper(
            web.scrape,
        )
        self.screenshot = to_streamed_response_wrapper(
            web.screenshot,
        )
        self.search = to_streamed_response_wrapper(
            web.search,
        )
        self.web_crawl_md = to_streamed_response_wrapper(
            web.web_crawl_md,
        )


class AsyncWebResourceWithStreamingResponse:
    def __init__(self, web: AsyncWebResource) -> None:
        self._web = web

        self.answers = async_to_streamed_response_wrapper(
            web.answers,
        )
        self.extract_competitors = async_to_streamed_response_wrapper(
            web.extract_competitors,
        )
        self.extract_styleguide = async_to_streamed_response_wrapper(
            web.extract_styleguide,
        )
        self.map_urls = async_to_streamed_response_wrapper(
            web.map_urls,
        )
        self.scrape = async_to_streamed_response_wrapper(
            web.scrape,
        )
        self.screenshot = async_to_streamed_response_wrapper(
            web.screenshot,
        )
        self.search = async_to_streamed_response_wrapper(
            web.search,
        )
        self.web_crawl_md = async_to_streamed_response_wrapper(
            web.web_crawl_md,
        )
