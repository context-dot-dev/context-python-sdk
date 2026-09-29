# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
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
        json_format: Dict[str, object] | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
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
        """Research the web and return a sourced answer in your JSON shape.

        Choose `fast`
        for a short task or `ultra` for deeper research.

        Args:
          task: Research task. The agent selects company/profile lookups, web searches, or page
              reads. Include domains or URLs to focus the research.

          json_format: Example answer object, not JSON Schema. Up to 8 levels, 500 values, and 16000
              characters; unknowns may be null.

          mode: `fast` prioritizes speed, with extra verification for people and companies;
              `ultra` supports deeper research (default).

          tags: Labels for filtering usage in the dashboard.

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
                    "json_format": json_format,
                    "mode": mode,
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
        Analyze a company's landing page and web search evidence to return direct
        competitors for the same product or market.

        Args:
          domain: Company domain to analyze, such as `stripe.com`. Full http(s) URLs are accepted
              and normalized to their domain.

          num_competitors: Exact number of direct competitors to return. Defaults to 5.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

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
        Extract colors, typography, spacing, and component styles from a website.

        Args:
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: Exact URL to inspect. Provide either `domain` or `directUrl`, not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age of cached brand data in ms. Defaults to 3 months; clamped to 0–1
              year. `0` refreshes.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
        headers: Dict[str, str] | Omit = omit,
        include_subdomains: bool | Omit = omit,
        max_links: int | Omit = omit,
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
        Discover a site's URLs, with page titles, descriptions, keywords, and language
        when available. Metadata can be missing on newly discovered URLs.

        Args:
          domain: Domain to map, e.g. `stripe.com`.

          headers: HTTP headers for the target origin. Non-empty headers bypass caching.

          include_subdomains: Include URLs on subdomains.

          max_links: Maximum number of URLs to return.

          search: Filter URLs by a topic or phrase, most relevant first.

          sitemap_url: Fetch this sitemap instead of discovering sitemaps. Must belong to the domain or
              a subdomain.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

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
                        "headers": headers,
                        "include_subdomains": include_subdomains,
                        "max_links": max_links,
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
        """Scrape anything from a URL on the internet.

        Returns the outputs you enable in
        formats. Handles PDFs, DOCX, PPT, XLSX, and 40 other file formats.

        Args:
          formats: Outputs to return. Set at least one to `true`.

          url: Public HTTP or HTTPS URL to scrape.

          highlights_params: Requires `formats.highlights: true`; required when it is set.

          image_params: Image options. Requires formats.images: true.

          json_params: Requires `formats.json: true`; required when it is set.

          markdown_params: Markdown options. Requires `formats.markdown`.

          max_age_ms: Maximum age of a cached output, in milliseconds. `0` fetches fresh. Defaults to
              3 days (259200000 ms). Maximum: 1 year (31536000000 ms).

          parse_params: Requires `formats.parse: true`; required when it is set.

          product_params: Product options. Requires formats.product: true.

          screenshot_params: Screenshot options. Requires formats.screenshot: true.

          shared_params: Browser and content settings shared by all outputs.

          tags: Labels for tracking request usage. Not retained when zdr is enabled.

          timeout_opts: Deadline for the whole request. Defaults to 90000 ms with `fail`. Fixed waits
              must end before it.

          zdr: `enabled` turns on zero data retention. Your organization must have ZDR enabled.

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
        Capture a screenshot of a website.

        Args:
          clear_popups: Optional parameter for comprehensive popup cleanup. If 'true', the browser
              dismisses detected cookie/consent UI and clears other detected obstructive
              popups and overlays before capture. If 'false' or not provided, this parameter
              requests no cleanup; handleCookiePopup can still request cookie/consent handling
              independently.

          color_scheme: Optional parameter to choose the site's visual theme in the screenshot. Use
              'light' or 'dark' when the site offers both appearances.

          country: Fetch from this country (ISO 3166-1 alpha-2).

          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          handle_cookie_popup: Optional parameter to control cookie/consent popup handling. If 'true', we
              dismiss cookie banner before capture. If 'false' or not provided, captures the
              page without that step.

          headers: Optional outbound HTTP headers, using the same JSON object or deep-object query
              format as other scrape endpoints (for example headers[Authorization]=Bearer
              token). Headers are scoped to the target origin during capture. For domain/page
              requests, discovery receives no custom headers and only pages on the resolved
              origin are eligible. Non-empty headers bypass screenshot caching and return an
              in-memory data URL; no screenshot is uploaded. Empty objects behave like omitted
              headers.

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          scroll_offset: Optional vertical scroll offset in pixels for capturing a long page in
              viewport-sized chunks. When provided, the full page is captured once and the
              returned image is the viewport-sized slice that begins at this Y offset (e.g.
              request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
              top to bottom). The final slice may be shorter than the viewport height. Takes
              precedence over fullScreenshot. Max: 100000.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted. When combined with timeoutOpts, timeoutOpts.milliseconds must be at
              least waitForMs + 10000 ms; a shorter deadline is rejected with 400
              TIMEOUT_TOO_SHORT_FOR_WAIT.

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
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"] | Omit = omit,
        highlights_options: web_search_params.HighlightsOptions | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        markdown_options: web_search_params.MarkdownOptions | Omit = omit,
        num_results: int | Omit = omit,
        query_fanout: bool | Omit = omit,
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
        Search the web and optionally return page content or relevant passages with each
        result.

        Args:
          query: Search query. Accepts natural language as well as Google-style search operators
              such as `site:`, `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Two-letter ISO 3166-1 alpha-2 country code to localize results to a specific
              country (maps to Google's `gl` parameter). Example: "us", "gb", "de".

          exclude_domains:
              Blocklist — drop results from these domains. Up to 100 domains. Example:
              ["pinterest.com", "reddit.com"].

          freshness: Restrict results to content published within this window.

          highlights_options: Passages from each result page that are relevant to the query. Pages are read
              with the `markdownOptions` settings.

          include_domains:
              Allowlist — only return results from these domains. Up to 100 domains. Example:
              ["arxiv.org", "github.com"].

          markdown_options: Inline Markdown scraping for each result. Set `enabled: true` to activate.

          num_results: Number of results to request and return (10–100). Defaults to 10.

          query_fanout: Currently has no effect.

          tags: Labels for filtering usage in the dashboard.

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
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "highlights_options": highlights_options,
                    "include_domains": include_domains,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "query_fanout": query_fanout,
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
        exclude_selectors: SequenceNotStr[str] | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: SequenceNotStr[str] | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_web_crawl_md_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_web_crawl_md_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """Crawl a website and return page content as Markdown.

        Use a batch for crawls
        beyond 500 pages.

        Args:
          url: Start URL, including `http://` or `https://`.

          country: Fetch from this country (ISO 3166-1 alpha-2).

          exclude_selectors: Remove matching elements after inclusions. Exclusions take precedence.

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          include_selectors: Keep matching HTML subtrees before converting each page to Markdown.

          max_age_ms: Maximum cache age in milliseconds. Defaults to 1 day; `0` fetches fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum pages to crawl.

          pdf: PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range.

          settle_animations: Wait briefly for CSS animations and transitions to settle before reading each
              page.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          stop_after_ms: Soft crawl deadline in milliseconds. Returns pages collected before the next
              deadline check.

          tags: Labels for filtering usage in the dashboard.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped. An
              automatic prefix scope in the form ^<starting URL> follows a redirect of the
              starting page.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Browser wait time in milliseconds after initial page load for each crawled page.
              Defaults to 3500 (3.5 seconds). Min: 0. Max: 30000 (30 seconds).

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
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "include_selectors": include_selectors,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "settle_animations": settle_animations,
                    "shorten_base64_images": shorten_base64_images,
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
        json_format: Dict[str, object] | Omit = omit,
        mode: Literal["fast", "ultra"] | Omit = omit,
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
        """Research the web and return a sourced answer in your JSON shape.

        Choose `fast`
        for a short task or `ultra` for deeper research.

        Args:
          task: Research task. The agent selects company/profile lookups, web searches, or page
              reads. Include domains or URLs to focus the research.

          json_format: Example answer object, not JSON Schema. Up to 8 levels, 500 values, and 16000
              characters; unknowns may be null.

          mode: `fast` prioritizes speed, with extra verification for people and companies;
              `ultra` supports deeper research (default).

          tags: Labels for filtering usage in the dashboard.

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
                    "json_format": json_format,
                    "mode": mode,
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
        Analyze a company's landing page and web search evidence to return direct
        competitors for the same product or market.

        Args:
          domain: Company domain to analyze, such as `stripe.com`. Full http(s) URLs are accepted
              and normalized to their domain.

          num_competitors: Exact number of direct competitors to return. Defaults to 5.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

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
        Extract colors, typography, spacing, and component styles from a website.

        Args:
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: Exact URL to inspect. Provide either `domain` or `directUrl`, not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age of cached brand data in ms. Defaults to 3 months; clamped to 0–1
              year. `0` refreshes.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          zdr: `enabled` turns on zero data retention. Returns 403 `ZDR_NOT_ENABLED` unless
              your organization has ZDR.

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
        headers: Dict[str, str] | Omit = omit,
        include_subdomains: bool | Omit = omit,
        max_links: int | Omit = omit,
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
        Discover a site's URLs, with page titles, descriptions, keywords, and language
        when available. Metadata can be missing on newly discovered URLs.

        Args:
          domain: Domain to map, e.g. `stripe.com`.

          headers: HTTP headers for the target origin. Non-empty headers bypass caching.

          include_subdomains: Include URLs on subdomains.

          max_links: Maximum number of URLs to return.

          search: Filter URLs by a topic or phrase, most relevant first.

          sitemap_url: Fetch this sitemap instead of discovering sitemaps. Must belong to the domain or
              a subdomain.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

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
                        "headers": headers,
                        "include_subdomains": include_subdomains,
                        "max_links": max_links,
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
        """Scrape anything from a URL on the internet.

        Returns the outputs you enable in
        formats. Handles PDFs, DOCX, PPT, XLSX, and 40 other file formats.

        Args:
          formats: Outputs to return. Set at least one to `true`.

          url: Public HTTP or HTTPS URL to scrape.

          highlights_params: Requires `formats.highlights: true`; required when it is set.

          image_params: Image options. Requires formats.images: true.

          json_params: Requires `formats.json: true`; required when it is set.

          markdown_params: Markdown options. Requires `formats.markdown`.

          max_age_ms: Maximum age of a cached output, in milliseconds. `0` fetches fresh. Defaults to
              3 days (259200000 ms). Maximum: 1 year (31536000000 ms).

          parse_params: Requires `formats.parse: true`; required when it is set.

          product_params: Product options. Requires formats.product: true.

          screenshot_params: Screenshot options. Requires formats.screenshot: true.

          shared_params: Browser and content settings shared by all outputs.

          tags: Labels for tracking request usage. Not retained when zdr is enabled.

          timeout_opts: Deadline for the whole request. Defaults to 90000 ms with `fail`. Fixed waits
              must end before it.

          zdr: `enabled` turns on zero data retention. Your organization must have ZDR enabled.

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
        Capture a screenshot of a website.

        Args:
          clear_popups: Optional parameter for comprehensive popup cleanup. If 'true', the browser
              dismisses detected cookie/consent UI and clears other detected obstructive
              popups and overlays before capture. If 'false' or not provided, this parameter
              requests no cleanup; handleCookiePopup can still request cookie/consent handling
              independently.

          color_scheme: Optional parameter to choose the site's visual theme in the screenshot. Use
              'light' or 'dark' when the site offers both appearances.

          country: Fetch from this country (ISO 3166-1 alpha-2).

          direct_url: A specific URL to screenshot directly, bypassing domain resolution (e.g.,
              'https://example.com/pricing'). When provided, the screenshot is taken of this
              exact URL. You must provide either 'domain' or 'directUrl', but not both.

          domain: Domain name to take screenshot of (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          full_screenshot: Optional parameter to determine screenshot type. If 'true', takes a full page
              screenshot capturing all content. If 'false' or not provided, takes a viewport
              screenshot (standard browser view).

          handle_cookie_popup: Optional parameter to control cookie/consent popup handling. If 'true', we
              dismiss cookie banner before capture. If 'false' or not provided, captures the
              page without that step.

          headers: Optional outbound HTTP headers, using the same JSON object or deep-object query
              format as other scrape endpoints (for example headers[Authorization]=Bearer
              token). Headers are scoped to the target origin during capture. For domain/page
              requests, discovery receives no custom headers and only pages on the resolved
              origin are eligible. Non-empty headers bypass screenshot caching and return an
              in-memory data URL; no screenshot is uploaded. Empty objects behave like omitted
              headers.

          max_age_ms: Return a cached screenshot if a prior screenshot for the same parameters exists
              and is younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always capture fresh.

          page: Optional parameter to specify which page type to screenshot. If provided, the
              system will scrape the domain's links and use heuristics to find the most
              appropriate URL for the specified page type (30 supported languages). If not
              provided, screenshots the main domain landing page. Only applicable when using
              'domain', not 'directUrl'.

          scroll_offset: Optional vertical scroll offset in pixels for capturing a long page in
              viewport-sized chunks. When provided, the full page is captured once and the
              returned image is the viewport-sized slice that begins at this Y offset (e.g.
              request scrollOffset=0, then 1080, then 2160 to walk a 1920x1080 landing page
              top to bottom). The final slice may be shorter than the viewport height. Takes
              precedence over fullScreenshot. Max: 100000.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          timeout_opts: Request deadline and what to return when it passes.

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted. When combined with timeoutOpts, timeoutOpts.milliseconds must be at
              least waitForMs + 10000 ms; a shorter deadline is rejected with 400
              TIMEOUT_TOO_SHORT_FOR_WAIT.

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
        exclude_domains: SequenceNotStr[str] | Omit = omit,
        freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"] | Omit = omit,
        highlights_options: web_search_params.HighlightsOptions | Omit = omit,
        include_domains: SequenceNotStr[str] | Omit = omit,
        markdown_options: web_search_params.MarkdownOptions | Omit = omit,
        num_results: int | Omit = omit,
        query_fanout: bool | Omit = omit,
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
        Search the web and optionally return page content or relevant passages with each
        result.

        Args:
          query: Search query. Accepts natural language as well as Google-style search operators
              such as `site:`, `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Two-letter ISO 3166-1 alpha-2 country code to localize results to a specific
              country (maps to Google's `gl` parameter). Example: "us", "gb", "de".

          exclude_domains:
              Blocklist — drop results from these domains. Up to 100 domains. Example:
              ["pinterest.com", "reddit.com"].

          freshness: Restrict results to content published within this window.

          highlights_options: Passages from each result page that are relevant to the query. Pages are read
              with the `markdownOptions` settings.

          include_domains:
              Allowlist — only return results from these domains. Up to 100 domains. Example:
              ["arxiv.org", "github.com"].

          markdown_options: Inline Markdown scraping for each result. Set `enabled: true` to activate.

          num_results: Number of results to request and return (10–100). Defaults to 10.

          query_fanout: Currently has no effect.

          tags: Labels for filtering usage in the dashboard.

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
                    "exclude_domains": exclude_domains,
                    "freshness": freshness,
                    "highlights_options": highlights_options,
                    "include_domains": include_domains,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "query_fanout": query_fanout,
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
        exclude_selectors: SequenceNotStr[str] | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: SequenceNotStr[str] | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_web_crawl_md_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: web_web_crawl_md_params.TimeoutOpts | Omit = omit,
        url_regex: str | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: int | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebCrawlMdResponse:
        """Crawl a website and return page content as Markdown.

        Use a batch for crawls
        beyond 500 pages.

        Args:
          url: Start URL, including `http://` or `https://`.

          country: Fetch from this country (ISO 3166-1 alpha-2).

          exclude_selectors: Remove matching elements after inclusions. Exclusions take precedence.

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          include_selectors: Keep matching HTML subtrees before converting each page to Markdown.

          max_age_ms: Maximum cache age in milliseconds. Defaults to 1 day; `0` fetches fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum pages to crawl.

          pdf: PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range.

          settle_animations: Wait briefly for CSS animations and transitions to settle before reading each
              page.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          stop_after_ms: Soft crawl deadline in milliseconds. Returns pages collected before the next
              deadline check.

          tags: Labels for filtering usage in the dashboard.

          timeout_opts: Request deadline and what to return when it passes.

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped. An
              automatic prefix scope in the form ^<starting URL> follows a redirect of the
              starting page.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Browser wait time in milliseconds after initial page load for each crawled page.
              Defaults to 3500 (3.5 seconds). Min: 0. Max: 30000 (30 seconds).

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
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "include_images": include_images,
                    "include_links": include_links,
                    "include_selectors": include_selectors,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "settle_animations": settle_animations,
                    "shorten_base64_images": shorten_base64_images,
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
