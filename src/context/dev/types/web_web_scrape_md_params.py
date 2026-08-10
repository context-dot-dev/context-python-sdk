# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebWebScrapeMdParams", "Action", "ActionWebScrapeWaitAction", "ActionWebScrapePerformAction", "Pdf"]


class WebWebScrapeMdParams(TypedDict, total=False):
    url: Required[str]
    """
    Full URL to scrape into LLM usable Markdown (must include http:// or https://
    protocol)
    """

    actions: Optional[Iterable[Action]]
    """
    Optional browser actions executed in array order after the page loads and before
    content is captured. Requires a paid plan. Send a JSON array in the query
    parameter. Maximum: 5 actions.
    """

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
    Fetch the target page through a residential proxy in this country (ISO 3166-1
    alpha-2).
    """

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """CSS selectors to remove before conversion to Markdown.

    Applied after includeSelectors. Exclusion takes precedence: an element matching
    both is removed. Examples: "nav", "footer", ".ad-banner", "[aria-hidden=true]".
    """

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    include_frames: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeFrames")]
    """When true, the contents of iframes are rendered to Markdown."""

    include_html: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeHTML")]
    """
    When true, the response also includes an `html` field with the page HTML the
    Markdown was converted from — the same body the Scrape HTML endpoint returns for
    the equivalent request.
    """

    include_images: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """CSS selectors.

    When provided, only matching HTML subtrees (and their descendants) are kept
    before conversion to Markdown. When omitted, the entire document is kept.
    Examples: "article.main", "#content", "[role=main]".
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: Pdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="settleAnimations")]
    """
    When true, waits briefly for CSS and transition animations to settle before
    converting to Markdown. Defaults to false. This adds a bit of latency in
    exchange for more stable output on animated pages.
    """

    shorten_base64_images: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    use_main_content_only: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="useMainContentOnly")]
    """
    Extract only the main content of the page, excluding headers, footers, sidebars,
    and navigation
    """

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    converting the page to Markdown. Min: 0. Max: 30000 (30 seconds).
    """

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Requires zero data retention to be enabled for your
    organization (contact support@context.dev), otherwise the request fails with
    ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.
    """


class ActionWebScrapeWaitAction(TypedDict, total=False):
    """Pause for a fixed number of milliseconds before continuing to the next action."""

    do: Required[Literal["wait"]]

    time_ms: Required[Annotated[int, PropertyInfo(alias="timeMs")]]


class ActionWebScrapePerformAction(TypedDict, total=False):
    """Resolve and perform one natural-language browser action."""

    action: Required[str]

    do: Required[Literal["perform"]]


Action: TypeAlias = Union[ActionWebScrapeWaitAction, ActionWebScrapePerformAction]


class Pdf(TypedDict, total=False):
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an inclusive 1-based page range.
    """

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    ocr: Union[bool, Literal["true", "false"]]
    """
    When true, OCR the selected PDF pages that have no usable text layer (scans),
    replacing each recovered page's text with the OCR result while pages with a real
    text layer keep it. Billed at 1 credit per page OCR actually recovered, on top
    of the base request cost. When false, no OCR runs.
    """

    should_parse: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 PDF_SKIPPED is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
