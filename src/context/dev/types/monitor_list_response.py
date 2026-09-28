# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .retry_config import RetryConfig

__all__ = [
    "MonitorListResponse",
    "Data",
    "DataChangeDetection",
    "DataChangeDetectionMonitorsExactChangeDetection",
    "DataChangeDetectionMonitorsSemanticChangeDetection",
    "DataSchedule",
    "DataTarget",
    "DataTargetMonitorsPageTarget",
    "DataTargetMonitorsPageTargetAction",
    "DataTargetMonitorsPageTargetActionWebScrapeWaitAction",
    "DataTargetMonitorsPageTargetActionWebScrapePerformAction",
    "DataTargetMonitorsPageTargetActionWebScrapeScrollAction",
    "DataTargetMonitorsSitemapTarget",
    "DataTargetMonitorsExtractTarget",
    "DataBaseline",
    "DataBaselineMonitorsPageBaseline",
    "DataBaselineMonitorsSitemapBaseline",
    "DataBaselineMonitorsExtractBaseline",
    "DataLastError",
    "DataWebhook",
    "DataWebhookFailure",
    "KeyMetadata",
]


class DataChangeDetectionMonitorsExactChangeDetection(BaseModel):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Literal["exact"]
    """Use `exact` to compare visible text or sitemap URLs."""


class DataChangeDetectionMonitorsSemanticChangeDetection(BaseModel):
    """
    Detect meaningful content changes using the target’s instructions and optional schema.
    """

    type: Literal["semantic"]
    """Use `semantic` to judge changes against the target instructions."""

    confidence_threshold: Optional[float] = None
    """Minimum confidence required to report a meaningful change, from 0 to 1."""


DataChangeDetection: TypeAlias = Annotated[
    Union[DataChangeDetectionMonitorsExactChangeDetection, DataChangeDetectionMonitorsSemanticChangeDetection],
    PropertyInfo(discriminator="type"),
]


class DataSchedule(BaseModel):
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be between 10 minutes and 1 year.
    """

    frequency: int
    """Number of units between runs.

    The resulting interval (frequency × unit) must be at least 10 minutes and at
    most 1 year (e.g. minimum 10 when unit is minutes; maximum 365 when unit is
    days).
    """

    type: Literal["interval"]
    """Use `interval` to run on a repeating schedule."""

    unit: Literal["minutes", "hours", "days"]
    """Time unit used with `frequency` to set the run interval."""


class DataTargetMonitorsPageTargetActionWebScrapeWaitAction(BaseModel):
    """Pause for a fixed number of milliseconds before continuing to the next action."""

    do: Literal["wait"]
    """Use `wait` to pause for a fixed duration."""

    time_ms: int = FieldInfo(alias="timeMs")
    """Time to pause in milliseconds before the next action."""


class DataTargetMonitorsPageTargetActionWebScrapePerformAction(BaseModel):
    """Resolve and perform one natural-language browser action."""

    action: str
    """One browser instruction, such as clicking a button or entering text."""

    do: Literal["perform"]
    """Use `perform` for a plain-language browser instruction."""


class DataTargetMonitorsPageTargetActionWebScrapeScrollAction(BaseModel):
    """
    Scroll the page or a selected scrollable container, waiting adaptively for content and dimensions to settle after each iteration.
    """

    do: Literal["scroll"]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"], None] = None
    """Pixels per scroll, one visible viewport, or the current scroll boundary.

    Defaults to viewport.
    """

    container: Optional[str] = None
    """CSS selector for the first matching scroll container. Defaults to the page."""

    direction: Optional[Literal["up", "down", "left", "right"]] = None
    """Direction to scroll. Defaults to down."""

    max_scrolls: Optional[int] = FieldInfo(alias="maxScrolls", default=None)
    """Maximum scroll iterations.

    Stops early when scrolling and scrollable extent stop changing. Defaults to 1.
    """


DataTargetMonitorsPageTargetAction: TypeAlias = Annotated[
    Union[
        DataTargetMonitorsPageTargetActionWebScrapeWaitAction,
        DataTargetMonitorsPageTargetActionWebScrapePerformAction,
        DataTargetMonitorsPageTargetActionWebScrapeScrollAction,
    ],
    PropertyInfo(discriminator="do"),
]


class DataTargetMonitorsPageTarget(BaseModel):
    """Watch a single web page.

    Exact detection reports visible-text diffs; semantic detection judges confirmed stable diffs against `instructions`.
    """

    type: Literal["page"]
    """Use `page` to watch one web page."""

    url: str
    """Public HTTP(S) page URL to monitor."""

    actions: Optional[List[DataTargetMonitorsPageTargetAction]] = None
    """
    Optional browser actions executed in array order after the page loads, before
    content is captured, on every run. Requires a paid plan. Maximum: 5 actions.
    Changes create a new baseline.
    """

    exclude_selectors: Optional[List[str]] = None
    """Remove matching regions after inclusions. Changes create a new baseline."""

    include_selectors: Optional[List[str]] = None
    """Monitor these CSS-selected regions.

    Empty or omitted uses main content. Changes create a new baseline.
    """

    instructions: Optional[str] = None
    """Plain-language goal describing which page changes matter.

    When provided without change_detection, semantic detection is inferred.
    """

    normalize_whitespace: Optional[bool] = None
    """Normalize whitespace before comparing or analyzing text."""


class DataTargetMonitorsSitemapTarget(BaseModel):
    """Watch a site’s URL inventory for confirmed additions and removals."""

    type: Literal["sitemap"]
    """Use `sitemap` to watch a site for added or removed URLs."""

    url: str
    """Sitemap URL to monitor."""

    exclude: Optional[List[str]] = None
    """URL path patterns to exclude (max 50)."""

    include: Optional[List[str]] = None
    """URL path patterns to include (max 50)."""

    max_urls: Optional[int] = None
    """Maximum number of sitemap URLs to track (capped at 10,000)."""


class DataTargetMonitorsExtractTarget(BaseModel):
    """
    Track relevant pages selected by `schema` and `instructions`; refresh the page set periodically.
    """

    instructions: str
    """
    Natural-language instructions guiding which pages and facts to track and which
    changes to report.
    """

    type: Literal["extract"]
    """Use `extract` to watch structured data across selected pages."""

    url: str
    """Root URL to extract structured data from."""

    follow_subdomains: Optional[bool] = None
    """Allow page discovery on subdomains of the target site."""

    max_depth: Optional[int] = None
    """Optional maximum link depth from the starting URL (0 = only the starting page)."""

    max_pages: Optional[int] = None
    """Maximum number of pages to track."""

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """JSON Schema for page selection and the baseline snapshot.

    Changes return diffs and evidence.
    """


DataTarget: TypeAlias = Annotated[
    Union[DataTargetMonitorsPageTarget, DataTargetMonitorsSitemapTarget, DataTargetMonitorsExtractTarget],
    PropertyInfo(discriminator="type"),
]


class DataBaselineMonitorsPageBaseline(BaseModel):
    """Current baseline of a `page` monitor: the visible page text as last observed."""

    captured_at: datetime
    """When this baseline was last captured or replaced."""

    text: str
    """The page's visible text as last observed."""


class DataBaselineMonitorsSitemapBaseline(BaseModel):
    """
    Current baseline of a `sitemap` monitor: the normalized URL set as last observed.
    """

    captured_at: datetime
    """When this baseline was last captured or replaced."""

    url_count: int
    """Number of URLs in the baseline."""

    urls: List[str]
    """The sitemap URLs as last observed (sorted, normalized)."""


class DataBaselineMonitorsExtractBaseline(BaseModel):
    """
    Current baseline of an `extract` monitor: the pages it tracks and the structured data as last extracted.
    """

    captured_at: datetime
    """When this baseline was last captured or replaced."""

    data: object
    """
    Latest structured snapshot matching the extraction schema, refreshed at most
    daily; `null` before capture.
    """

    urls_analyzed: List[str]
    """The page URLs the monitor tracks and analyzes for changes."""


DataBaseline: TypeAlias = Union[
    DataBaselineMonitorsPageBaseline, DataBaselineMonitorsSitemapBaseline, DataBaselineMonitorsExtractBaseline, None
]


class DataLastError(BaseModel):
    """Error from the most recent failed run; null when the last run succeeded."""

    code: str

    message: str


class DataWebhook(BaseModel):
    """Webhook destination and delivery settings. Null means no webhook is configured."""

    url: str
    """Public HTTP(S) URL that receives events.

    Slack and GovSlack URLs get formatted messages.
    """

    events: Optional[List[Literal["change.detected", "run.completed"]]] = None
    """Events to deliver.

    Defaults to `change.detected`; `run.completed` also includes unchanged runs.
    """

    retry: Optional[RetryConfig] = None
    """Webhook retry settings. Use {} for the default schedule."""

    secret: Optional[str] = None
    """API-generated signing secret.

    Visible only with full access or `monitors:write` permission.
    """


class DataWebhookFailure(BaseModel):
    """
    Present while webhook deliveries are failing consecutively; null when deliveries are healthy or no webhook is configured. Cleared on the next successful delivery and when the webhook URL changes.
    """

    consecutive_failures: int
    """Number of consecutive delivery attempts that did not succeed."""

    last_failed_at: datetime

    last_message: str
    """Human-readable description of the most recent failure."""

    last_status: Literal["rejected", "failed", "skipped_unsafe_url"]
    """Outcome of the most recent failed delivery.

    rejected means a non-2xx response; failed means no HTTP response was received;
    skipped_unsafe_url means the URL failed the public-endpoint safety check.
    """


class Data(BaseModel):
    """A web monitor.

    `mode` is the constant `web`; behavior is described by `target` (page/sitemap/extract) and `change_detection` (exact/semantic).
    """

    id: str

    change_detection: DataChangeDetection
    """How changes are judged.

    Defaults to `semantic` for extract targets and page targets with `instructions`,
    otherwise `exact`.
    """

    created_at: datetime

    mode: Literal["web"]
    """Always `web`. Optional."""

    name: str

    schedule: DataSchedule
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    status: Literal["active", "paused", "failed"]
    """Current state.

    Failed monitors keep running; paused monitors must be resumed with
    `status: "active"`.
    """

    target: DataTarget
    """What to watch: a page, a sitemap, or data extracted from a site."""

    updated_at: datetime

    baseline: Optional[DataBaseline] = None
    """Comparison baseline, included on Retrieve.

    Null until capture completes or after target changes.
    """

    last_change_at: Optional[datetime] = None

    last_error: Optional[DataLastError] = None
    """Error from the most recent failed run; null when the last run succeeded."""

    last_run_at: Optional[datetime] = None

    next_run_at: Optional[datetime] = None
    """When the next scheduled run is due; null while paused."""

    tags: Optional[List[str]] = None
    """Labels for filtering monitors, their changes, and their usage."""

    webhook: Optional[DataWebhook] = None
    """Webhook destination and delivery settings. Null means no webhook is configured."""

    webhook_failure: Optional[DataWebhookFailure] = None
    """
    Present while webhook deliveries are failing consecutively; null when deliveries
    are healthy or no webhook is configured. Cleared on the next successful delivery
    and when the webhook URL changes.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class MonitorListResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
