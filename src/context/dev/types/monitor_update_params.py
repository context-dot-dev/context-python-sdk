# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .retry_config_param import RetryConfigParam

__all__ = [
    "MonitorUpdateParams",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Schedule",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "Webhook",
]


class MonitorUpdateParams(TypedDict, total=False):
    change_detection: ChangeDetection
    """Discriminated union describing how changes are detected."""

    name: str

    schedule: Schedule
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    status: Literal["active", "paused"]

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes.

    Duplicates are removed.
    """

    target: Target
    """Discriminated union describing what the monitor watches."""

    webhook: Optional[Webhook]
    """Set to null to remove the webhook."""


class ChangeDetectionMonitorsExactChangeDetection(TypedDict, total=False):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Required[Literal["exact"]]


class ChangeDetectionMonitorsSemanticChangeDetection(TypedDict, total=False):
    """
    Detect meaning-level changes to page content, ignoring cosmetic or instruction-irrelevant differences. Which changes are meaningful is judged against the page or extract target's `instructions` (and an extract target's `schema`, when provided).
    """

    type: Required[Literal["semantic"]]

    confidence_threshold: float


ChangeDetection: TypeAlias = Union[
    ChangeDetectionMonitorsExactChangeDetection, ChangeDetectionMonitorsSemanticChangeDetection
]


class Schedule(TypedDict, total=False):
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be between 10 minutes and 1 year.
    """

    frequency: Required[int]
    """Number of units between runs.

    The resulting interval (frequency × unit) must be at least 10 minutes and at
    most 1 year (e.g. minimum 10 when unit is minutes; maximum 365 when unit is
    days).
    """

    type: Required[Literal["interval"]]

    unit: Required[Literal["minutes", "hours", "days"]]


class TargetMonitorsPageTarget(TypedDict, total=False):
    """Watch a single web page.

    Exact detection reports visible-text diffs; semantic detection judges confirmed stable diffs against `instructions`.
    """

    type: Required[Literal["page"]]

    url: Required[str]

    instructions: str
    """Plain-language goal describing which page changes matter.

    When provided without change_detection, semantic detection is inferred.
    """

    normalize_whitespace: bool
    """Normalize whitespace before comparing or analyzing text."""


class TargetMonitorsSitemapTarget(TypedDict, total=False):
    """Watch a sitemap for URL additions and removals.

    Crawled URLs are normalized (lowercased host, no trailing slash/fragment) and scoped to the monitored site and its subdomains before comparison. On a detected difference the sitemap is re-fetched within the same run and only URLs both observations agree on are reported, suppressing transient crawl flaps.
    """

    type: Required[Literal["sitemap"]]

    url: Required[str]
    """Sitemap URL to monitor."""

    exclude: SequenceNotStr[str]
    """URL path patterns to exclude (max 50)."""

    include: SequenceNotStr[str]
    """URL path patterns to include (max 50)."""

    max_urls: int
    """Maximum number of sitemap URLs to track (capped at 10,000)."""


class TargetMonitorsExtractTarget(TypedDict, total=False):
    """Watch the monitor-relevant pages of a site for meaningful changes.

    A crawl guided by `schema`/`instructions` selects up to `max_pages` relevant pages to track; each run re-checks exactly those pages, and confirmed content changes are judged for relevance against the monitor's `instructions` (and `schema`, when provided). The tracked page set is refreshed by a periodic re-discovery crawl.
    """

    instructions: Required[str]
    """
    Natural-language instructions guiding which pages and facts to track and which
    changes to report.
    """

    type: Required[Literal["extract"]]

    url: Required[str]
    """Root URL to extract structured data from."""

    follow_subdomains: bool

    max_depth: int
    """Optional maximum link depth from the starting URL (0 = only the starting page)."""

    max_pages: int
    """Maximum number of pages to track."""

    schema: Dict[str, object]
    """JSON Schema describing the data you care about.

    It is used three ways: it guides which pages are selected for tracking, it gives
    the change judge extra context on which changes matter (alongside
    `instructions`), and it defines the shape of the baseline `data` snapshot on GET
    /monitors/{monitor_id} (refreshed at most about once a day). It is not a
    response format for changes: change events and webhook payloads always contain
    diffs, summaries, and evidence excerpts — never data in this schema's shape. If
    omitted, a default summary + key-points schema is used.
    """


Target: TypeAlias = Union[TargetMonitorsPageTarget, TargetMonitorsSitemapTarget, TargetMonitorsExtractTarget]


class Webhook(TypedDict, total=False):
    """Set to null to remove the webhook."""

    url: Required[str]
    """Webhook URL events are delivered to."""

    events: List[Literal["change.detected", "run.completed"]]
    """Events delivered to this endpoint.

    `change.detected` fires only when a run detects a change; `run.completed` fires
    on every completed run — including runs that detected no change — and embeds the
    change when one was detected. Defaults to `["change.detected"]` when omitted.
    """

    retry: RetryConfigParam
    """Webhook retry settings. Use {} for the default schedule."""
