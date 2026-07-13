# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebCrawlMdParams", "Pdf"]


class WebWebCrawlMdParams(TypedDict, total=False):
    url: Required[str]
    """The starting URL for the crawl (must include http:// or https:// protocol)"""

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
    """
    Two-letter ISO 3166-1 alpha-2 country code identifying a supported Context.dev
    residential proxy exit location. Must be one of Context.dev's supported
    countries. When provided, Context.dev fetches the target page from that country.
    """

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """CSS selectors to remove before each crawled page is converted to Markdown.

    Applied after includeSelectors. Exclusion takes precedence: an element matching
    both is removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """When true, follow links on subdomains of the starting URL's domain (e.g.

    docs.example.com when starting from example.com). www and apex are always
    treated as equivalent.
    """

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """
    When true, the contents of iframes are rendered to Markdown for each crawled
    page.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in the Markdown output"""

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """CSS selectors.

    When provided, only matching HTML subtrees (and their descendants) are kept
    before each crawled page is converted to Markdown. When omitted, the entire
    document is kept. Examples: "article.main", "#content", "[role=main]".
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth from the starting URL (0 = only the starting page)"""

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to crawl. Hard cap: 500."""

    pdf: Pdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    When true, waits briefly for CSS and transition animations to settle before
    extracting each crawled page. Defaults to false. This adds a bit of latency in
    exchange for more stable output on animated pages.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate base64-encoded image data in the Markdown output"""

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft time budget for the crawl in milliseconds.

    After each scrape, the crawler checks the elapsed time and, if exceeded, returns
    the pages collected so far instead of continuing. Min: 10000 (10s). Max: 110000
    (110s). Default: 80000 (80s).
    """

    tags: SequenceNotStr[str]
    """Optional caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Regex pattern. Only URLs matching this pattern will be followed and scraped."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content, stripping headers, footers, sidebars, and
    navigation
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load for each
    crawled page. Min: 0. Max: 30000 (30 seconds).
    """


class Pdf(TypedDict, total=False):
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an inclusive 1-based page range.
    """

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    ocr: bool
    """
    When true, detect and OCR images embedded in the selected PDF pages, inserting
    recognized text at each image's position in page reading order while preserving
    the PDF text layer. This is separate from automatic scanned-PDF OCR fallback.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF pages are fetched and parsed.

    When false, PDF pages are skipped entirely (not included in results and not
    counted as failures).
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
