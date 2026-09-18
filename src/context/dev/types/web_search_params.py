# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebSearchParams", "MarkdownOptions", "MarkdownOptionsPdf", "MarkdownOptionsTimeoutOpts", "TimeoutOpts"]


class WebSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search query.

    Accepts natural language as well as Google-style search operators such as
    `site:`, `-site:`, `inurl:`, `intitle:`, quoted phrases, and `OR`.
    """

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
    """
    Two-letter ISO 3166-1 alpha-2 country code to localize results to a specific
    country (maps to Google's `gl` parameter). Example: "us", "gb", "de".
    """

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Blocklist — drop results from these domains.

    Example: ["pinterest.com", "reddit.com"].
    """

    freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"]
    """Restrict results to content published within this window."""

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Allowlist — only return results from these domains.

    Example: ["arxiv.org", "github.com"].
    """

    markdown_options: Annotated[MarkdownOptions, PropertyInfo(alias="markdownOptions")]
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to request and return (10–100). Defaults to 10."""

    query_fanout: Annotated[bool, PropertyInfo(alias="queryFanout")]
    """Expand the query into multiple parallel variants for broader recall."""

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Asset uploads are skipped, so hosted image URLs are
    omitted. Requires zero data retention to be enabled for your organization
    (contact support@context.dev), otherwise the request fails with ZDR_NOT_ENABLED.
    Successful ZDR responses include X-Context-ZDR: true.
    """


class MarkdownOptionsPdf(TypedDict, total=False):
    """PDF handling. Use start/end to bound text extraction and OCR to a page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDF results are skipped with WEBSITE_ACCESS_ERROR."""

    start: int
    """First PDF page to parse (1-based, inclusive). Defaults to page 1."""


class MarkdownOptionsTimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail", "return-partial"]
    """What to do at the deadline.

    "fail" returns 408 REQUEST_TIMEOUT without charging credits. "return-partial"
    returns usable results collected so far; if none are available, the request
    still fails without charging credits. Partial results are not cached as complete
    results. "return-partial" requires milliseconds of at least 5000.
    """


class MarkdownOptions(TypedDict, total=False):
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    enabled: bool
    """Scrape each result to Markdown. Off by default to keep search cheap and fast."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Render iframe contents into the Markdown."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Emit image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep hyperlinks in the Markdown."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Cache TTL in ms for scraped Markdown keyed by URL + options.

    Default 1 day, max 30 days. Set to 0 to force a fresh scrape.
    """

    pdf: MarkdownOptionsPdf
    """PDF handling. Use start/end to bound text extraction and OCR to a page range."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate inline base64 image payloads to keep responses small."""

    timeout_opts: Annotated[MarkdownOptionsTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Strip nav, header, footer, and sidebar — keep only the primary article content."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """Extra wait after page load before rendering, in ms (0–30000).

    Useful for JS-heavy pages.
    """


class TimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail", "return-partial"]
    """What to do at the deadline.

    "fail" returns 408 REQUEST_TIMEOUT without charging credits. "return-partial"
    returns usable results collected so far; if none are available, the request
    still fails without charging credits. Partial results are not cached as complete
    results.
    """
