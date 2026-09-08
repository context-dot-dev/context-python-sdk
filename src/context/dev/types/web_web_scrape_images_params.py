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

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    wait_for_ms: Annotated[Optional[int], PropertyInfo(alias="waitForMs")]
    """
    Optional browser wait time in milliseconds after initial page load before
    collecting images. Min: 0. Max: 30000 (30 seconds).
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
    type.
    """

    max_time_per_ms: Annotated[int, PropertyInfo(alias="maxTimePerMs")]
    """Per-image enrichment timeout in milliseconds. Default: 30000. Maximum: 60000."""

    resolution: bool
    """Measure image width and height when possible."""
