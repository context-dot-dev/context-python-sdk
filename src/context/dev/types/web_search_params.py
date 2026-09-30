# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebSearchParams",
    "HighlightsOptions",
    "MarkdownOptions",
    "MarkdownOptionsPdf",
    "MarkdownOptionsTimeoutOpts",
    "TimeoutOpts",
]


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

    Up to 100 domains. Example: ["pinterest.com", "reddit.com"].
    """

    freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"]
    """Restrict results to content published within this window."""

    highlights_options: Annotated[Optional[HighlightsOptions], PropertyInfo(alias="highlightsOptions")]
    """Passages from each result page that are relevant to the query.

    Pages are read with the `markdownOptions` settings.
    """

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Allowlist — only return results from these domains.

    Up to 100 domains. Example: ["arxiv.org", "github.com"].
    """

    markdown_options: Annotated[Optional[MarkdownOptions], PropertyInfo(alias="markdownOptions")]
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to request and return (10–100). Defaults to 10."""

    query_fanout: Annotated[bool, PropertyInfo(alias="queryFanout")]
    """Currently has no effect."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class HighlightsOptions(TypedDict, total=False):
    """Passages from each result page that are relevant to the query.

    Pages are read with the `markdownOptions` settings.
    """

    enabled: bool
    """Return relevant passages for each result. Adds 1 credit per 10 results."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of passages per result."""


class MarkdownOptionsPdf(TypedDict, total=False):
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDF results are skipped with WEBSITE_ACCESS_ERROR."""

    start: int
    """First 1-based PDF page to parse."""


class MarkdownOptionsTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class MarkdownOptions(TypedDict, total=False):
    """Inline Markdown scraping for each result. Set `enabled: true` to activate."""

    enabled: bool
    """Scrape each result to Markdown. Adds 1 credit per 10 results."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Render iframe contents into the Markdown."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Emit image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep hyperlinks in the Markdown."""

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds for result page content.

    Defaults to 180 days (15552000000 ms) when Markdown is requested, or 365 days
    (31536000000 ms) when only highlights are requested. Explicit values override
    either default. Maximum: 365 days. Set to 0 to force a fresh scrape.
    """

    pdf: MarkdownOptionsPdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Truncate inline base64 image payloads to keep responses small."""

    timeout_opts: Annotated[MarkdownOptionsTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Strip nav, header, footer, and sidebar — keep only the primary article content."""

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """Extra wait after page load before rendering, in ms (0–30000).

    Useful for JS-heavy pages.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    """
