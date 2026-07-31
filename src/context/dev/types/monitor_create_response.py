# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "MonitorCreateResponse",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Schedule",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "Baseline",
    "BaselineMonitorsPageBaseline",
    "BaselineMonitorsSitemapBaseline",
    "BaselineMonitorsExtractBaseline",
    "LastError",
    "Webhook",
    "WebhookFailure",
]


class ChangeDetectionMonitorsExactChangeDetection(BaseModel):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Literal["exact"]


class ChangeDetectionMonitorsSemanticChangeDetection(BaseModel):
    """
    Detect meaning-level changes to page content, ignoring cosmetic or instruction-irrelevant differences. Which changes are meaningful is judged against the page or extract target's `instructions` (and an extract target's `schema`, when provided).
    """

    type: Literal["semantic"]

    confidence_threshold: Optional[float] = None


ChangeDetection: TypeAlias = Annotated[
    Union[ChangeDetectionMonitorsExactChangeDetection, ChangeDetectionMonitorsSemanticChangeDetection],
    PropertyInfo(discriminator="type"),
]


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

    unit: Literal["minutes", "hours", "days"]


class TargetMonitorsPageTarget(BaseModel):
    """Watch a single web page.

    Exact detection reports visible-text diffs; semantic detection judges confirmed stable diffs against `instructions`.
    """

    type: Literal["page"]

    url: str

    instructions: Optional[str] = None
    """Plain-language goal describing which page changes matter.

    When provided without change_detection, semantic detection is inferred.
    """

    normalize_whitespace: Optional[bool] = None
    """Normalize whitespace before comparing or analyzing text."""


class TargetMonitorsSitemapTarget(BaseModel):
    """Watch a sitemap for URL additions and removals.

    Crawled URLs are normalized (lowercased host, no trailing slash/fragment) and scoped to the monitored site and its subdomains before comparison. On a detected difference the sitemap is re-fetched within the same run and only URLs both observations agree on are reported, suppressing transient crawl flaps.
    """

    type: Literal["sitemap"]

    url: str
    """Sitemap URL to monitor."""

    exclude: Optional[List[str]] = None
    """URL path patterns to exclude (max 50)."""

    include: Optional[List[str]] = None
    """URL path patterns to include (max 50)."""

    max_urls: Optional[int] = None
    """Maximum number of sitemap URLs to track (capped at 10,000)."""


class TargetMonitorsExtractTarget(BaseModel):
    """Watch the monitor-relevant pages of a site for meaningful changes.

    A crawl guided by `schema`/`instructions` selects up to `max_pages` relevant pages to track; each run re-checks exactly those pages, and confirmed content changes are judged for relevance against the monitor's `instructions` (and `schema`, when provided). The tracked page set is refreshed by a periodic re-discovery crawl.
    """

    instructions: str
    """
    Natural-language instructions guiding which pages and facts to track and which
    changes to report.
    """

    type: Literal["extract"]

    url: str
    """Root URL to extract structured data from."""

    follow_subdomains: Optional[bool] = None

    max_depth: Optional[int] = None
    """Optional maximum link depth from the starting URL (0 = only the starting page)."""

    max_pages: Optional[int] = None
    """Maximum number of pages to track."""

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """JSON Schema describing the data you care about.

    It is used three ways: it guides which pages are selected for tracking, it gives
    the change judge extra context on which changes matter (alongside
    `instructions`), and it defines the shape of the baseline `data` snapshot on GET
    /monitors/{monitor_id} (refreshed at most about once a day). It is not a
    response format for changes: change events and webhook payloads always contain
    diffs, summaries, and evidence excerpts — never data in this schema's shape. If
    omitted, a default summary + key-points schema is used.
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
    The extracted structured data, matching the monitor's extraction schema (same
    shape as the /web/extract endpoint's `data`). Refreshed when the monitor
    re-discovers its page set (at most about once a day); `null` when no extraction
    has been captured yet.
    """

    urls_analyzed: List[str]
    """The page URLs the monitor tracks and analyzes for changes."""


Baseline: TypeAlias = Union[
    BaselineMonitorsPageBaseline, BaselineMonitorsSitemapBaseline, BaselineMonitorsExtractBaseline, None
]


class LastError(BaseModel):
    """Error from the most recent failed run; null when the last run succeeded."""

    code: str

    message: str


class Webhook(BaseModel):
    url: str
    """Webhook URL events are delivered to."""

    events: Optional[List[Literal["change.detected", "run.completed"]]] = None
    """Events delivered to this endpoint.

    `change.detected` fires only when a run detects a change; `run.completed` fires
    on every completed run — including runs that detected no change — and embeds the
    change when one was detected. Defaults to `["change.detected"]` when omitted.
    """

    secret: Optional[str] = None
    """Signing secret used to verify webhook authenticity.

    Each delivery includes an `X-Context-Signature: t=<unix>,v1=<hmac>` header,
    where the HMAC is SHA-256 over `"{t}.{rawRequestBody}"` keyed by this secret.
    Recompute it with a constant-time compare and reject stale timestamps to prevent
    replay. Generated by the API; cannot be set by clients.
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


class MonitorCreateResponse(BaseModel):
    """
    A newly created monitor plus `initial_run_id`, the id of the baseline run queued at creation.
    """

    id: str

    change_detection: ChangeDetection
    """Discriminated union describing how changes are detected."""

    created_at: datetime

    initial_run_id: Optional[str] = None
    """
    The baseline run queued by this create call, or null if it could not be queued
    immediately (in which case the baseline runs on the next scheduled tick). Poll
    GET /monitors/{monitor_id}/runs/{run_id}.
    """

    mode: Literal["web"]
    """Top-level monitor category.

    Always `web` today; the concrete behavior is described by `target` and
    `change_detection`.
    """

    name: str

    schedule: Schedule
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    status: Literal["active", "paused", "failed"]
    """Monitor lifecycle status.

    `failed` means the most recent run failed (see the monitor's `last_error`);
    failed monitors keep running on schedule and flip back to `active` on the next
    successful run. Monitors are auto-`paused` after repeated consecutive failures
    or insufficient-credit skips; resume by PATCHing status to `active`.
    """

    target: Target
    """Discriminated union describing what the monitor watches."""

    updated_at: datetime

    baseline: Optional[Baseline] = None
    """
    Current baseline: the last observed value the monitor compares new snapshots
    against. Its shape follows `target.type` (page/sitemap/extract). Only populated
    on GET /monitors/{monitor_id}; null until the first baseline run completes (and
    after a target or change_detection update, which resets the baseline).
    """

    last_change_at: Optional[datetime] = None

    last_error: Optional[LastError] = None
    """Error from the most recent failed run; null when the last run succeeded."""

    last_run_at: Optional[datetime] = None

    next_run_at: Optional[datetime] = None
    """When the next scheduled run is due."""

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes.

    Duplicates are removed.
    """

    webhook: Optional[Webhook] = None

    webhook_failure: Optional[WebhookFailure] = None
    """
    Present while webhook deliveries are failing consecutively; null when deliveries
    are healthy or no webhook is configured. Cleared on the next successful delivery
    and when the webhook URL changes.
    """
