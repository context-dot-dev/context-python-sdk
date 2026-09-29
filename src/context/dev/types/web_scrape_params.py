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
    """Outputs to return. Set at least one to `true`."""

    url: Required[str]
    """Public HTTP or HTTPS URL to scrape."""

    highlights_params: Annotated[HighlightsParams, PropertyInfo(alias="highlightsParams")]
    """Requires `formats.highlights: true`; required when it is set."""

    image_params: Annotated[ImageParams, PropertyInfo(alias="imageParams")]
    """Image options. Requires formats.images: true."""

    json_params: Annotated[JsonParams, PropertyInfo(alias="jsonParams")]
    """Requires `formats.json: true`; required when it is set."""

    markdown_params: Annotated[MarkdownParams, PropertyInfo(alias="markdownParams")]
    """Markdown options. Requires `formats.markdown`."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached output, in milliseconds.

    `0` fetches fresh. Defaults to 3 days (259200000 ms). Maximum: 1 year
    (31536000000 ms).
    """

    parse_params: Annotated[ParseParams, PropertyInfo(alias="parseParams")]
    """Requires `formats.parse: true`; required when it is set."""

    product_params: Annotated[ProductParams, PropertyInfo(alias="productParams")]
    """Product options. Requires formats.product: true."""

    screenshot_params: Annotated[ScreenshotParams, PropertyInfo(alias="screenshotParams")]
    """Screenshot options. Requires formats.screenshot: true."""

    shared_params: Annotated[SharedParams, PropertyInfo(alias="sharedParams")]
    """Browser and content settings shared by all outputs."""

    tags: SequenceNotStr[str]
    """Labels for tracking request usage. Not retained when zdr is enabled."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Deadline for the whole request.

    Defaults to 90000 ms with `fail`. Fixed waits must end before it.
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Your organization must have ZDR enabled.
    """


class Formats(TypedDict, total=False):
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
    """Fields extracted with `parseParams.rules`, returned as `parsed`."""

    product: bool
    """Product details such as name, price, and availability."""

    screenshot: bool
    """A screenshot of the page."""


class HighlightsParams(TypedDict, total=False):
    """Requires `formats.highlights: true`; required when it is set."""

    query: Required[str]
    """The question or topic to find passages for."""

    max_characters: Annotated[int, PropertyInfo(alias="maxCharacters")]
    """Maximum combined length of returned passages."""


class ImageParams(TypedDict, total=False):
    """Image options. Requires formats.images: true."""

    dedupe: Literal["none", "visual"]
    """Set `visual` to drop visual duplicates, keeping the largest copy."""

    enrich: List[Literal["dimensions", "classification", "file"]]
    """Extra data per image: `dimensions`, `classification`, or a hosted `file` URL."""


class JsonParams(TypedDict, total=False):
    """Requires `formats.json: true`; required when it is set."""

    schema: Required[Dict[str, object]]
    """JSON Schema (not an example object) for a top-level object, up to 50 KB.

    Use optional or nullable fields for missing facts.
    """

    instructions: str
    """Extra guidance, such as which facts to prefer or how to read a field."""


class MarkdownParams(TypedDict, total=False):
    """Markdown options. Requires `formats.markdown`."""

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include images in the Markdown using image syntax with URLs and alt text."""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Keep link URLs in the Markdown. Set false to return link text without URLs."""

    inline_images: Annotated[Literal["placeholder", "preserve"], PropertyInfo(alias="inlineImages")]
    """How base64 images appear: `placeholder` (default) or `preserve`.

    Requires `includeImages`.
    """


class ParseParamsRulesUnionMember1(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to match within the current page or parent rule."""

    output: Union[Literal["text", "html"], str, object]
    """Return text, HTML, an attribute such as `@href`, or nested field rules.

    Defaults to text.
    """

    type: Literal["item", "list"]
    """Return the first match with `item` or all matches with `list`."""


ParseParamsRules: TypeAlias = Union[str, ParseParamsRulesUnionMember1]


class ParseParams(TypedDict, total=False):
    """Requires `formats.parse: true`; required when it is set."""

    rules: Required[Dict[str, ParseParamsRules]]
    """Field names mapped to CSS selectors (`h1`, `a@href`) or rule objects.

    Max 100 fields, 5 levels.
    """


class ProductParams(TypedDict, total=False):
    """Product options. Requires formats.product: true."""

    use_ai_fallback: Annotated[bool, PropertyInfo(alias="useAIFallback")]
    """Use an AI model when the page has no structured product data."""


class ScreenshotParamsAreaElement(TypedDict, total=False):
    selector: Required[str]
    """CSS selector matching exactly one visible element."""


class ScreenshotParamsAreaRectangle(TypedDict, total=False):
    """Pixels from the document origin."""

    height: Required[int]
    """Height of the capture in pixels."""

    width: Required[int]
    """Width of the capture in pixels."""

    x: Required[int]
    """Left edge of the capture, in pixels from the document origin."""

    y: Required[int]
    """Top edge of the capture, in pixels from the document origin."""


ScreenshotParamsArea: TypeAlias = Union[
    Literal["viewport", "fullPage"], ScreenshotParamsAreaElement, ScreenshotParamsAreaRectangle
]


class ScreenshotParams(TypedDict, total=False):
    """Screenshot options. Requires formats.screenshot: true."""

    area: ScreenshotParamsArea
    """What to capture: `viewport`, `fullPage`, one element, or a rectangle.

    Max 40 megapixels.
    """

    format: Literal["png", "jpeg", "webp"]
    """Image format for the screenshot."""


class SharedParamsActionPerform(TypedDict, total=False):
    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    type: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class SharedParamsActionScroll(TypedDict, total=False):
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


class SharedParamsActionWait(TypedDict, total=False):
    milliseconds: Required[int]
    """Time to pause in milliseconds before the next action."""

    type: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""


class SharedParamsActionWaitFor(TypedDict, total=False):
    selector: Required[str]
    """CSS selector to wait for before continuing."""

    type: Required[Literal["waitFor"]]
    """Use `waitFor` to wait for a matching element."""


SharedParamsAction: TypeAlias = Union[
    SharedParamsActionPerform, SharedParamsActionScroll, SharedParamsActionWait, SharedParamsActionWaitFor
]


class SharedParamsParsersPdf(TypedDict, total=False):
    """PDF page range and OCR."""

    end_page: Annotated[int, PropertyInfo(alias="endPage")]
    """Last page to parse. Must be at least `startPage`."""

    ocr: Literal["off", "auto"]
    """Set `auto` to read scanned pages with OCR."""

    start_page: Annotated[int, PropertyInfo(alias="startPage")]
    """First page to parse, starting at 1."""


class SharedParamsParsers(TypedDict, total=False):
    """Document parsing options."""

    pdf: SharedParamsParsersPdf
    """PDF page range and OCR."""


class SharedParamsViewport(TypedDict, total=False):
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    height: int
    """Browser viewport height in pixels."""

    width: int
    """Browser viewport width in pixels."""


class SharedParams(TypedDict, total=False):
    """Browser and content settings shared by all outputs."""

    actions: Iterable[SharedParamsAction]
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

    parsers: SharedParamsParsers
    """Document parsing options."""

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """Wait for CSS animations to finish before capture.

    Defaults to `true` when `screenshot` is requested.
    """

    theme: Literal["light", "dark"]
    """Emulate a light or dark color scheme."""

    viewport: SharedParamsViewport
    """Browser size in pixels.

    Omit for 1920 × 1080. When provided, missing dimensions default to 1440 × 900.
    """

    wait_for: Annotated[Union[int, str], PropertyInfo(alias="waitFor")]
    """Milliseconds, or a CSS selector to wait for, after actions.

    Defaults to 500 (2000 with frames or XML).
    """


class TimeoutOpts(TypedDict, total=False):
    """Deadline for the whole request.

    Defaults to 90000 ms with `fail`. Fixed waits must end before it.
    """

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    "return-partial" requires at least 5000 ms.
    """
