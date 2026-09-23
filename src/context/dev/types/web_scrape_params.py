# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebScrapeParams",
    "Formats",
    "HighlightsParams",
    "ImageParams",
    "JsonParams",
    "MarkdownParams",
    "ParseParams",
    "ParseParamsRules",
    "ParseParamsRulesUnionMember1",
    "ProductParams",
    "ScreenshotParams",
    "ScreenshotParamsArea",
    "ScreenshotParamsAreaElement",
    "ScreenshotParamsAreaRectangle",
    "SharedParams",
    "SharedParamsAction",
    "SharedParamsActionPerform",
    "SharedParamsActionScroll",
    "SharedParamsActionWait",
    "SharedParamsActionWaitFor",
    "SharedParamsParsers",
    "SharedParamsParsersPdf",
    "SharedParamsViewport",
    "TimeoutOpts",
]


class WebScrapeParams(TypedDict, total=False):
    formats: Required[Formats]
    """Outputs to return. Enable at least one; omitted formats are false."""

    url: Required[str]
    """The URL to scrape."""

    highlights_params: Annotated[HighlightsParams, PropertyInfo(alias="highlightsParams")]
    """Highlight options. Requires formats.highlights: true."""

    image_params: Annotated[ImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[JsonParams, PropertyInfo(alias="jsonParams")]
    """Required when formats.json is true."""

    markdown_params: Annotated[MarkdownParams, PropertyInfo(alias="markdownParams")]
    """Markdown options. Requires formats.markdown: true."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of each cached output.

    Defaults to 1 day; 0 fetches fresh and updates the requested outputs. Compatible
    outputs are shared with the individual scrape endpoints. Image results with
    hosted files refresh after 23 hours; other outputs retain their own freshness.
    """

    parse_params: Annotated[ParseParams, PropertyInfo(alias="parseParams")]
    """Required when formats.parse is true."""

    product_params: Annotated[ProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[ScreenshotParams, PropertyInfo(alias="screenshotParams")]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[SharedParams, PropertyInfo(alias="sharedParams")]
    """Shared browser and content settings.

    Content filters leave screenshots and original bytes unchanged.
    """

    tags: SequenceNotStr[str]
    """Labels for tracking request usage. Not retained when zdr is enabled."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Total deadline, including navigation, actions, waiting, and all outputs.

    Defaults to 60000 milliseconds with behavior fail. Use return-partial to capture
    the current page state and return captured images if image processing cannot
    finish before the deadline; these responses set isPartial and are not cached.
    Every requested format must still be available. Fixed waits must fit before a
    response reserve of up to 5000 milliseconds (at most one quarter of the timeout)
    when using return-partial.
    """

    zdr: Literal["enabled", "disabled"]
    """Zero data retention.

    Bypasses caches and uploads; excludes request/response content and tags from
    logs. Must be enabled for your organization. Not available with the highlights
    output.
    """


class Formats(TypedDict, total=False):
    """Outputs to return. Enable at least one; omitted formats are false."""

    bytes: bool
    """The original HTTP response body."""

    highlights: bool
    """
    Plain-text passages from the page that are most relevant to
    highlightsParams.query, each prefixed with its section heading. Adds 3 credits.
    Not available with zdr enabled.
    """

    html: bool
    """Rendered HTML."""

    images: bool
    """Images found on the page."""

    json: bool
    """
    Page data extracted by an LLM from the page Markdown into jsonParams.schema;
    values carried only in attributes or CSS classes need formats.parse instead.
    Adds four credits when the page has text to extract; when shared content filters
    leave no text the result is an empty object and only the base price applies.
    """

    markdown: bool
    """Page content as Markdown."""

    parse: bool
    """Fields selected by parseParams.rules."""

    product: bool
    """Structured product data for product detail pages. Adds one credit."""

    screenshot: bool
    """An inline image of the page."""


class HighlightsParams(TypedDict, total=False):
    """Highlight options. Requires formats.highlights: true."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of the returned passages, in characters."""


class ImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """For visual duplicates, keep the largest image."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Add dimensions, a visual category, or a hosted file URL.

    Each image has a maximum processing time of 30000 milliseconds, bounded by the
    remaining request deadline.
    """


class JsonParams(TypedDict, total=False):
    """Required when formats.json is true."""

    schema: Required[Dict[str, object]]
    """JSON Schema for the returned object.

    Must describe a top-level object; at most 50 KB serialized. Optional fields the
    page does not state are omitted, or null when their type allows null, while
    required non-nullable fields always receive a best-effort value, so prefer
    nullable or optional fields for data a page may omit. Zod users can pass the
    output of z.toJSONSchema().
    """

    instructions: str
    """
    Optional guidance on which facts to prioritize or how to interpret schema
    fields.
    """


class MarkdownParams(TypedDict, total=False):
    """Markdown options. Requires formats.markdown: true."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """Base64 images use placeholders by default. Requires includeImages: true."""


class ParseParamsRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]

    output: Union[Literal["text", "html"], str, object]

    type: Literal["item", "list"]


ParseParamsRules: TypeAlias = Union[str, ParseParamsRulesUnionMember1]


class ParseParams(TypedDict, total=False):
    """Required when formats.parse is true."""

    rules: Required[Dict[str, ParseParamsRules]]
    """Map field names to CSS selectors or rules.

    Missing items return null; missing lists return [].
    """


class ProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    use_ai_fallback: Annotated[bool, PropertyInfo(alias="useAIFallback")]
    """
    Extract the product with a specialized model when the page has no structured
    product data. Adds six credits when the model returns a verdict. If the fallback
    fails, returns a partial response with the deterministic result and no fallback
    charge. Request deadlines and client disconnects still apply.
    """


class ScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """Must match one visible element."""


class ScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]

    width: Required[int]

    x: Required[int]

    y: Required[int]


ScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"], ScreenshotParamsAreaElement, ScreenshotParamsAreaRectangle
]


class ScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: ScreenshotParamsArea
    """Viewport, full page, one visible element, or a rectangle.

    Maximum 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]


class SharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]

    type: Required[Literal["perform"]]


class SharedParamsActionScroll(TypedDict, total=False):
    type: Required[Literal["scroll"]]

    amount: Union[int, Literal["viewport", "max"]]

    direction: Literal["down", "up", "left", "right"]

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]

    selector: str
    """Scroll this container. Omit to scroll the page."""


class SharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]

    type: Required[Literal["wait"]]


class SharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]

    type: Required[Literal["waitFor"]]


SharedParamsAction: TypeAlias = Union[
    SharedParamsActionPerform, SharedParamsActionScroll, SharedParamsActionWait, SharedParamsActionWaitFor
]


class SharedParamsParsersPdf(TypedDict, total=False):
    """PDF text options for HTML, Markdown, and parsed fields."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least startPage."""

    ocr: Literal["off", "auto"]
    """Read text from scanned pages."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class SharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: SharedParamsParsersPdf
    """PDF text options for HTML, Markdown, and parsed fields."""


class SharedParamsViewport(TypedDict, total=False):
    """Browser dimensions in pixels."""

    height: int

    width: int


class SharedParams(TypedDict, total=False):
    """Shared browser and content settings.

    Content filters leave screenshots and original bytes unchanged.
    """

    actions: Iterable[SharedParamsAction]
    """Run in order before capture.

    A failed action fails the request. Bypasses caching.
    """

    country: str
    """Supported two-letter country code, case-insensitive.

    Applies to every output, including image downloads.
    """

    dismiss_cookies: Annotated[bool, PropertyInfo(alias="dismissCookies")]
    """Dismiss cookie banners by accepting cookies before actions."""

    dismiss_popups: Annotated[bool, PropertyInfo(alias="dismissPopups")]
    """Dismiss other popups before actions."""

    exclude_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="excludeSelectors")]
    """Remove matching content. Exclusions win."""

    headers: Dict[str, str]
    """Headers for the target origin. Requests with custom headers bypass caching."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """Include iframe content in extraction.

    Screenshots show visible frames regardless.
    """

    include_selectors: Annotated[SequenceNotStr[str], PropertyInfo(alias="includeSelectors")]
    """Keep matching content after mainContentOnly."""

    main_content_only: Annotated[bool, PropertyInfo(alias="mainContentOnly")]
    """Keep only main content in HTML, Markdown, images, and parsed fields."""

    parsers: SharedParamsParsers
    """Document parsing options."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Settle animations before capture.

    Defaults to true with screenshots, otherwise false.
    """

    theme: Literal["light", "dark"]
    """Override the browser color scheme."""

    viewport: SharedParamsViewport
    """Browser dimensions in pixels."""

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """After actions, wait this many milliseconds or until a CSS selector is visible.

    Defaults to 500 ms, or 2000 ms with frames or an XML URL. Set 0 to skip.
    """


class TimeoutOpts(TypedDict, total=False):
    """Total deadline, including navigation, actions, waiting, and all outputs.

    Defaults to 60000 milliseconds with behavior fail. Use return-partial to capture the current page state and return captured images if image processing cannot finish before the deadline; these responses set isPartial and are not cached. Every requested format must still be available. Fixed waits must fit before a response reserve of up to 5000 milliseconds (at most one quarter of the timeout) when using return-partial.
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
