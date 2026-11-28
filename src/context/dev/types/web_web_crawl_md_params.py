# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebCrawlMdParams", "Pdf", "TimeoutOpts"]


class WebWebCrawlMdParams(TypedDict, total=False):
    url: Required[str]
    """Start URL, including `http://` or `https://`."""

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
    """Country to fetch from, as an ISO 3166-1 alpha-2 code."""

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    exclude_url_regex: Annotated[str, PropertyInfo(alias="excludeUrlRegex")]
    """Never follow or scrape URLs matching this regex, even when they match
    `urlRegex`.

    The start URL is always scraped.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """
    Follow links to subdomains of the start URL's domain, such as `docs.example.com`
    from `example.com`. `www` and the apex domain always count as the same site.
    """

    include_frames: Annotated[Union[bool, Literal["auto"]], PropertyInfo(alias="includeFrames")]
    """Which iframe contents to include in each page's Markdown.

    `auto` inlines only iframes that hold page content, such as same-site documents,
    framesets, job boards, forms, and embedded documents, and skips ads and widgets.
    `true` inlines every iframe; `false` inlines none.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown (`html-conversion` only)."""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached result, in milliseconds.

    `0` always fetches fresh. Defaults to 1 day (86400000 ms). Maximum: 30 days
    (2592000000 ms).
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth from the start URL.

    `0` crawls only the start URL. Omit for no depth limit.
    """

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to crawl."""

    pdf: Pdf
    """Whether to parse PDFs and which pages to read."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS animations and transitions to settle before reading each
    page.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data (`html-conversion` only)."""

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft time budget for the crawl, in milliseconds.

    When it runs out, the crawl returns the pages collected so far. Larger values
    are capped at 110 seconds.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Only follow and scrape URLs matching this regex.

    A prefix pattern of the form `^<start URL>` also follows a redirect of the start
    page.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Keep only the main content, without navigation, headers, footers, or sidebars."""

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """Time to wait after each page loads before reading it, in milliseconds.

    `0` waits 500 ms. `timeoutOpts.milliseconds` must be at least `waitForMs` plus
    10000 ms, or the request fails with `TIMEOUT_TOO_SHORT_FOR_WAIT`.
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Pdf(TypedDict, total=False):
    """Whether to parse PDFs and which pages to read."""

    end: int
    """Last page to parse. Defaults to the last page. Must be at least `start`."""

    ocr: bool
    """Read scanned PDF pages with OCR. Pages that already have text are kept as is."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF pages.

    When `false`, PDFs are left out of the results and not counted as failures.
    """

    start: int
    """First page to parse, starting at 1."""


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """
