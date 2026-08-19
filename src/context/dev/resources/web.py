# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal

import httpx

from ..types import (
    web_search_params,
    web_extract_params,
    web_screenshot_params,
    web_web_crawl_md_params,
    web_extract_fonts_params,
    web_web_scrape_md_params,
    web_web_scrape_html_params,
    web_web_scrape_images_params,
    web_extract_styleguide_params,
    web_web_scrape_sitemap_params,
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
from ..types.web_search_response import WebSearchResponse
from ..types.web_extract_response import WebExtractResponse
from ..types.web_screenshot_response import WebScreenshotResponse
from ..types.web_web_crawl_md_response import WebWebCrawlMdResponse
from ..types.web_extract_fonts_response import WebExtractFontsResponse
from ..types.web_web_scrape_md_response import WebWebScrapeMdResponse
from ..types.web_web_scrape_html_response import WebWebScrapeHTMLResponse
from ..types.web_web_scrape_images_response import WebWebScrapeImagesResponse
from ..types.web_extract_styleguide_response import WebExtractStyleguideResponse
from ..types.web_web_scrape_sitemap_response import WebWebScrapeSitemapResponse
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

    def extract(
        self,
        *,
        schema: Dict[str, object],
        url: str,
        fact_check: bool | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        instructions: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_extract_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractResponse:
        """
        Crawl a website, use the provided JSON Schema and instructions to prioritize
        relevant internal links, and extract structured data from the selected pages.

        Args:
          schema: JSON Schema for the returned data object. TypeScript Zod users can pass a JSON
              Schema generated from a Zod object; Python users can pass the equivalent JSON
              Schema object.

          url: The starting website URL to crawl and extract from. Must include http:// or
              https://.

          fact_check: When true, every returned value must be grounded in facts stated on the page;
              fields that cannot be supported by the page are returned as null/empty. When
              false (default), the model may make reasonable inferences and derivations from
              the page content (e.g. ideal customer, competitor analysis, recommendations)
              while keeping verifiable specifics (names, quotes, URLs, dates, metrics)
              faithful to the source.

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain.

          include_frames: When true, iframe contents are included in Markdown before extraction.

          instructions: Optional extraction guidance, such as which facts to prioritize or how to
              interpret fields in the schema.

          max_age_ms: Return cached scrape results if a prior scrape for the same parameters is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms).

          max_depth: Optional maximum link depth from the starting URL (0 = only the starting page).
              If omitted, there is no crawl depth limit.

          max_pages: Maximum number of pages to analyze for extraction. Hard cap: 50. Defaults to 5.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting each crawled page. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          stop_after_ms: Soft time budget for the crawl in milliseconds. Min: 10000 (10s). Max: 110000
              (110s). Default: 80000 (80s).

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load for each
              crawled page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/web/extract",
            body=maybe_transform(
                {
                    "schema": schema,
                    "url": url,
                    "fact_check": fact_check,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "instructions": instructions,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "settle_animations": settle_animations,
                    "stop_after_ms": stop_after_ms,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                    "wait_for_ms": wait_for_ms,
                },
                web_extract_params.WebExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebExtractResponse,
        )

    def extract_competitors(
        self,
        *,
        domain: str,
        num_competitors: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
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

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_competitors_params.WebExtractCompetitorsParams,
                ),
            ),
            cast_to=WebExtractCompetitorsResponse,
        )

    def extract_fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
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

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

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

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
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
        include_domains: SequenceNotStr[str] | Omit = omit,
        markdown_options: web_search_params.MarkdownOptions | Omit = omit,
        num_results: int | Omit = omit,
        query_fanout: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResponse:
        """
        Search the web and optionally scrape each result to Markdown in one round-trip.

        Args:
          query: Search query. Accepts natural language as well as Google-style search operators
              such as `site:`, `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Two-letter ISO 3166-1 alpha-2 country code to localize results to a specific
              country (maps to Google's `gl` parameter). Example: "us", "gb", "de".

          exclude_domains: Blocklist — drop results from these domains. Example: ["pinterest.com",
              "reddit.com"].

          freshness: Restrict results to content published within this window.

          include_domains: Allowlist — only return results from these domains. Example: ["arxiv.org",
              "github.com"].

          markdown_options: Inline Markdown scraping for each result. Set `enabled: true` to activate.

          num_results: Number of results to request and return (10–100). Defaults to 10.

          query_fanout: Expand the query into multiple parallel variants for broader recall.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                    "include_domains": include_domains,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "query_fanout": query_fanout,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
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
        timeout_ms: int | Omit = omit,
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
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before each crawled page is converted to Markdown.
              Applied after includeSelectors. Exclusion takes precedence: an element matching
              both is removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before each crawled page is converted to Markdown. When
              omitted, the entire document is kept. Examples: "article.main", "#content",
              "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting each crawled page. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          stop_after_ms: Soft time budget for the crawl in milliseconds. After each scrape, the crawler
              checks the elapsed time and, if exceeded, returns the pages collected so far
              instead of continuing. Min: 10000 (10s). Max: 110000 (110s). Default: 80000
              (80s).

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped. An
              automatic prefix scope in the form ^<starting URL> follows a redirect of the
              starting page.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Browser wait time in milliseconds after initial page load for each crawled page.
              Defaults to 3500 (3.5 seconds). Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                    "timeout_ms": timeout_ms,
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

    def web_scrape_html(
        self,
        *,
        url: str,
        actions: Optional[Iterable[web_web_scrape_html_params.Action]] | Omit = omit,
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
        headers: Dict[str, str] | Omit = omit,
        include_frames: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: web_web_scrape_html_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        The base
        request costs 1 credit; requests with browser actions cost 2 credits.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove from the result. Applied after includeSelectors.
              Exclusion takes precedence: an element matching both is removed. Examples:
              "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, iframes are rendered inline into the returned HTML.

          include_selectors: CSS selectors. When provided, only matching subtrees (and their descendants) are
              kept and everything else is dropped. When omitted, the entire document is kept.
              Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting HTML. Defaults to false. This adds a bit of latency in exchange for
              more stable output on animated pages.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: When true, return only the page's main content in the HTML response, excluding
              headers, footers, sidebars, and navigation when detectable.

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
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
        actions: Optional[Iterable[web_web_scrape_images_params.Action]] | Omit = omit,
        dedupe: bool | Omit = omit,
        enrichment: Optional[web_web_scrape_images_params.Enrichment] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
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
        embeds. The base request costs 1 credit, or 2 credits with browser actions. When
        enrichment is enabled, the entire call costs 5 credits, including requests that
        also use actions.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          dedupe: When true, visually duplicate images are removed: every image is loaded and
              perceptually hashed, and only the highest-resolution copy of each duplicate
              group is kept. Images that cannot be downloaded or hashed are kept. Default:
              false.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "actions": actions,
                        "dedupe": dedupe,
                        "enrichment": enrichment,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        actions: Optional[Iterable[web_web_scrape_md_params.Action]] | Omit = omit,
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
        headers: Dict[str, str] | Omit = omit,
        include_frames: bool | Omit = omit,
        include_html: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: web_web_scrape_md_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """Scrapes the given URL into LLM usable Markdown.

        Inspect key_metadata on JSON
        responses from a recognized API key; use error_code to distinguish stable
        failure categories.

        ### YouTube

        YouTube URLs return the video or channel itself rather than the surrounding
        player and navigation chrome. A URL addressing a single video (`/watch`,
        `youtu.be`, `/shorts`, `/embed`, `/live`) returns its title, channel, duration,
        view count, keywords, full description, and the transcript when the video has
        captions that can be retrieved; videos without captions return everything except
        the transcript. A channel URL (`/channel/UC…`, `/@handle`, `/c/…`, `/user/…`)
        returns its name, handle, subscriber count, video count, and full description.
        When `includeImages=true`, video responses also include the thumbnail and
        channel responses include the avatar. Costs the same as any other scrape.

        ### Billing & errors

        | HTTP status | Billed?                                   | Meaning                                                                                                                                                                                                                                                                                                       |
        | ----------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | 200         | Yes — 1 credit, or 2 credits with actions | Successful scrape, including a zero-length result when includeSelectors matched nothing                                                                                                                                                                                                                       |
        | 400         | No                                        | Invalid input, skipped PDF, or the page could not be scraped. error_code WEBSITE_BLOCKED specifically means the site answered with an anti-bot challenge, CAPTCHA wall, or login shell instead of the page (even when the site returned HTTP 200) — retrying later or from another country sometimes succeeds |
        | 401 / 403   | No                                        | Invalid/disabled key, insufficient permissions, or credits exhausted; inspect error_code                                                                                                                                                                                                                      |
        | 404         | No                                        | Target page returned or fingerprinted as not found                                                                                                                                                                                                                                                            |
        | 408         | No                                        | Request timed out                                                                                                                                                                                                                                                                                             |
        | 413         | No                                        | Target content exceeds the maximum supported size (20 MB)                                                                                                                                                                                                                                                     |
        | 415         | No                                        | Unsupported content type                                                                                                                                                                                                                                                                                      |
        | 429         | No                                        | Per-minute rate limit exceeded; honor Retry-After                                                                                                                                                                                                                                                             |
        | 500         | No                                        | Internal error                                                                                                                                                                                                                                                                                                |

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before conversion to Markdown. Applied after
              includeSelectors. Exclusion takes precedence: an element matching both is
              removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_html: When true, the response also includes an `html` field with the page HTML the
              Markdown was converted from — the same body the Scrape HTML endpoint returns for
              the equivalent request.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before conversion to Markdown. When omitted, the entire
              document is kept. Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              converting to Markdown. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_html": include_html,
                        "include_images": include_images,
                        "include_links": include_links,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
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
        headers: Dict[str, str] | Omit = omit,
        max_links: int | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """Crawl an entire website's sitemap and return all discovered page URLs.

        Pass
        `search` to have the crawled sitemap filtered down to the pages about a phrase
        (for example `pricing and plans` or `api authentication docs`), most relevant
        first — a searched crawl scans the whole sitemap and costs 2 credits instead
        of 1.

        Args:
          domain: Domain to build a sitemap for

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          search: Optional search phrase. When provided, the crawled sitemap is filtered to the
              pages whose URLs are about that phrase, most relevant first, and the request
              costs 2 credits instead of 1.

          sitemap_url: Optional explicit sitemap URL. When provided, exactly this sitemap is crawled
              instead of discovering the domain's sitemaps.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "headers": headers,
                        "max_links": max_links,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                        "zdr": zdr,
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

    async def extract(
        self,
        *,
        schema: Dict[str, object],
        url: str,
        fact_check: bool | Omit = omit,
        follow_subdomains: bool | Omit = omit,
        include_frames: bool | Omit = omit,
        instructions: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_depth: int | Omit = omit,
        max_pages: int | Omit = omit,
        pdf: web_extract_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        stop_after_ms: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebExtractResponse:
        """
        Crawl a website, use the provided JSON Schema and instructions to prioritize
        relevant internal links, and extract structured data from the selected pages.

        Args:
          schema: JSON Schema for the returned data object. TypeScript Zod users can pass a JSON
              Schema generated from a Zod object; Python users can pass the equivalent JSON
              Schema object.

          url: The starting website URL to crawl and extract from. Must include http:// or
              https://.

          fact_check: When true, every returned value must be grounded in facts stated on the page;
              fields that cannot be supported by the page are returned as null/empty. When
              false (default), the model may make reasonable inferences and derivations from
              the page content (e.g. ideal customer, competitor analysis, recommendations)
              while keeping verifiable specifics (names, quotes, URLs, dates, metrics)
              faithful to the source.

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain.

          include_frames: When true, iframe contents are included in Markdown before extraction.

          instructions: Optional extraction guidance, such as which facts to prioritize or how to
              interpret fields in the schema.

          max_age_ms: Return cached scrape results if a prior scrape for the same parameters is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms).

          max_depth: Optional maximum link depth from the starting URL (0 = only the starting page).
              If omitted, there is no crawl depth limit.

          max_pages: Maximum number of pages to analyze for extraction. Hard cap: 50. Defaults to 5.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting each crawled page. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          stop_after_ms: Soft time budget for the crawl in milliseconds. Min: 10000 (10s). Max: 110000
              (110s). Default: 80000 (80s).

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          wait_for_ms: Optional browser wait time in milliseconds after initial page load for each
              crawled page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/web/extract",
            body=await async_maybe_transform(
                {
                    "schema": schema,
                    "url": url,
                    "fact_check": fact_check,
                    "follow_subdomains": follow_subdomains,
                    "include_frames": include_frames,
                    "instructions": instructions,
                    "max_age_ms": max_age_ms,
                    "max_depth": max_depth,
                    "max_pages": max_pages,
                    "pdf": pdf,
                    "settle_animations": settle_animations,
                    "stop_after_ms": stop_after_ms,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                    "wait_for_ms": wait_for_ms,
                },
                web_extract_params.WebExtractParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=WebExtractResponse,
        )

    async def extract_competitors(
        self,
        *,
        domain: str,
        num_competitors: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
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

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                        "timeout_ms": timeout_ms,
                    },
                    web_extract_competitors_params.WebExtractCompetitorsParams,
                ),
            ),
            cast_to=WebExtractCompetitorsResponse,
        )

    async def extract_fonts(
        self,
        *,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        color_scheme: Literal["light", "dark"] | Omit = omit,
        direct_url: str | Omit = omit,
        domain: str | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
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
          color_scheme: Optional browser color scheme to emulate for websites that respond to
              prefers-color-scheme. This value is part of the styleguide cache key.

          direct_url: A specific URL to fetch the styleguide from directly, bypassing domain
              resolution (e.g., 'https://example.com/design-system'). When provided, the
              styleguide is extracted from this exact URL. You must provide either 'domain' or
              'directUrl', but not both.

          domain: Domain name to extract styleguide from (e.g., 'example.com', 'google.com'). The
              domain will be automatically normalized and validated. You must provide either
              'domain' or 'directUrl', but not both.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
              are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
              year.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "color_scheme": color_scheme,
                        "direct_url": direct_url,
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        max_age_ms: Optional[int] | Omit = omit,
        page: Literal["login", "signup", "blog", "careers", "pricing", "terms", "privacy", "contact"] | Omit = omit,
        scroll_offset: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
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

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

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

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          viewport: Optional browser viewport dimensions for the screenshot. Defaults to 1920x1080.

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before taking
              the screenshot. Min: 0. Max: 30000 (30 seconds). Defaults to 3000 ms when
              omitted.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "max_age_ms": max_age_ms,
                        "page": page,
                        "scroll_offset": scroll_offset,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
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
        include_domains: SequenceNotStr[str] | Omit = omit,
        markdown_options: web_search_params.MarkdownOptions | Omit = omit,
        num_results: int | Omit = omit,
        query_fanout: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebSearchResponse:
        """
        Search the web and optionally scrape each result to Markdown in one round-trip.

        Args:
          query: Search query. Accepts natural language as well as Google-style search operators
              such as `site:`, `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.

          country: Two-letter ISO 3166-1 alpha-2 country code to localize results to a specific
              country (maps to Google's `gl` parameter). Example: "us", "gb", "de".

          exclude_domains: Blocklist — drop results from these domains. Example: ["pinterest.com",
              "reddit.com"].

          freshness: Restrict results to content published within this window.

          include_domains: Allowlist — only return results from these domains. Example: ["arxiv.org",
              "github.com"].

          markdown_options: Inline Markdown scraping for each result. Set `enabled: true` to activate.

          num_results: Number of results to request and return (10–100). Defaults to 10.

          query_fanout: Expand the query into multiple parallel variants for broader recall.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

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
                    "include_domains": include_domains,
                    "markdown_options": markdown_options,
                    "num_results": num_results,
                    "query_fanout": query_fanout,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
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
        timeout_ms: int | Omit = omit,
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
        """
        Performs a crawl starting from a given URL, extracts page content as Markdown,
        and returns results for all crawled pages.

        Args:
          url: The starting URL for the crawl (must include http:// or https:// protocol)

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before each crawled page is converted to Markdown.
              Applied after includeSelectors. Exclusion takes precedence: an element matching
              both is removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          follow_subdomains: When true, follow links on subdomains of the starting URL's domain (e.g.
              docs.example.com when starting from example.com). www and apex are always
              treated as equivalent.

          include_frames: When true, the contents of iframes are rendered to Markdown for each crawled
              page.

          include_images: Include image references in the Markdown output

          include_links: Preserve hyperlinks in the Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before each crawled page is converted to Markdown. When
              omitted, the entire document is kept. Examples: "article.main", "#content",
              "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_depth: Maximum link depth from the starting URL (0 = only the starting page)

          max_pages: Maximum number of pages to crawl. Hard cap: 500.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting each crawled page. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Truncate base64-encoded image data in the Markdown output

          stop_after_ms: Soft time budget for the crawl in milliseconds. After each scrape, the crawler
              checks the elapsed time and, if exceeded, returns the pages collected so far
              instead of continuing. Min: 10000 (10s). Max: 110000 (110s). Default: 80000
              (80s).

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Regex pattern. Only URLs matching this pattern will be followed and scraped. An
              automatic prefix scope in the form ^<starting URL> follows a redirect of the
              starting page.

          use_main_content_only: Extract only the main content, stripping headers, footers, sidebars, and
              navigation

          wait_for_ms: Browser wait time in milliseconds after initial page load for each crawled page.
              Defaults to 3500 (3.5 seconds). Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                    "timeout_ms": timeout_ms,
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

    async def web_scrape_html(
        self,
        *,
        url: str,
        actions: Optional[Iterable[web_web_scrape_html_params.Action]] | Omit = omit,
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
        headers: Dict[str, str] | Omit = omit,
        include_frames: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: web_web_scrape_html_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeHTMLResponse:
        """Scrapes the given URL and returns the raw HTML content of the page.

        The base
        request costs 1 credit; requests with browser actions cost 2 credits.

        Args:
          url: Full URL to scrape (must include http:// or https:// protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove from the result. Applied after includeSelectors.
              Exclusion takes precedence: an element matching both is removed. Examples:
              "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, iframes are rendered inline into the returned HTML.

          include_selectors: CSS selectors. When provided, only matching subtrees (and their descendants) are
              kept and everything else is dropped. When omitted, the entire document is kept.
              Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              extracting HTML. Defaults to false. This adds a bit of latency in exchange for
              more stable output on animated pages.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: When true, return only the page's main content in the HTML response, excluding
              headers, footers, sidebars, and navigation when detectable.

          wait_for_ms:
              Optional browser wait time in milliseconds after initial page load. Min: 0. Max:
              30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
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
        actions: Optional[Iterable[web_web_scrape_images_params.Action]] | Omit = omit,
        dedupe: bool | Omit = omit,
        enrichment: Optional[web_web_scrape_images_params.Enrichment] | Omit = omit,
        headers: Dict[str, str] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
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
        embeds. The base request costs 1 credit, or 2 credits with browser actions. When
        enrichment is enabled, the entire call costs 5 credits, including requests that
        also use actions.

        Args:
          url: Page URL to inspect. Must include http:// or https://.

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          dedupe: When true, visually duplicate images are removed: every image is loaded and
              perceptually hashed, and only the highest-resolution copy of each duplicate
              group is kept. Images that cannot be downloaded or hashed are kept. Default:
              false.

          enrichment: Optional per-image processing, sent as deep-object query params such as
              enrichment[resolution]=true.

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_age_ms: Reuse a cached result this many milliseconds old or newer. Default: 86400000 (1
              day). Set to 0 to bypass cache. Maximum: 2592000000 (30 days).

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

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
                        "actions": actions,
                        "dedupe": dedupe,
                        "enrichment": enrichment,
                        "headers": headers,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
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
        actions: Optional[Iterable[web_web_scrape_md_params.Action]] | Omit = omit,
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
        headers: Dict[str, str] | Omit = omit,
        include_frames: bool | Omit = omit,
        include_html: bool | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        include_selectors: Optional[SequenceNotStr[str]] | Omit = omit,
        max_age_ms: Optional[int] | Omit = omit,
        pdf: web_web_scrape_md_params.Pdf | Omit = omit,
        settle_animations: bool | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        wait_for_ms: Optional[int] | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeMdResponse:
        """Scrapes the given URL into LLM usable Markdown.

        Inspect key_metadata on JSON
        responses from a recognized API key; use error_code to distinguish stable
        failure categories.

        ### YouTube

        YouTube URLs return the video or channel itself rather than the surrounding
        player and navigation chrome. A URL addressing a single video (`/watch`,
        `youtu.be`, `/shorts`, `/embed`, `/live`) returns its title, channel, duration,
        view count, keywords, full description, and the transcript when the video has
        captions that can be retrieved; videos without captions return everything except
        the transcript. A channel URL (`/channel/UC…`, `/@handle`, `/c/…`, `/user/…`)
        returns its name, handle, subscriber count, video count, and full description.
        When `includeImages=true`, video responses also include the thumbnail and
        channel responses include the avatar. Costs the same as any other scrape.

        ### Billing & errors

        | HTTP status | Billed?                                   | Meaning                                                                                                                                                                                                                                                                                                       |
        | ----------- | ----------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
        | 200         | Yes — 1 credit, or 2 credits with actions | Successful scrape, including a zero-length result when includeSelectors matched nothing                                                                                                                                                                                                                       |
        | 400         | No                                        | Invalid input, skipped PDF, or the page could not be scraped. error_code WEBSITE_BLOCKED specifically means the site answered with an anti-bot challenge, CAPTCHA wall, or login shell instead of the page (even when the site returned HTTP 200) — retrying later or from another country sometimes succeeds |
        | 401 / 403   | No                                        | Invalid/disabled key, insufficient permissions, or credits exhausted; inspect error_code                                                                                                                                                                                                                      |
        | 404         | No                                        | Target page returned or fingerprinted as not found                                                                                                                                                                                                                                                            |
        | 408         | No                                        | Request timed out                                                                                                                                                                                                                                                                                             |
        | 413         | No                                        | Target content exceeds the maximum supported size (20 MB)                                                                                                                                                                                                                                                     |
        | 415         | No                                        | Unsupported content type                                                                                                                                                                                                                                                                                      |
        | 429         | No                                        | Per-minute rate limit exceeded; honor Retry-After                                                                                                                                                                                                                                                             |
        | 500         | No                                        | Internal error                                                                                                                                                                                                                                                                                                |

        Args:
          url: Full URL to scrape into LLM usable Markdown (must include http:// or https://
              protocol)

          actions: Optional browser actions executed in array order after the page loads and before
              content is captured. Requires a paid plan. Send a JSON array in the query
              parameter. Maximum: 5 actions.

          country: Fetch the target page through a residential proxy in this country (ISO 3166-1
              alpha-2).

          exclude_selectors: CSS selectors to remove before conversion to Markdown. Applied after
              includeSelectors. Exclusion takes precedence: an element matching both is
              removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          include_frames: When true, the contents of iframes are rendered to Markdown.

          include_html: When true, the response also includes an `html` field with the page HTML the
              Markdown was converted from — the same body the Scrape HTML endpoint returns for
              the equivalent request.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          include_selectors: CSS selectors. When provided, only matching HTML subtrees (and their
              descendants) are kept before conversion to Markdown. When omitted, the entire
              document is kept. Examples: "article.main", "#content", "[role=main]".

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          pdf: PDF parsing controls. Use start/end to limit text extraction and embedded-image
              detection/OCR to an inclusive 1-based page range.

          settle_animations: When true, waits briefly for CSS and transition animations to settle before
              converting to Markdown. Defaults to false. This adds a bit of latency in
              exchange for more stable output on animated pages.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          use_main_content_only: Extract only the main content of the page, excluding headers, footers, sidebars,
              and navigation

          wait_for_ms: Optional browser wait time in milliseconds after initial page load before
              converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "actions": actions,
                        "country": country,
                        "exclude_selectors": exclude_selectors,
                        "headers": headers,
                        "include_frames": include_frames,
                        "include_html": include_html,
                        "include_images": include_images,
                        "include_links": include_links,
                        "include_selectors": include_selectors,
                        "max_age_ms": max_age_ms,
                        "pdf": pdf,
                        "settle_animations": settle_animations,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "use_main_content_only": use_main_content_only,
                        "wait_for_ms": wait_for_ms,
                        "zdr": zdr,
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
        headers: Dict[str, str] | Omit = omit,
        max_links: int | Omit = omit,
        search: str | Omit = omit,
        sitemap_url: str | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        url_regex: str | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> WebWebScrapeSitemapResponse:
        """Crawl an entire website's sitemap and return all discovered page URLs.

        Pass
        `search` to have the crawled sitemap filtered down to the pages about a phrase
        (for example `pricing and plans` or `api authentication docs`), most relevant
        first — a searched crawl scans the whole sitemap and costs 2 credits instead
        of 1.

        Args:
          domain: Domain to build a sitemap for

          headers: Optional outbound HTTP headers forwarded only to the target URL, sent as
              deep-object query params such as headers[X-Custom]=value. When provided, caching
              is bypassed: the result is neither read from nor written to cache.

          max_links: Maximum number of links to return from the sitemap crawl. Defaults to 10,000.
              Minimum is 1, maximum is 100,000.

          search: Optional search phrase. When provided, the crawled sitemap is filtered to the
              pages whose URLs are about that phrase, most relevant first, and the request
              costs 2 credits instead of 1.

          sitemap_url: Optional explicit sitemap URL. When provided, exactly this sitemap is crawled
              instead of discovering the domain's sitemaps.

          tags: Optional comma-separated caller-defined tags for tracking this request. Tags are
              recorded on the request's usage log and can be used to filter usage on the
              dashboard usage page. Up to 20 tags, each 1-50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          url_regex: Optional RE2-compatible regex pattern. Only URLs matching this pattern are
              returned and counted against maxLinks.

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

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
                        "headers": headers,
                        "max_links": max_links,
                        "search": search,
                        "sitemap_url": sitemap_url,
                        "tags": tags,
                        "timeout_ms": timeout_ms,
                        "url_regex": url_regex,
                        "zdr": zdr,
                    },
                    web_web_scrape_sitemap_params.WebWebScrapeSitemapParams,
                ),
            ),
            cast_to=WebWebScrapeSitemapResponse,
        )


class WebResourceWithRawResponse:
    def __init__(self, web: WebResource) -> None:
        self._web = web

        self.extract = to_raw_response_wrapper(
            web.extract,
        )
        self.extract_competitors = to_raw_response_wrapper(
            web.extract_competitors,
        )
        self.extract_fonts = to_raw_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = to_raw_response_wrapper(
            web.extract_styleguide,
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

        self.extract = async_to_raw_response_wrapper(
            web.extract,
        )
        self.extract_competitors = async_to_raw_response_wrapper(
            web.extract_competitors,
        )
        self.extract_fonts = async_to_raw_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = async_to_raw_response_wrapper(
            web.extract_styleguide,
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

        self.extract = to_streamed_response_wrapper(
            web.extract,
        )
        self.extract_competitors = to_streamed_response_wrapper(
            web.extract_competitors,
        )
        self.extract_fonts = to_streamed_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = to_streamed_response_wrapper(
            web.extract_styleguide,
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

        self.extract = async_to_streamed_response_wrapper(
            web.extract,
        )
        self.extract_competitors = async_to_streamed_response_wrapper(
            web.extract_competitors,
        )
        self.extract_fonts = async_to_streamed_response_wrapper(
            web.extract_fonts,
        )
        self.extract_styleguide = async_to_streamed_response_wrapper(
            web.extract_styleguide,
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
