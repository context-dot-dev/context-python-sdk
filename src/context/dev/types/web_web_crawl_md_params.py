# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove matching elements after inclusions. Exclusions take precedence."""

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
    """Keep matching HTML subtrees before converting each page to Markdown."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds. Defaults to 1 day; `0` fetches fresh."""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth from the starting URL (0 = only the starting page)"""

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum pages to crawl."""

    pdf: Pdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS animations and transitions to settle before reading each
    page.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate base64-encoded image data in the Markdown output"""

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft crawl deadline in milliseconds.

    Returns pages collected before the next deadline check.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    url_regex: Annotated[str, PropertyInfo(alias="urlRegex")]
    """Regex pattern.

    Only URLs matching this pattern will be followed and scraped. An automatic
    prefix scope in the form ^<starting URL> follows a redirect of the starting
    page.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content, stripping headers, footers, sidebars, and
    navigation
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """Browser wait time in milliseconds after initial page load for each crawled page.

    Defaults to 3500 (3.5 seconds). Min: 0. Max: 30000 (30 seconds).
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Pdf(TypedDict, total=False):
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    ocr: bool
    """Read scanned PDF pages with OCR; preserve pages that already contain text."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF pages are fetched and parsed.

    When false, PDF pages are skipped entirely (not included in results and not
    counted as failures).
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    """
