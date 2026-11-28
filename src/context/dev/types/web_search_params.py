# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
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

    Accepts natural language and search operators such as `site:`, `-site:`,
    `inurl:`, `intitle:`, quoted phrases, and `OR`.
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
    Localize results to this country, as an ISO 3166-1 alpha-2 code such as `us` or
    `de`.
    """

    description_max_characters: Annotated[Optional[int], PropertyInfo(alias="descriptionMaxCharacters")]
    """Maximum length of each result's `description`, in characters."""

    exclude_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeDomains")]
    """Leave out results from these domains, such as `pinterest.com`."""

    freshness: Literal["last_24_hours", "last_week", "last_month", "last_year"]
    """Restrict results to content published within this window."""

    highlights_options: Annotated[Optional[HighlightsOptions], PropertyInfo(alias="highlightsOptions")]
    """Return passages from each result page that are relevant to the query.

    Pages are read with the `markdownOptions` settings.
    """

    include_domains: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeDomains")]
    """Only return results from these domains, such as `arxiv.org`."""

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
    """
    Languages to return results in, as BCP 47 codes such as `en` or `de`, or `all`
    for any language.
    """

    markdown_options: Annotated[Optional[MarkdownOptions], PropertyInfo(alias="markdownOptions")]
    """Scrape each result page to Markdown. Set `enabled` to `true` to turn it on."""

    num_results: Annotated[int, PropertyInfo(alias="numResults")]
    """Number of results to return."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class HighlightsOptions(TypedDict, total=False):
    """Return passages from each result page that are relevant to the query.

    Pages are read with the `markdownOptions` settings.
    """

    enabled: bool
    """Return relevant passages for each result. Adds 1 credit per 10 results."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of passages per result, in characters."""


class MarkdownOptionsPdf(TypedDict, total=False):
    """Whether to parse PDFs and which pages to read."""

    end: int
    """Last page to parse. Defaults to the last page. Must be at least `start`."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF results. When `false`, PDF results fail with `WEBSITE_ACCESS_ERROR`."""

    start: int
    """First page to parse, starting at 1."""


class MarkdownOptionsTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial. `return-partial` requires at least 5000 ms. On `POST /web/scrape`, an
    output that is not ready in time fails with `REQUEST_TIMEOUT` inside a 200
    response under either behavior; 408 means the whole request could not respond by
    the deadline.
    """


class MarkdownOptions(TypedDict, total=False):
    """Scrape each result page to Markdown. Set `enabled` to `true` to turn it on."""

    enabled: bool
    """Scrape each result page to Markdown.

    Adds 1 credit per result that returns Markdown.
    """

    include_frames: Annotated[Union[bool, Literal["auto"]], PropertyInfo(alias="includeFrames")]
    """Which iframe contents to include in the Markdown.

    `auto` inlines only iframes that hold page content, such as same-site documents,
    framesets, job boards, forms, and embedded documents, and skips ads and widgets.
    `true` inlines every iframe; `false` inlines none.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown."""

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached result, in milliseconds.

    `0` always fetches fresh. Defaults to 180 days (15552000000 ms) with Markdown,
    or 365 days (31536000000 ms) with highlights only.
    """

    pdf: MarkdownOptionsPdf
    """Whether to parse PDFs and which pages to read."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data."""

    timeout_opts: Annotated[MarkdownOptionsTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Keep only the main content, without navigation, headers, footers, or sidebars."""

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """Time to wait after each result page loads before reading it, in milliseconds.

    `0` waits 500 ms. Helps with JavaScript-heavy pages.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """
