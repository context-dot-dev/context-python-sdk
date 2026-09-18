# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebExtractParams",
    "Action",
    "ActionWebScrapeWaitAction",
    "ActionWebScrapePerformAction",
    "ActionWebScrapeScrollAction",
    "Pdf",
    "TimeoutOpts",
]


class WebExtractParams(TypedDict, total=False):
    schema: Required[Dict[str, object]]
    """JSON Schema for the returned data object.

    Image fields such as `image_urls` or `product_photos` automatically make page
    image references available to extraction, so product data and photos can be
    returned in one call. TypeScript Zod users can pass a JSON Schema generated from
    a Zod object; Python users can pass the equivalent JSON Schema object.
    """

    url: Required[str]
    """The starting website URL to crawl and extract from.

    Must include http:// or https://.
    """

    actions: Iterable[Action]
    """
    Optional browser actions executed in order on the requested page after it loads,
    before links are discovered or additional pages are crawled. Requires a paid
    plan. When actions are provided and stopAfterMs is omitted, the crawl budget
    defaults to 110000 ms.
    """

    fact_check: Annotated[bool, PropertyInfo(alias="factCheck")]
    """
    When true, every returned value must be grounded in facts stated on the page;
    fields that cannot be supported by the page are returned as null/empty. When
    false (default), the model may make reasonable inferences and derivations from
    the page content (e.g. ideal customer, competitor analysis, recommendations)
    while keeping verifiable specifics (names, quotes, URLs, dates, metrics)
    faithful to the source.
    """

    follow_subdomains: Annotated[bool, PropertyInfo(alias="followSubdomains")]
    """When true, follow links on subdomains of the starting URL's domain."""

    include_frames: Annotated[bool, PropertyInfo(alias="includeFrames")]
    """When true, iframe contents are included in Markdown before extraction."""

    instructions: str
    """
    Optional extraction guidance, such as which facts to prioritize or how to
    interpret fields in the schema.
    """

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return cached scrape results if a prior scrape for the same parameters is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms).
    """

    max_depth: Annotated[int, PropertyInfo(alias="maxDepth")]
    """Optional maximum link depth from the starting URL (0 = only the starting page).

    If omitted, there is no crawl depth limit.
    """

    max_pages: Annotated[int, PropertyInfo(alias="maxPages")]
    """Maximum number of pages to analyze for extraction. Hard cap: 50. Defaults to 5."""

    pdf: Pdf

    settle_animations: Annotated[bool, PropertyInfo(alias="settleAnimations")]
    """
    When true, waits briefly for CSS and transition animations to settle before
    extracting each crawled page. Defaults to false. This adds a bit of latency in
    exchange for more stable output on animated pages.
    """

    stop_after_ms: Annotated[int, PropertyInfo(alias="stopAfterMs")]
    """Soft time budget for the crawl in milliseconds.

    Min: 10000 (10s). Max: 110000 (110s). Defaults to 80000 (80s), or 110000 (110s)
    when browser actions are provided.
    """

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    wait_for_ms: Annotated[int, PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load for each
    crawled page.
    """

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Asset uploads are skipped, so hosted image URLs are
    omitted. Requires zero data retention to be enabled for your organization
    (contact support@context.dev), otherwise the request fails with ZDR_NOT_ENABLED.
    Successful ZDR responses include X-Context-ZDR: true.
    """


class ActionWebScrapeWaitAction(TypedDict, total=False):
    """Pause for a fixed number of milliseconds before continuing to the next action."""

    do: Required[Literal["wait"]]

    time_ms: Required[Annotated[int, PropertyInfo(alias="timeMs")]]


class ActionWebScrapePerformAction(TypedDict, total=False):
    """Resolve and perform one natural-language browser action."""

    action: Required[str]

    do: Required[Literal["perform"]]


class ActionWebScrapeScrollAction(TypedDict, total=False):
    """
    Scroll the page or a selected scrollable container, waiting adaptively for content and dimensions to settle after each iteration.
    """

    do: Required[Literal["scroll"]]

    amount: Union[int, Literal["viewport", "max"]]
    """Pixels per scroll, one visible viewport, or the current scroll boundary.

    Defaults to viewport.
    """

    container: str
    """CSS selector for the first matching scroll container. Defaults to the page."""

    direction: Literal["up", "down", "left", "right"]
    """Direction to scroll. Defaults to down."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum scroll iterations.

    Stops early when scrolling and scrollable extent stop changing. Defaults to 1.
    """


Action: TypeAlias = Union[ActionWebScrapeWaitAction, ActionWebScrapePerformAction, ActionWebScrapeScrollAction]


class Pdf(TypedDict, total=False):
    end: int
    """Last 1-based PDF page to parse.

    Must be greater than or equal to start when both are provided.
    """

    should_parse: Annotated[bool, PropertyInfo(alias="shouldParse")]
    """When true, PDF pages are fetched and parsed. When false, PDF pages are skipped."""

    start: int
    """First 1-based PDF page to parse."""


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
