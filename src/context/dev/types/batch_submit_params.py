# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .retry_config_param import RetryConfigParam

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
    "InputScrapeDataBatchUnifiedScrapeData",
    "InputScrapeDataBatchUnifiedScrapeDataFormats",
    "InputScrapeDataBatchUnifiedScrapeDataURL",
    "InputScrapeDataBatchUnifiedScrapeDataHighlightsParams",
    "InputScrapeDataBatchUnifiedScrapeDataImageParams",
    "InputScrapeDataBatchUnifiedScrapeDataJsonParams",
    "InputScrapeDataBatchUnifiedScrapeDataMarkdownParams",
    "InputScrapeDataBatchUnifiedScrapeDataParseParams",
    "InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParser",
    "InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRules",
    "InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRulesUnionMember1",
    "InputScrapeDataBatchUnifiedScrapeDataParseParamsPrebuiltParser",
    "InputScrapeDataBatchUnifiedScrapeDataProductParams",
    "InputScrapeDataBatchUnifiedScrapeDataScreenshotParams",
    "InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsArea",
    "InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaElement",
    "InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaRectangle",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParams",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsAction",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionPerform",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionScroll",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWait",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWaitFor",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsers",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsersPdf",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfile",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileExisting",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileNew",
    "InputScrapeDataBatchUnifiedScrapeDataSharedParamsViewport",
    "InputScrapeDataBatchUnifiedScrapeDataTimeoutOpts",
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
    "InputCrawlDataBatchUnifiedCrawlData",
    "InputCrawlDataBatchUnifiedCrawlDataFormats",
    "InputCrawlDataBatchUnifiedCrawlDataSource",
    "InputCrawlDataBatchUnifiedCrawlDataSourceStartURL",
    "InputCrawlDataBatchUnifiedCrawlDataSourceStartURLControls",
    "InputCrawlDataBatchUnifiedCrawlDataSourceSitemap",
    "InputCrawlDataBatchUnifiedCrawlDataSourceSitemapControls",
    "InputCrawlDataBatchUnifiedCrawlDataHighlightsParams",
    "InputCrawlDataBatchUnifiedCrawlDataImageParams",
    "InputCrawlDataBatchUnifiedCrawlDataJsonParams",
    "InputCrawlDataBatchUnifiedCrawlDataMarkdownParams",
    "InputCrawlDataBatchUnifiedCrawlDataParseParams",
    "InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParser",
    "InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRules",
    "InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRulesUnionMember1",
    "InputCrawlDataBatchUnifiedCrawlDataParseParamsPrebuiltParser",
    "InputCrawlDataBatchUnifiedCrawlDataProductParams",
    "InputCrawlDataBatchUnifiedCrawlDataScreenshotParams",
    "InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsArea",
    "InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaElement",
    "InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaRectangle",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParams",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsAction",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionPerform",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionScroll",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWait",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWaitFor",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsers",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsersPdf",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfile",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileExisting",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileNew",
    "InputCrawlDataBatchUnifiedCrawlDataSharedParamsViewport",
    "InputCrawlDataBatchUnifiedCrawlDataTimeoutOpts",
    "Webhook",
]


class BatchSubmitParams(TypedDict, total=False):
    input: Required[Input]
    """Choose a URL list or a site crawl."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply to every page. A URL must pass every policy."""

    tags: SequenceNotStr[str]
    """Tags stored on the batch. Filter the batch list by them later."""

    webhook: Webhook
    """Where to send the batch's final-status event.

    Omit `retry` for one attempt; `{}` uses the default retry schedule.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """Legacy URL notified when the batch finishes.

    Preserves one best-effort attempt. Cannot be combined with webhook.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Unique key per submission.

    Retrying with the same key and body returns the original batch; a different body
    returns `409`.
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
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    ocr: bool
    """Read scanned PDF pages with OCR; preserve pages that already have text."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDFs fail with `PDF_SKIPPED`."""

    start: int
    """First 1-based PDF page to parse."""


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
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_html: Annotated[bool, PropertyInfo(alias="includeHTML")]
    """Also return each page's HTML in `html`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Include links in the Markdown (`html-conversion` only)."""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors.

    Filtered pages ignore `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds.

    Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms). `0` fetches
    fresh.
    """

    pdf: InputScrapeDataMarkdownOptionsPdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before extracting, on browser-rendered pages."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data (`html-conversion` only)."""

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputScrapeDataMarkdown(TypedDict, total=False):
    """Scrape the listed pages as Markdown."""

    format: Required[Literal["markdown"]]
    """Return page content as Markdown."""

    urls: Required[Iterable[InputScrapeDataMarkdownURL]]
    """Pages to scrape. Maximum 100000."""

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
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    ocr: bool
    """Read scanned PDF pages with OCR; preserve pages that already have text."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDFs fail with `PDF_SKIPPED`."""

    start: int
    """First 1-based PDF page to parse."""


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
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors.

    Filtered pages ignore `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds.

    Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms). `0` fetches
    fresh.
    """

    pdf: InputScrapeDataHTMLOptionsPdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before extracting, on browser-rendered pages."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Return the main content without navigation or footers."""

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """How long to wait after initial page load, in milliseconds. `0` waits 500 ms."""


class InputScrapeDataHTML(TypedDict, total=False):
    """Scrape the listed pages as HTML."""

    format: Required[Literal["html"]]
    """Return page content as HTML."""

    urls: Required[Iterable[InputScrapeDataHtmlurL]]
    """Pages to scrape. Maximum 100000."""

    options: InputScrapeDataHTMLOptions
    """Options for HTML output."""


class InputScrapeDataBatchUnifiedScrapeDataFormats(TypedDict, total=False):
    """Outputs to return. Set at least one to `true`."""

    bytes: bool
    """The original HTTP response body."""

    highlights: bool
    """Markdown excerpts relevant to `highlightsParams.query`."""

    html: bool
    """Rendered HTML."""

    images: bool
    """Images found on the page."""

    json: bool
    """An object matching `jsonParams.schema`, extracted from the page."""

    markdown: bool
    """Page content as Markdown."""

    parse: bool
    """Fields extracted with custom rules or a prebuilt parser, returned as `parsed`."""

    product: bool
    """Product details such as name, price, and availability."""

    screenshot: bool
    """A screenshot of the page."""


class InputScrapeDataBatchUnifiedScrapeDataURL(TypedDict, total=False):
    """A page to scrape, with optional data for matching results."""

    url: Required[str]
    """Page URL to scrape."""

    item_id: Annotated[str, PropertyInfo(alias="itemId")]
    """Your ID for this page, returned with its result.

    The same URL can use different IDs.
    """

    meta: Dict[str, object]
    """Custom JSON returned unchanged with this page result."""


class InputScrapeDataBatchUnifiedScrapeDataHighlightsParams(TypedDict, total=False):
    """Requires `formats.highlights: true`; required when it is set."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of returned passages."""


class InputScrapeDataBatchUnifiedScrapeDataImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """Set `visual` to drop visual duplicates, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Extra data per image: `dimensions`, `classification`, or a hosted `file` URL."""


class InputScrapeDataBatchUnifiedScrapeDataJsonParams(TypedDict, total=False):
    """Requires `formats.json: true`; required when it is set."""

    schema: Required[Dict[str, object]]
    """JSON Schema (not an example object) for a top-level object, up to 50 KB.

    Use optional or nullable fields for missing facts.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class InputScrapeDataBatchUnifiedScrapeDataMarkdownParams(TypedDict, total=False):
    """Markdown options. Requires `formats.markdown`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include images in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown (`html-conversion` only)."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """How base64 images appear when `includeImages` is set (`html-conversion` only)."""

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """


class InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """Return text, HTML, an attribute such as `@href`, or nested field rules.

    Defaults to text.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRules: TypeAlias = Union[
    str, InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRulesUnionMember1
]


class InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParser(TypedDict, total=False):
    rules: Required[Dict[str, InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParserRules]]
    """Field names mapped to CSS selectors (`h1`, `a@href`) or rule objects.

    Max 100 fields, 5 levels.
    """

    type: Literal["custom"]
    """Extract fields using custom CSS rules.

    This is the default when type is omitted.
    """


class InputScrapeDataBatchUnifiedScrapeDataParseParamsPrebuiltParser(TypedDict, total=False):
    parser: Required[
        Literal[
            "google-maps",
            "google-maps-reviews",
            "google-play",
            "google-play-reviews",
            "app-store",
            "app-store-reviews",
            "g2-reviews",
            "instagram-profile",
            "instagram-post",
            "instagram-feed",
            "tiktok-profile",
            "tiktok-video",
            "tiktok-feed",
            "tiktok-comments",
            "tiktok-followers",
            "tiktok-following",
            "tiktok-user-search",
            "emails",
            "phone-numbers",
            "links",
        ]
    ]
    """google-maps parses Google Maps business data into data.results.

    Accepts Maps place, search, and internal data URLs. Uses a US exit and English
    labels regardless of hl or Accept-Language. google-maps-reviews returns the
    reviews of a place in data.reviews, in the same shape as the Serper reviews API
    (rating, date, isoDate, snippet, translatedSnippet, likes, user, media,
    response, link, id), plus language, guided ratings in details, and
    user.isLocalGuide; data also carries the place featureId, cid, and sort. sort
    and limit pick the order and count, and oldest is exact. It accepts Maps place,
    search, and ?cid= URLs, plus search.google.com/local/reviews URLs, so the
    google_maps_url and google_reviews_url fields of google-maps results work as
    input. An unknown place returns no reviews. google-play parses a Play Store app
    into data: details, developer contact, ratings, price, permissions, and data
    safety. google-play-reviews returns the 200 newest reviews of the app, with
    developer replies, in data.reviews. Both Play parsers accept app details URLs
    (play.google.com/store/apps/details?id=…); hl and gl set the language and
    storefront, defaulting to en and us. app-store parses an App Store app into
    data: details, developer, ratings, price, version, and screenshots.
    app-store-reviews returns up to the 500 newest reviews in data.reviews. Both App
    Store parsers accept app URLs (apps.apple.com/us/app/…/id…); the country in the
    path sets the storefront, defaulting to us. g2-reviews returns the 25 most
    recently published reviews of a G2 product in data.reviews (rating, title,
    likes, dislikes, problems_solved, reviewer role, company size, and industry),
    plus data.product. It accepts G2 product URLs (g2.com/products/…), follows
    renamed products, and keeps star-rating filters from the URL
    (filters[nps_score][]=1 to 5); other filters, sort orders, and pages are
    ignored. instagram-profile parses a public profile (instagram.com/{username})
    into data: bio, links, follower and post counts, category, business address,
    similar_accounts, and latest_posts (up to the 12 posts at the top of the
    profile, newest first). Instagram lists pinned posts there ahead of newer ones,
    so posts with is_pinned true can be older; when Instagram shows only a rounded
    post count (32K), post_count is that rounded number and is_post_count_rounded is
    true. instagram-post parses a post or reel (/p/…, /reel/…) into data: caption,
    hashtags, mentions, like, comment, and view counts (like_count and view_count
    are null when the owner hides them), media URLs, tagged users, collaborators,
    location, and the top ~14 comments in data.comments. instagram-feed returns the
    top posts for a hashtag or keyword (/explore/tags/…, /popular/…) or the recent
    posts at a location (/explore/locations/{id}/…) in data.posts; keyword posts
    carry only the shortcode, owner, thumbnail, and views, plus the caption when
    Instagram shows it. All three Instagram parsers read public data without logging
    in, so private accounts return no posts and follower lists are unavailable.
    tiktok-profile parses a public profile (tiktok.com/@{username}) into data:
    nickname, bio, bio link, follower, following, like, and video counts, verified,
    private, and business flags, and business category; it does not list videos.
    tiktok-video parses a video or photo post (/@{username}/video/{id} or
    /@{username}/photo/{id}) into data: caption, hashtags, mentions, author, view,
    like, comment, share, save, and repost counts, duration, thumbnail, a video_url
    that downloads without cookies, image_urls for photo posts, music, location, and
    ad, paid-partnership, and AI-generated flags. tiktok-feed returns videos in the
    tiktok-video shape as data.videos: the latest 15 from a profile URL, the top 30
    from a hashtag URL (/tag/{name}), or the top 12 from a search URL
    (/search?q={query}). tiktok-comments returns the first 20 comments of a video or
    photo post as data.comments: text, posted_at, like and reply counts, whether the
    author liked it, and the commenter. tiktok-followers and tiktok-following return
    up to 30 accounts of a profile as data.users, in the tiktok-profile shape.
    tiktok-user-search returns the top 10 accounts for a user search URL
    (/search/user?q={query}) as data.users: id, username, nickname, biography,
    avatar_url, sec_uid, follower_count, like_count, and is_verified. The TikTok
    parsers accept tiktok.com, www.tiktok.com, and m.tiktok.com URLs but not short
    links (vm.tiktok.com, vt.tiktok.com, tiktok.com/t/…). emails accepts any page
    and returns its email addresses as data.emails ([{ email }]), read from mailto
    links, Cloudflare-protected addresses, and visible text. phone-numbers accepts
    any page and returns its valid phone numbers in E.164 as data.phone_numbers ([{
    phone }]), read from tel links and visible text; numbers without a country code
    are read for the country of the site TLD, defaulting to US. links accepts any
    page and returns its unique http(s) links as data.links ([{ url, text }]), with
    absolute URLs; text falls back to aria-label or image alt and is null when a
    link has none. The emails parser reads the rendered page and respects content
    filters; the other prebuilt parsers read their data independently of DOM
    filters.
    """

    type: Required[Literal["prebuilt"]]
    """Use a prebuilt parser instead of custom rules."""

    limit: int
    """google-maps-reviews only.

    Maximum number of reviews to return. Defaults to 100; maximum 1000.
    """

    sort: Literal["newest", "oldest", "relevant", "highest", "lowest"]
    """google-maps-reviews only.

    Order of data.reviews. newest, relevant, highest, and lowest follow Google;
    oldest returns the earliest reviews first, which Google itself does not offer.
    """


InputScrapeDataBatchUnifiedScrapeDataParseParams: TypeAlias = Union[
    InputScrapeDataBatchUnifiedScrapeDataParseParamsCustomParser,
    InputScrapeDataBatchUnifiedScrapeDataParseParamsPrebuiltParser,
]


class InputScrapeDataBatchUnifiedScrapeDataProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    dedupe_images: Annotated[bool, PropertyInfo(alias="dedupeImages")]
    """Drop visually duplicate product images, keeping the largest copy."""

    use_ai_fallback: Annotated[bool, PropertyInfo(alias="useAIFallback")]
    """Ignored. The AI fallback runs automatically."""


class InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"],
    InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaElement,
    InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsAreaRectangle,
]


class InputScrapeDataBatchUnifiedScrapeDataScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: InputScrapeDataBatchUnifiedScrapeDataScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Max 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    direction: Literal["down", "up", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps for this action."""

    selector: str
    """Scroll this container. Omit to scroll the page."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """Time to pause in milliseconds before the next action."""

    type: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Use `waitFor` to wait for a matching element."""


InputScrapeDataBatchUnifiedScrapeDataSharedParamsAction: TypeAlias = Union[
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionPerform,
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionScroll,
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWait,
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsActionWaitFor,
]


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsersPdf(TypedDict, total=False):
    """PDF page range and OCR."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least `startPage`."""

    include_numbered_pages: Annotated[bool, PropertyInfo(alias="includeNumberedPages")]
    """
    Start each page in the Markdown with a `<!-- page N -->` line using its original
    1-based page number; these responses are never served from cache.
    """

    ocr: Literal["off", "auto"]
    """Set `auto` to read scanned pages with OCR."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsersPdf
    """PDF page range and OCR."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileExisting(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]
    """The ID returned in profile.id by an earlier scrape."""

    type: Required[Literal["existing"]]
    """Reuse a saved browser profile."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileNew(TypedDict, total=False):
    identifier: Required[str]
    """Username or email for the target website."""

    password: Required[str]
    """Password used to sign in. It is never stored in the profile."""

    type: Required[Literal["new"]]
    """Sign in and create a browser profile."""

    description: str
    """Optional label shown when listing profiles with `GET /org/browser/profiles`."""


InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfile: TypeAlias = Union[
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileExisting,
    InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfileNew,
]


class InputScrapeDataBatchUnifiedScrapeDataSharedParamsViewport(TypedDict, total=False):
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class InputScrapeDataBatchUnifiedScrapeDataSharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[InputScrapeDataBatchUnifiedScrapeDataSharedParamsAction]
    """Browser steps run in order before capture.

    Requires a paid plan. Skips the cache.
    """

    country: str
    """Proxy country as a two-letter code, such as `US`. Case-insensitive."""

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Accept cookie banners before actions and capture."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Close other popups before actions and capture."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Include iframe content in HTML and text outputs.

    Screenshots always show visible frames.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only the main content. Doesn't affect `screenshot`, `bytes`, or `product`."""

    parsers: InputScrapeDataBatchUnifiedScrapeDataSharedParamsParsers
    """Document parsing options."""

    profile: InputScrapeDataBatchUnifiedScrapeDataSharedParamsProfile
    """Create or reuse an authenticated browser profile.

    Requires a paid plan and an HTTPS target. Profiles persist session state, bypass
    shared caches, and cannot be combined with ZDR, custom headers, raw bytes, or
    prebuilt parsers.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `screenshot` is requested.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: InputScrapeDataBatchUnifiedScrapeDataSharedParamsViewport
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Milliseconds, or a CSS selector to wait for, after actions.

    Defaults to 500 (2000 with frames or XML).
    """


class InputScrapeDataBatchUnifiedScrapeDataTimeoutOpts(TypedDict, total=False):
    """
    Deadline for each page, using the same behavior and defaults as POST /web/scrape.
    """

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class InputScrapeDataBatchUnifiedScrapeData(TypedDict, total=False):
    """Use the same formats and parameters as POST /web/scrape, replacing url with urls.

    Options apply to every page.
    """

    formats: Required[InputScrapeDataBatchUnifiedScrapeDataFormats]
    """Outputs to return. Set at least one to `true`."""

    urls: Required[Iterable[InputScrapeDataBatchUnifiedScrapeDataURL]]
    """Pages to scrape. Maximum 100000."""

    highlights_params: Annotated[
        InputScrapeDataBatchUnifiedScrapeDataHighlightsParams, PropertyInfo(alias="highlightsParams")
    ]
    """Requires `formats.highlights: true`; required when it is set."""

    image_params: Annotated[InputScrapeDataBatchUnifiedScrapeDataImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[InputScrapeDataBatchUnifiedScrapeDataJsonParams, PropertyInfo(alias="jsonParams")]
    """Requires `formats.json: true`; required when it is set."""

    markdown_params: Annotated[
        InputScrapeDataBatchUnifiedScrapeDataMarkdownParams, PropertyInfo(alias="markdownParams")
    ]
    """Markdown options. Requires `formats.markdown`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached output, in milliseconds.

    `0` fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[InputScrapeDataBatchUnifiedScrapeDataParseParams, PropertyInfo(alias="parseParams")]
    """Requires `formats.parse: true`; required when it is set."""

    product_params: Annotated[InputScrapeDataBatchUnifiedScrapeDataProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[
        InputScrapeDataBatchUnifiedScrapeDataScreenshotParams, PropertyInfo(alias="screenshotParams")
    ]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[InputScrapeDataBatchUnifiedScrapeDataSharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[InputScrapeDataBatchUnifiedScrapeDataTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """
    Deadline for each page, using the same behavior and defaults as POST
    /web/scrape.
    """

    zdr: Literal["disabled"]
    """Batches persist their results.

    Only disabled is supported; enabled returns ZDR_NOT_SUPPORTED.
    """


InputScrapeData: TypeAlias = Union[InputScrapeDataMarkdown, InputScrapeDataHTML, InputScrapeDataBatchUnifiedScrapeData]


class InputScrape(TypedDict, total=False):
    """Scrape a list of up to 100,000 URLs."""

    data: Required[InputScrapeData]
    """Pages to scrape and their output format."""

    mode: Required[Literal["scrape"]]
    """Scrape the pages in `data.urls`."""


class InputCrawlDataMarkdownSourceStartURLControls(TypedDict, total=False):
    """Limits and filters for page discovery."""

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """Regex pattern for URLs to exclude, even when they match `regex`.

    The `start_url` itself is always included.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    languages: Union[
        Literal["same_as_start_url"],
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
    Only follow pages in these languages, or `same_as_start_url`; all languages when
    omitted.
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern for URLs to include. The `start_url` itself is always included."""


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

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """
    Regex pattern; sitemap URLs matching it are not scraped, even when they match
    `regex`.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern; only sitemap URLs matching it are scraped."""


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
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    ocr: bool
    """Read scanned PDF pages with OCR; preserve pages that already have text."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDFs fail with `PDF_SKIPPED`."""

    start: int
    """First 1-based PDF page to parse."""


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
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_html: Annotated[bool, PropertyInfo(alias="includeHTML")]
    """Also return each page's HTML in `html`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Include links in the Markdown (`html-conversion` only)."""

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors.

    Filtered pages ignore `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds.

    Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms). `0` fetches
    fresh.
    """

    pdf: InputCrawlDataMarkdownOptionsPdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before extracting, on browser-rendered pages."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten inline base64 image data (`html-conversion` only)."""

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """

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

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """Regex pattern for URLs to exclude, even when they match `regex`.

    The `start_url` itself is always included.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    languages: Union[
        Literal["same_as_start_url"],
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
    Only follow pages in these languages, or `same_as_start_url`; all languages when
    omitted.
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern for URLs to include. The `start_url` itself is always included."""


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

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """
    Regex pattern; sitemap URLs matching it are not scraped, even when they match
    `regex`.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern; only sitemap URLs matching it are scraped."""


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
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    end: int
    """Last PDF page to parse (1-based, inclusive).

    Defaults to the final page. Must be >= start.
    """

    ocr: bool
    """Read scanned PDF pages with OCR; preserve pages that already have text."""

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """Parse PDF URLs. When false, PDFs fail with `PDF_SKIPPED`."""

    start: int
    """First 1-based PDF page to parse."""


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
    """Fetch from this country (ISO 3166-1 alpha-2)."""

    exclude_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors.

    Applied after `includeSelectors`, so an element matching both is removed.
    """

    include_selectors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors.

    Filtered pages ignore `maxAgeMs`.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum cache age in milliseconds.

    Defaults to 3 days (259200000 ms). Maximum: 1 year (31536000000 ms). `0` fetches
    fresh.
    """

    pdf: InputCrawlDataHTMLOptionsPdf
    """PDF handling. `start`/`end` limit parsing to an inclusive, 1-based page range."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before extracting, on browser-rendered pages."""

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


class InputCrawlDataBatchUnifiedCrawlDataFormats(TypedDict, total=False):
    """Outputs to return. Set at least one to `true`."""

    bytes: bool
    """The original HTTP response body."""

    highlights: bool
    """Markdown excerpts relevant to `highlightsParams.query`."""

    html: bool
    """Rendered HTML."""

    images: bool
    """Images found on the page."""

    json: bool
    """An object matching `jsonParams.schema`, extracted from the page."""

    markdown: bool
    """Page content as Markdown."""

    parse: bool
    """Fields extracted with custom rules or a prebuilt parser, returned as `parsed`."""

    product: bool
    """Product details such as name, price, and availability."""

    screenshot: bool
    """A screenshot of the page."""


class InputCrawlDataBatchUnifiedCrawlDataSourceStartURLControls(TypedDict, total=False):
    """Limits and filters for page discovery."""

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """Regex pattern for URLs to exclude, even when they match `regex`.

    The `start_url` itself is always included.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """Follow links to subdomains."""

    languages: Union[
        Literal["same_as_start_url"],
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
    Only follow pages in these languages, or `same_as_start_url`; all languages when
    omitted.
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Maximum link depth. Source pages are depth 0. No limit when omitted."""

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern for URLs to include. The `start_url` itself is always included."""


class InputCrawlDataBatchUnifiedCrawlDataSourceStartURL(TypedDict, total=False):
    """Discover pages by following links from one URL."""

    type: Required[Literal["start_url"]]
    """Start from one page."""

    url: Required[str]
    """Page where crawling begins. A URL without a scheme is read as https://."""

    controls: InputCrawlDataBatchUnifiedCrawlDataSourceStartURLControls
    """Limits and filters for page discovery."""


class InputCrawlDataBatchUnifiedCrawlDataSourceSitemapControls(TypedDict, total=False):
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so there is no crawl depth here.
    """

    exclude_regex: Annotated[str, PropertyInfo(alias="excludeRegex")]
    """
    Regex pattern; sitemap URLs matching it are not scraped, even when they match
    `regex`.
    """

    max_urls: Annotated[int, PropertyInfo(alias="maxUrls")]
    """Maximum pages to fetch. Unused reserved credits are refunded. Maximum 100000."""

    regex: str
    """Regex pattern; only sitemap URLs matching it are scraped."""


class InputCrawlDataBatchUnifiedCrawlDataSourceSitemap(TypedDict, total=False):
    """Scrape the pages listed in a domain's sitemap.

    Links on those pages are not followed.
    """

    domain: Required[str]
    """Domain whose sitemap lists the pages to scrape.

    A full URL is reduced to its domain.
    """

    type: Required[Literal["sitemap"]]
    """Scrape the URLs in the domain's sitemap."""

    controls: InputCrawlDataBatchUnifiedCrawlDataSourceSitemapControls
    """Limits and filters for the sitemap URLs.

    A sitemap batch scrapes exactly those URLs and never follows links off them, so
    there is no crawl depth here.
    """


InputCrawlDataBatchUnifiedCrawlDataSource: TypeAlias = Union[
    InputCrawlDataBatchUnifiedCrawlDataSourceStartURL, InputCrawlDataBatchUnifiedCrawlDataSourceSitemap
]


class InputCrawlDataBatchUnifiedCrawlDataHighlightsParams(TypedDict, total=False):
    """Requires `formats.highlights: true`; required when it is set."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of returned passages."""


class InputCrawlDataBatchUnifiedCrawlDataImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """Set `visual` to drop visual duplicates, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Extra data per image: `dimensions`, `classification`, or a hosted `file` URL."""


class InputCrawlDataBatchUnifiedCrawlDataJsonParams(TypedDict, total=False):
    """Requires `formats.json: true`; required when it is set."""

    schema: Required[Dict[str, object]]
    """JSON Schema (not an example object) for a top-level object, up to 50 KB.

    Use optional or nullable fields for missing facts.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class InputCrawlDataBatchUnifiedCrawlDataMarkdownParams(TypedDict, total=False):
    """Markdown options. Requires `formats.markdown`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include images in the Markdown (`html-conversion` only)."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown (`html-conversion` only)."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """How base64 images appear when `includeImages` is set (`html-conversion` only)."""

    source_preference: Annotated[
        List[Literal["html-conversion", "markdown-direct"]], PropertyInfo(alias="sourcePreference")
    ]
    """
    Markdown sources in order of preference: `html-conversion` converts the page
    HTML, `markdown-direct` uses Markdown the site publishes.
    """


class InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """Return text, HTML, an attribute such as `@href`, or nested field rules.

    Defaults to text.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRules: TypeAlias = Union[
    str, InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRulesUnionMember1
]


class InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParser(TypedDict, total=False):
    rules: Required[Dict[str, InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParserRules]]
    """Field names mapped to CSS selectors (`h1`, `a@href`) or rule objects.

    Max 100 fields, 5 levels.
    """

    type: Literal["custom"]
    """Extract fields using custom CSS rules.

    This is the default when type is omitted.
    """


class InputCrawlDataBatchUnifiedCrawlDataParseParamsPrebuiltParser(TypedDict, total=False):
    parser: Required[
        Literal[
            "google-maps",
            "google-maps-reviews",
            "google-play",
            "google-play-reviews",
            "app-store",
            "app-store-reviews",
            "g2-reviews",
            "instagram-profile",
            "instagram-post",
            "instagram-feed",
            "tiktok-profile",
            "tiktok-video",
            "tiktok-feed",
            "tiktok-comments",
            "tiktok-followers",
            "tiktok-following",
            "tiktok-user-search",
            "emails",
            "phone-numbers",
            "links",
        ]
    ]
    """google-maps parses Google Maps business data into data.results.

    Accepts Maps place, search, and internal data URLs. Uses a US exit and English
    labels regardless of hl or Accept-Language. google-maps-reviews returns the
    reviews of a place in data.reviews, in the same shape as the Serper reviews API
    (rating, date, isoDate, snippet, translatedSnippet, likes, user, media,
    response, link, id), plus language, guided ratings in details, and
    user.isLocalGuide; data also carries the place featureId, cid, and sort. sort
    and limit pick the order and count, and oldest is exact. It accepts Maps place,
    search, and ?cid= URLs, plus search.google.com/local/reviews URLs, so the
    google_maps_url and google_reviews_url fields of google-maps results work as
    input. An unknown place returns no reviews. google-play parses a Play Store app
    into data: details, developer contact, ratings, price, permissions, and data
    safety. google-play-reviews returns the 200 newest reviews of the app, with
    developer replies, in data.reviews. Both Play parsers accept app details URLs
    (play.google.com/store/apps/details?id=…); hl and gl set the language and
    storefront, defaulting to en and us. app-store parses an App Store app into
    data: details, developer, ratings, price, version, and screenshots.
    app-store-reviews returns up to the 500 newest reviews in data.reviews. Both App
    Store parsers accept app URLs (apps.apple.com/us/app/…/id…); the country in the
    path sets the storefront, defaulting to us. g2-reviews returns the 25 most
    recently published reviews of a G2 product in data.reviews (rating, title,
    likes, dislikes, problems_solved, reviewer role, company size, and industry),
    plus data.product. It accepts G2 product URLs (g2.com/products/…), follows
    renamed products, and keeps star-rating filters from the URL
    (filters[nps_score][]=1 to 5); other filters, sort orders, and pages are
    ignored. instagram-profile parses a public profile (instagram.com/{username})
    into data: bio, links, follower and post counts, category, business address,
    similar_accounts, and latest_posts (up to the 12 posts at the top of the
    profile, newest first). Instagram lists pinned posts there ahead of newer ones,
    so posts with is_pinned true can be older; when Instagram shows only a rounded
    post count (32K), post_count is that rounded number and is_post_count_rounded is
    true. instagram-post parses a post or reel (/p/…, /reel/…) into data: caption,
    hashtags, mentions, like, comment, and view counts (like_count and view_count
    are null when the owner hides them), media URLs, tagged users, collaborators,
    location, and the top ~14 comments in data.comments. instagram-feed returns the
    top posts for a hashtag or keyword (/explore/tags/…, /popular/…) or the recent
    posts at a location (/explore/locations/{id}/…) in data.posts; keyword posts
    carry only the shortcode, owner, thumbnail, and views, plus the caption when
    Instagram shows it. All three Instagram parsers read public data without logging
    in, so private accounts return no posts and follower lists are unavailable.
    tiktok-profile parses a public profile (tiktok.com/@{username}) into data:
    nickname, bio, bio link, follower, following, like, and video counts, verified,
    private, and business flags, and business category; it does not list videos.
    tiktok-video parses a video or photo post (/@{username}/video/{id} or
    /@{username}/photo/{id}) into data: caption, hashtags, mentions, author, view,
    like, comment, share, save, and repost counts, duration, thumbnail, a video_url
    that downloads without cookies, image_urls for photo posts, music, location, and
    ad, paid-partnership, and AI-generated flags. tiktok-feed returns videos in the
    tiktok-video shape as data.videos: the latest 15 from a profile URL, the top 30
    from a hashtag URL (/tag/{name}), or the top 12 from a search URL
    (/search?q={query}). tiktok-comments returns the first 20 comments of a video or
    photo post as data.comments: text, posted_at, like and reply counts, whether the
    author liked it, and the commenter. tiktok-followers and tiktok-following return
    up to 30 accounts of a profile as data.users, in the tiktok-profile shape.
    tiktok-user-search returns the top 10 accounts for a user search URL
    (/search/user?q={query}) as data.users: id, username, nickname, biography,
    avatar_url, sec_uid, follower_count, like_count, and is_verified. The TikTok
    parsers accept tiktok.com, www.tiktok.com, and m.tiktok.com URLs but not short
    links (vm.tiktok.com, vt.tiktok.com, tiktok.com/t/…). emails accepts any page
    and returns its email addresses as data.emails ([{ email }]), read from mailto
    links, Cloudflare-protected addresses, and visible text. phone-numbers accepts
    any page and returns its valid phone numbers in E.164 as data.phone_numbers ([{
    phone }]), read from tel links and visible text; numbers without a country code
    are read for the country of the site TLD, defaulting to US. links accepts any
    page and returns its unique http(s) links as data.links ([{ url, text }]), with
    absolute URLs; text falls back to aria-label or image alt and is null when a
    link has none. The emails parser reads the rendered page and respects content
    filters; the other prebuilt parsers read their data independently of DOM
    filters.
    """

    type: Required[Literal["prebuilt"]]
    """Use a prebuilt parser instead of custom rules."""

    limit: int
    """google-maps-reviews only.

    Maximum number of reviews to return. Defaults to 100; maximum 1000.
    """

    sort: Literal["newest", "oldest", "relevant", "highest", "lowest"]
    """google-maps-reviews only.

    Order of data.reviews. newest, relevant, highest, and lowest follow Google;
    oldest returns the earliest reviews first, which Google itself does not offer.
    """


InputCrawlDataBatchUnifiedCrawlDataParseParams: TypeAlias = Union[
    InputCrawlDataBatchUnifiedCrawlDataParseParamsCustomParser,
    InputCrawlDataBatchUnifiedCrawlDataParseParamsPrebuiltParser,
]


class InputCrawlDataBatchUnifiedCrawlDataProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    dedupe_images: Annotated[bool, PropertyInfo(alias="dedupeImages")]
    """Drop visually duplicate product images, keeping the largest copy."""

    use_ai_fallback: Annotated[bool, PropertyInfo(alias="useAIFallback")]
    """Ignored. The AI fallback runs automatically."""


class InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"],
    InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaElement,
    InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsAreaRectangle,
]


class InputCrawlDataBatchUnifiedCrawlDataScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: InputCrawlDataBatchUnifiedCrawlDataScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Max 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    direction: Literal["down", "up", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps for this action."""

    selector: str
    """Scroll this container. Omit to scroll the page."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """Time to pause in milliseconds before the next action."""

    type: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Use `waitFor` to wait for a matching element."""


InputCrawlDataBatchUnifiedCrawlDataSharedParamsAction: TypeAlias = Union[
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionPerform,
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionScroll,
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWait,
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsActionWaitFor,
]


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsersPdf(TypedDict, total=False):
    """PDF page range and OCR."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least `startPage`."""

    include_numbered_pages: Annotated[bool, PropertyInfo(alias="includeNumberedPages")]
    """
    Start each page in the Markdown with a `<!-- page N -->` line using its original
    1-based page number; these responses are never served from cache.
    """

    ocr: Literal["off", "auto"]
    """Set `auto` to read scanned pages with OCR."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsersPdf
    """PDF page range and OCR."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileExisting(TypedDict, total=False):
    profile_id: Required[Annotated[str, PropertyInfo(alias="profileId")]]
    """The ID returned in profile.id by an earlier scrape."""

    type: Required[Literal["existing"]]
    """Reuse a saved browser profile."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileNew(TypedDict, total=False):
    identifier: Required[str]
    """Username or email for the target website."""

    password: Required[str]
    """Password used to sign in. It is never stored in the profile."""

    type: Required[Literal["new"]]
    """Sign in and create a browser profile."""

    description: str
    """Optional label shown when listing profiles with `GET /org/browser/profiles`."""


InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfile: TypeAlias = Union[
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileExisting,
    InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfileNew,
]


class InputCrawlDataBatchUnifiedCrawlDataSharedParamsViewport(TypedDict, total=False):
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class InputCrawlDataBatchUnifiedCrawlDataSharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[InputCrawlDataBatchUnifiedCrawlDataSharedParamsAction]
    """Browser steps run in order before capture.

    Requires a paid plan. Skips the cache.
    """

    country: str
    """Proxy country as a two-letter code, such as `US`. Case-insensitive."""

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Accept cookie banners before actions and capture."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Close other popups before actions and capture."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove elements matching these CSS selectors. Overrides `includeSelectors`."""

    headers: Dict[str, str]
    """HTTP headers to send to the target site. Requests with headers skip the cache."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Include iframe content in HTML and text outputs.

    Screenshots always show visible frames.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep only elements matching these CSS selectors."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only the main content. Doesn't affect `screenshot`, `bytes`, or `product`."""

    parsers: InputCrawlDataBatchUnifiedCrawlDataSharedParamsParsers
    """Document parsing options."""

    profile: InputCrawlDataBatchUnifiedCrawlDataSharedParamsProfile
    """Create or reuse an authenticated browser profile.

    Requires a paid plan and an HTTPS target. Profiles persist session state, bypass
    shared caches, and cannot be combined with ZDR, custom headers, raw bytes, or
    prebuilt parsers.
    """

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `screenshot` is requested.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: InputCrawlDataBatchUnifiedCrawlDataSharedParamsViewport
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Milliseconds, or a CSS selector to wait for, after actions.

    Defaults to 500 (2000 with frames or XML).
    """


class InputCrawlDataBatchUnifiedCrawlDataTimeoutOpts(TypedDict, total=False):
    """
    Deadline for each page, using the same behavior and defaults as POST /web/scrape.
    """

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """


class InputCrawlDataBatchUnifiedCrawlData(TypedDict, total=False):
    """
    Use the same formats and parameters as POST /web/scrape, replacing url with source. Options apply to every page.
    """

    formats: Required[InputCrawlDataBatchUnifiedCrawlDataFormats]
    """Outputs to return. Set at least one to `true`."""

    source: Required[InputCrawlDataBatchUnifiedCrawlDataSource]
    """How to find pages to crawl."""

    highlights_params: Annotated[
        InputCrawlDataBatchUnifiedCrawlDataHighlightsParams, PropertyInfo(alias="highlightsParams")
    ]
    """Requires `formats.highlights: true`; required when it is set."""

    image_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataJsonParams, PropertyInfo(alias="jsonParams")]
    """Requires `formats.json: true`; required when it is set."""

    markdown_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataMarkdownParams, PropertyInfo(alias="markdownParams")]
    """Markdown options. Requires `formats.markdown`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached output, in milliseconds.

    `0` fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataParseParams, PropertyInfo(alias="parseParams")]
    """Requires `formats.parse: true`; required when it is set."""

    product_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[
        InputCrawlDataBatchUnifiedCrawlDataScreenshotParams, PropertyInfo(alias="screenshotParams")
    ]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[InputCrawlDataBatchUnifiedCrawlDataSharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[InputCrawlDataBatchUnifiedCrawlDataTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """
    Deadline for each page, using the same behavior and defaults as POST
    /web/scrape.
    """

    zdr: Literal["disabled"]
    """Batches persist their results.

    Only disabled is supported; enabled returns ZDR_NOT_SUPPORTED.
    """


InputCrawlData: TypeAlias = Union[InputCrawlDataMarkdown, InputCrawlDataHTML, InputCrawlDataBatchUnifiedCrawlData]


class InputCrawl(TypedDict, total=False):
    """Crawl pages starting from a URL or from a domain's sitemap."""

    data: Required[InputCrawlData]
    """Crawl source and output format."""

    mode: Required[Literal["crawl"]]
    """Discover and scrape pages from `data.source`."""


Input: TypeAlias = Union[InputScrape, InputCrawl]


class Webhook(TypedDict, total=False):
    """Where to send the batch's final-status event.

    Omit `retry` for one attempt; `{}` uses the default retry schedule.
    """

    url: Required[str]
    """
    Public HTTP(S) URL that receives batch completion, failure, or cancellation
    events.
    """

    retry: RetryConfigParam
    """Webhook retry settings. Use {} for the default schedule."""
