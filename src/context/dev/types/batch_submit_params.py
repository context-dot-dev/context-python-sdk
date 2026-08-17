# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "BatchSubmitParams",
    "Input",
    "InputScrape",
    "InputScrapeData",
    "InputScrapeDataMarkdown",
    "InputScrapeDataMarkdownURL",
    "InputScrapeDataMarkdownOptions",
    "InputScrapeDataMarkdownOptionsPdf",
    "InputScrapeDataHTML",
    "InputScrapeDataHtmlurL",
    "InputScrapeDataHTMLOptions",
    "InputScrapeDataHTMLOptionsPdf",
    "InputCrawl",
    "InputCrawlData",
    "InputCrawlDataMarkdown",
    "InputCrawlDataMarkdownSource",
    "InputCrawlDataMarkdownSourceStartURL",
    "InputCrawlDataMarkdownSourceStartURLControls",
    "InputCrawlDataMarkdownSourceSitemap",
    "InputCrawlDataMarkdownSourceSitemapControls",
    "InputCrawlDataMarkdownOptions",
    "InputCrawlDataMarkdownOptionsPdf",
    "InputCrawlDataHTML",
    "InputCrawlDataHTMLSource",
    "InputCrawlDataHTMLSourceStartURL",
    "InputCrawlDataHTMLSourceStartURLControls",
    "InputCrawlDataHTMLSourceSitemap",
    "InputCrawlDataHTMLSourceSitemapControls",
    "InputCrawlDataHTMLOptions",
    "InputCrawlDataHTMLOptionsPdf",
]


class BatchSubmitParams(TypedDict, total=False):
    input: Required[Input]
    """Choose a URL list or a site crawl."""

    tags: SequenceNotStr[str]
    """Tags stored on the batch. Filter the batch list by them later."""

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """URL notified when the batch finishes."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Any string unique to this submission.

    Retries with the same key return the original batch.
    """


class InputScrapeDataMarkdownURL(TypedDict, total=False):
    """A page to scrape, with optional data for matching results."""

    url: Required[str]
    """Page URL to scrape."""

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """Your ID for this page, returned with its result.

    The same URL can use different IDs.
    """

    meta: Dict[str, object]
    """Custom JSON returned unchanged with this page result."""


class InputScrapeDataMarkdownOptionsPdf(TypedDict, total=False):
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
    When true, OCR the selected PDF pages that have no usable text layer (scans),
    replacing each recovered page's text with the OCR result while pages with a real
    text layer keep it. Billed at 1 credit per page OCR actually recovered, on top
    of the base request cost. When false, no OCR runs.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 PDF_SKIPPED is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """


class InputScrapeDataMarkdownOptions(TypedDict, total=False):
    """Options for Markdown output."""

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
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_html: Annotated[bool, PropertyInfo(alias="includeHTML")]
    """
    Also include each page's HTML in its result record, as an `html` field alongside
    the Markdown.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Include links in the Markdown."""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only the subtrees matching these CSS selectors.

    Filtered pages are always fetched fresh, ignoring `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: InputScrapeDataMarkdownOptionsPdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS and transition animations to settle before extraction, on
    pages that render in a browser.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputScrapeDataMarkdown(TypedDict, total=False):
    """Scrape the listed pages as Markdown."""

    format: Required[Literal["markdown"]]
    """Return page content as Markdown."""

    urls: Required[Iterable[InputScrapeDataMarkdownURL]]
    """Pages to scrape. Maximum 25000."""

    options: InputScrapeDataMarkdownOptions
    """Options for Markdown output."""


class InputScrapeDataHtmlurL(TypedDict, total=False):
    """A page to scrape, with optional data for matching results."""

    url: Required[str]
    """Page URL to scrape."""

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """Your ID for this page, returned with its result.

    The same URL can use different IDs.
    """

    meta: Dict[str, object]
    """Custom JSON returned unchanged with this page result."""


class InputScrapeDataHTMLOptionsPdf(TypedDict, total=False):
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
    When true, OCR the selected PDF pages that have no usable text layer (scans),
    replacing each recovered page's text with the OCR result while pages with a real
    text layer keep it. Billed at 1 credit per page OCR actually recovered, on top
    of the base request cost. When false, no OCR runs.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 PDF_SKIPPED is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """


class InputScrapeDataHTMLOptions(TypedDict, total=False):
    """Options for HTML output."""

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
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only the subtrees matching these CSS selectors.

    Filtered pages are always fetched fresh, ignoring `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: InputScrapeDataHTMLOptionsPdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS and transition animations to settle before extraction, on
    pages that render in a browser.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputScrapeDataHTML(TypedDict, total=False):
    """Scrape the listed pages as HTML."""

    format: Required[Literal["html"]]
    """Return page content as HTML."""

    urls: Required[Iterable[InputScrapeDataHtmlurL]]
    """Pages to scrape. Maximum 25000."""

    options: InputScrapeDataHTMLOptions
    """Options for HTML output."""


InputScrapeData: TypeAlias = Union[InputScrapeDataMarkdown, InputScrapeDataHTML]


class InputScrape(TypedDict, total=False):
    """Scrape up to 25K URLs in one batch."""

    data: Required[InputScrapeData]
    """Pages to scrape and their output format."""

    mode: Required[Literal["scrape"]]
    """Scrape the pages in `data.urls`."""


class InputCrawlDataMarkdownSourceStartURLControls(TypedDict, total=False):
    """Limits and filters for page discovery."""

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 25000."""

    regex: str
    """RE2 pattern for URLs to include. The `start_url` itself is always included."""


class InputCrawlDataMarkdownSourceStartURL(TypedDict, total=False):
    """Discover pages by following links from one URL."""

    type: Required[Literal["start_url"]]
    """Start from one page."""

    url: Required[str]
    """Page where crawling begins. A URL without a scheme is read as https://."""

    controls: InputCrawlDataMarkdownSourceStartURLControls
    """Limits and filters for page discovery."""


class InputCrawlDataMarkdownSourceSitemapControls(TypedDict, total=False):
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so there is no crawl depth here.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 25000."""

    regex: str
    """RE2 pattern; only sitemap URLs matching it are scraped."""


class InputCrawlDataMarkdownSourceSitemap(TypedDict, total=False):
    """Scrape the pages listed in a domain's sitemap.

    Links on those pages are not followed.
    """

    domain: Required[str]
    """Domain whose sitemap lists the pages to scrape.

    A full URL is reduced to its domain.
    """

    type: Required[Literal["sitemap"]]
    """Scrape the URLs in the domain's sitemap."""

    controls: InputCrawlDataMarkdownSourceSitemapControls
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so
    there is no crawl depth here.
    """


InputCrawlDataMarkdownSource: TypeAlias = Union[
    InputCrawlDataMarkdownSourceStartURL, InputCrawlDataMarkdownSourceSitemap
]


class InputCrawlDataMarkdownOptionsPdf(TypedDict, total=False):
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
    When true, OCR the selected PDF pages that have no usable text layer (scans),
    replacing each recovered page's text with the OCR result while pages with a real
    text layer keep it. Billed at 1 credit per page OCR actually recovered, on top
    of the base request cost. When false, no OCR runs.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 PDF_SKIPPED is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """


class InputCrawlDataMarkdownOptions(TypedDict, total=False):
    """Options for Markdown output."""

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
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_html: Annotated[bool, PropertyInfo(alias="includeHTML")]
    """
    Also include each page's HTML in its result record, as an `html` field alongside
    the Markdown.
    """

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Include links in the Markdown."""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only the subtrees matching these CSS selectors.

    Filtered pages are always fetched fresh, ignoring `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: InputCrawlDataMarkdownOptionsPdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS and transition animations to settle before extraction, on
    pages that render in a browser.
    """

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputCrawlDataMarkdown(TypedDict, total=False):
    """Crawl pages and return Markdown."""

    format: Required[Literal["markdown"]]
    """Return page content as Markdown."""

    source: Required[InputCrawlDataMarkdownSource]
    """How to find pages to crawl."""

    options: InputCrawlDataMarkdownOptions
    """Options for Markdown output."""


class InputCrawlDataHTMLSourceStartURLControls(TypedDict, total=False):
    """Limits and filters for page discovery."""

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 25000."""

    regex: str
    """RE2 pattern for URLs to include. The `start_url` itself is always included."""


class InputCrawlDataHTMLSourceStartURL(TypedDict, total=False):
    """Discover pages by following links from one URL."""

    type: Required[Literal["start_url"]]
    """Start from one page."""

    url: Required[str]
    """Page where crawling begins. A URL without a scheme is read as https://."""

    controls: InputCrawlDataHTMLSourceStartURLControls
    """Limits and filters for page discovery."""


class InputCrawlDataHTMLSourceSitemapControls(TypedDict, total=False):
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so there is no crawl depth here.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 25000."""

    regex: str
    """RE2 pattern; only sitemap URLs matching it are scraped."""


class InputCrawlDataHTMLSourceSitemap(TypedDict, total=False):
    """Scrape the pages listed in a domain's sitemap.

    Links on those pages are not followed.
    """

    domain: Required[str]
    """Domain whose sitemap lists the pages to scrape.

    A full URL is reduced to its domain.
    """

    type: Required[Literal["sitemap"]]
    """Scrape the URLs in the domain's sitemap."""

    controls: InputCrawlDataHTMLSourceSitemapControls
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so
    there is no crawl depth here.
    """


InputCrawlDataHTMLSource: TypeAlias = Union[InputCrawlDataHTMLSourceStartURL, InputCrawlDataHTMLSourceSitemap]


class InputCrawlDataHTMLOptionsPdf(TypedDict, total=False):
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
    When true, OCR the selected PDF pages that have no usable text layer (scans),
    replacing each recovered page's text with the OCR result while pages with a real
    text layer keep it. Billed at 1 credit per page OCR actually recovered, on top
    of the base request cost. When false, no OCR runs.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF URLs are fetched and parsed.

    When false, PDF URLs are skipped and a 400 PDF_SKIPPED is returned.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """


class InputCrawlDataHTMLOptions(TypedDict, total=False):
    """Options for HTML output."""

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
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only the subtrees matching these CSS selectors.

    Filtered pages are always fetched fresh, ignoring `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 1 day (86400000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    pdf: InputCrawlDataHTMLOptionsPdf
    """PDF parsing controls.

    Use start/end to limit text extraction and embedded-image detection/OCR to an
    inclusive 1-based page range.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    Wait briefly for CSS and transition animations to settle before extraction, on
    pages that render in a browser.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputCrawlDataHTML(TypedDict, total=False):
    """Crawl pages and return HTML."""

    format: Required[Literal["html"]]
    """Return page content as HTML."""

    source: Required[InputCrawlDataHTMLSource]
    """How to find pages to crawl."""

    options: InputCrawlDataHTMLOptions
    """Options for HTML output."""


InputCrawlData: TypeAlias = Union[InputCrawlDataMarkdown, InputCrawlDataHTML]


class InputCrawl(TypedDict, total=False):
    """Crawl pages starting from a URL or from a domain's sitemap."""

    data: Required[InputCrawlData]
    """Crawl source and output format."""

    mode: Required[Literal["crawl"]]
    """Discover and scrape pages from `data.source`."""


Input: TypeAlias = Union[InputScrape, InputCrawl]
