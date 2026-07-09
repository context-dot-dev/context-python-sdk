# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "MonitorCreateParams",
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


class MonitorCreateParams(TypedDict, total=False):
    change_detection: Required[ChangeDetection]
    """Discriminated union describing how changes are detected."""

    name: Required[str]

    schedule: Required[Schedule]
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    target: Required[Target]
    """Discriminated union describing what the monitor watches."""

    mode: Literal["web"]
    """Top-level monitor category.

    Always `web` today; the concrete behavior is described by `target` and
    `change_detection`.
    """

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes."""

    webhook: Optional[Webhook]


class ChangeDetectionMonitorsExactChangeDetection(TypedDict, total=False):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Required[Literal["exact"]]


class ChangeDetectionMonitorsSemanticChangeDetection(TypedDict, total=False):
    """
    Detect meaning-level changes to tracked page content, ignoring cosmetic or paraphrase-only differences. Which changes are meaningful is judged against the extract target's `instructions` (and `schema`, when provided).
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
    """Watch a single web page."""

    type: Required[Literal["page"]]

    url: Required[str]

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
    """URL path patterns to exclude."""

    include: SequenceNotStr[str]
    """URL path patterns to include."""

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
    url: Required[str]
    """Webhook URL called when a change is detected."""
