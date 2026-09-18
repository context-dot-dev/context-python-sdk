# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "WebWebScrapeImagesParams",
    "Action",
    "ActionWebScrapeWaitAction",
    "ActionWebScrapePerformAction",
    "ActionWebScrapeScrollAction",
    "Enrichment",
    "TimeoutOpts",
]


class WebWebScrapeImagesParams(TypedDict, total=False):
    url: Required[str]
    """Page URL to inspect. Must include http:// or https://."""

    actions: Optional[Iterable[Action]]
    """
    Optional browser actions executed in array order after the page loads and before
    content is captured. Requires a paid plan. Send a JSON array in the query
    parameter. Maximum: 5 actions.
    """

    dedupe: bool
    """
    When true, visually duplicate images are removed: every image is loaded and
    perceptually hashed, and only the highest-resolution copy of each duplicate
    group is kept. Images that cannot be downloaded or hashed are kept. Default:
    false.
    """

    enrichment: Optional[Enrichment]
    """
    Optional per-image processing, sent as deep-object query params such as
    enrichment[resolution]=true.
    """

    headers: Dict[str, str]
    """
    Optional outbound HTTP headers forwarded only to the target URL, sent as
    deep-object query params such as headers[X-Custom]=value. When provided, caching
    is bypassed: the result is neither read from nor written to cache.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Reuse a cached result this many milliseconds old or newer.

    Default: 86400000 (1 day). Set to 0 to bypass cache. Maximum: 2592000000 (30
    days).
    """

    tags: SequenceNotStr[str]
    """Comma-separated tags for tracking request usage.

    Up to 20 tags, each 1-50 characters.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    collecting images. Min: 0. Max: 30000 (30 seconds). When combined with
    timeoutOpts, timeoutOpts.milliseconds must be at least waitForMs + 10000 ms; a
    shorter deadline is rejected with 400 TIMEOUT_TOO_SHORT_FOR_WAIT.
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


class Enrichment(TypedDict, total=False):
    """
    Optional per-image processing, sent as deep-object query params such as enrichment[resolution]=true.
    """

    classification: bool
    """Classify each image by visual asset type."""

    hosted_url: Annotated[bool, PropertyInfo(alias="hostedUrl")]
    """
    Host materializable images on the Brand.dev CDN and return their URL and MIME
    type. Ignored when zero data retention is enabled.
    """

    max_time_per_ms: Annotated[int, PropertyInfo(alias="maxTimePerMs")]
    """Per-image enrichment timeout in milliseconds. Default: 30000. Maximum: 60000."""

    resolution: bool
    """Measure image width and height when possible."""


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
    results. "return-partial" requires milliseconds of at least 5000.
    """
