# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .retry_config_param import RetryConfigParam

__all__ = [
    "MonitorCreateParams",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Schedule",
    "Webhook",
]


class MonitorCreateParams(TypedDict, total=False):
    name: Required[str]
    """Display name for the monitor."""

    target: Required[Target]
    """What to watch: a page, a sitemap, or data extracted from a site."""

    change_detection: ChangeDetection
    """How changes are judged.

    Defaults to `semantic` for extract targets and page targets with `instructions`,
    otherwise `exact`.
    """

    mode: Literal["web"]
    """Always `web`. Optional."""

    schedule: Schedule
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering monitors, their changes, and their usage."""

    webhook: Optional[Webhook]
    """Webhook destination and delivery settings. Null means no webhook is configured."""


class TargetMonitorsPageTarget(TypedDict, total=False):
    """Watch a single web page.

    Exact detection reports visible-text diffs; semantic detection judges confirmed stable diffs against `instructions`.
    """

    type: Required[Literal["page"]]
    """Use `page` to watch one web page."""

    url: Required[str]
    """Public HTTP(S) page URL to monitor."""

    exclude_selectors: SequenceNotStr[str]
    """Remove matching regions after inclusions. Changes create a new baseline."""

    include_selectors: SequenceNotStr[str]
    """Monitor these CSS-selected regions.

    Empty or omitted uses main content. Changes create a new baseline.
    """

    instructions: str
    """Plain-language goal describing which page changes matter.

    When provided without change_detection, semantic detection is inferred.
    """

    normalize_whitespace: bool
    """Normalize whitespace before comparing or analyzing text."""


class TargetMonitorsSitemapTarget(TypedDict, total=False):
    """Watch a site’s URL inventory for confirmed additions and removals."""

    type: Required[Literal["sitemap"]]
    """Use `sitemap` to watch a site for added or removed URLs."""

    url: Required[str]
    """Sitemap URL to monitor."""

    exclude: SequenceNotStr[str]
    """URL path patterns to exclude (max 50)."""

    include: SequenceNotStr[str]
    """URL path patterns to include (max 50)."""

    max_urls: int
    """Maximum number of sitemap URLs to track (capped at 10,000)."""


class TargetMonitorsExtractTarget(TypedDict, total=False):
    """
    Track relevant pages selected by `schema` and `instructions`; refresh the page set periodically.
    """

    instructions: Required[str]
    """
    Natural-language instructions guiding which pages and facts to track and which
    changes to report.
    """

    type: Required[Literal["extract"]]
    """Use `extract` to watch structured data across selected pages."""

    url: Required[str]
    """Root URL to extract structured data from."""

    follow_subdomains: bool
    """Allow page discovery on subdomains of the target site."""

    max_depth: int
    """Optional maximum link depth from the starting URL (0 = only the starting page)."""

    max_pages: int
    """Maximum number of pages to track."""

    schema: Dict[str, object]
    """JSON Schema for page selection and the baseline snapshot.

    Changes return diffs and evidence.
    """


Target: TypeAlias = Union[TargetMonitorsPageTarget, TargetMonitorsSitemapTarget, TargetMonitorsExtractTarget]


class ChangeDetectionMonitorsExactChangeDetection(TypedDict, total=False):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Required[Literal["exact"]]
    """Use `exact` to compare visible text or sitemap URLs."""


class ChangeDetectionMonitorsSemanticChangeDetection(TypedDict, total=False):
    """
    Detect meaningful content changes using the target’s instructions and optional schema.
    """

    type: Required[Literal["semantic"]]
    """Use `semantic` to judge changes against the target instructions."""

    confidence_threshold: float
    """Minimum confidence required to report a meaningful change, from 0 to 1."""


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
    """Use `interval` to run on a repeating schedule."""

    unit: Required[Literal["minutes", "hours", "days"]]
    """Time unit used with `frequency` to set the run interval."""


class Webhook(TypedDict, total=False):
    """Webhook destination and delivery settings. Null means no webhook is configured."""

    url: Required[str]
    """Public HTTP(S) URL that receives events.

    Slack and GovSlack URLs get formatted messages.
    """

    events: List[Literal["change.detected", "run.completed"]]
    """Events to deliver.

    Defaults to `change.detected`; `run.completed` also includes unchanged runs.
    """

    retry: RetryConfigParam
    """Webhook retry settings. Use {} for the default schedule."""
