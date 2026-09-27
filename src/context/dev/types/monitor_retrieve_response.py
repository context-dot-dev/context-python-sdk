# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .retry_config import RetryConfig

__all__ = [
    "MonitorRetrieveResponse",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "Baseline",
    "BaselineMonitorsPageBaseline",
    "BaselineMonitorsSitemapBaseline",
    "BaselineMonitorsExtractBaseline",
    "KeyMetadata",
    "LastError",
    "Schedule",
    "Webhook",
    "WebhookFailure",
]


class ChangeDetectionMonitorsExactChangeDetection(BaseModel):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Literal["exact"]
    """Use `exact` to compare visible text or sitemap URLs."""


class ChangeDetectionMonitorsSemanticChangeDetection(BaseModel):
    """
    Detect meaningful content changes using the target’s instructions and optional schema.
    """

    type: Literal["semantic"]
    """Use `semantic` to judge changes against the target instructions."""

    confidence_threshold: Optional[float] = None
    """Minimum confidence required to report a meaningful change, from 0 to 1."""


ChangeDetection: TypeAlias = Annotated[
    Union[ChangeDetectionMonitorsExactChangeDetection, ChangeDetectionMonitorsSemanticChangeDetection],
    PropertyInfo(discriminator="type"),
]


class TargetMonitorsPageTarget(BaseModel):
    """Watch a single web page.

    Exact detection reports visible-text diffs; semantic detection judges confirmed stable diffs against `instructions`.
    """

    type: Literal["page"]
    """Use `page` to watch one web page."""

    url: str
    """Public HTTP(S) page URL to monitor."""

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


class TargetMonitorsSitemapTarget(BaseModel):
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


class TargetMonitorsExtractTarget(BaseModel):
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


Target: TypeAlias = Annotated[
    Union[TargetMonitorsPageTarget, TargetMonitorsSitemapTarget, TargetMonitorsExtractTarget],
    PropertyInfo(discriminator="type"),
]


class BaselineMonitorsPageBaseline(BaseModel):
    """Current baseline of a `page` monitor: the visible page text as last observed."""

    captured_at: datetime
    """When this baseline was last captured or replaced."""

    text: str
    """The page's visible text as last observed."""


class BaselineMonitorsSitemapBaseline(BaseModel):
    """
    Current baseline of a `sitemap` monitor: the normalized URL set as last observed.
    """

    captured_at: datetime
    """When this baseline was last captured or replaced."""

    url_count: int
    """Number of URLs in the baseline."""

    urls: List[str]
    """The sitemap URLs as last observed (sorted, normalized)."""


class BaselineMonitorsExtractBaseline(BaseModel):
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


Baseline: TypeAlias = Union[
    BaselineMonitorsPageBaseline, BaselineMonitorsSitemapBaseline, BaselineMonitorsExtractBaseline, None
]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class LastError(BaseModel):
    """Error from the most recent failed run; null when the last run succeeded."""

    code: str

    message: str


class Schedule(BaseModel):
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


class Webhook(BaseModel):
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


class WebhookFailure(BaseModel):
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


class MonitorRetrieveResponse(BaseModel):
    id: str

    change_detection: ChangeDetection
    """How changes are judged.

    Defaults to `semantic` for extract targets and page targets with `instructions`,
    otherwise `exact`.
    """

    created_at: datetime

    mode: Literal["web"]
    """Always `web`. Optional."""

    name: str

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["active", "paused", "failed"]
    """Current state.

    Failed monitors keep running; paused monitors must be resumed with
    `status: "active"`.
    """

    target: Target
    """What to watch: a page, a sitemap, or data extracted from a site."""

    updated_at: datetime

    baseline: Optional[Baseline] = None
    """Comparison baseline, included on Retrieve.

    Null until capture completes or after target changes.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    last_change_at: Optional[datetime] = None

    last_error: Optional[LastError] = None
    """Error from the most recent failed run; null when the last run succeeded."""

    last_run_at: Optional[datetime] = None

    next_run_at: Optional[datetime] = None
    """When the next scheduled run is due; null while paused."""

    schedule: Optional[Schedule] = None
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    tags: Optional[List[str]] = None
    """Labels for filtering monitors, their changes, and their usage."""

    webhook: Optional[Webhook] = None
    """Webhook destination and delivery settings. Null means no webhook is configured."""

    webhook_failure: Optional[WebhookFailure] = None
    """
    Present while webhook deliveries are failing consecutively; null when deliveries
    are healthy or no webhook is configured. Cleared on the next successful delivery
    and when the webhook URL changes.
    """
