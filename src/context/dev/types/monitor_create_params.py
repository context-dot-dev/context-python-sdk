# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Union, Optional
from typing_extensions import Literal, Required, TypeAlias, TypedDict

from .._types import SequenceNotStr

__all__ = [
    "MonitorCreateParams",
    "MonitorsCreatePageExactMonitorRequest",
    "MonitorsCreatePageExactMonitorRequestChangeDetection",
    "MonitorsCreatePageExactMonitorRequestSchedule",
    "MonitorsCreatePageExactMonitorRequestTarget",
    "MonitorsCreatePageExactMonitorRequestWebhook",
    "MonitorsCreateSitemapExactMonitorRequest",
    "MonitorsCreateSitemapExactMonitorRequestChangeDetection",
    "MonitorsCreateSitemapExactMonitorRequestSchedule",
    "MonitorsCreateSitemapExactMonitorRequestTarget",
    "MonitorsCreateSitemapExactMonitorRequestWebhook",
    "MonitorsCreatePageSemanticMonitorRequest",
    "MonitorsCreatePageSemanticMonitorRequestChangeDetection",
    "MonitorsCreatePageSemanticMonitorRequestSchedule",
    "MonitorsCreatePageSemanticMonitorRequestTarget",
    "MonitorsCreatePageSemanticMonitorRequestWebhook",
    "MonitorsCreateExtractSemanticMonitorRequest",
    "MonitorsCreateExtractSemanticMonitorRequestChangeDetection",
    "MonitorsCreateExtractSemanticMonitorRequestSchedule",
    "MonitorsCreateExtractSemanticMonitorRequestTarget",
    "MonitorsCreateExtractSemanticMonitorRequestWebhook",
]


class MonitorsCreatePageExactMonitorRequest(TypedDict, total=False):
    change_detection: Required[MonitorsCreatePageExactMonitorRequestChangeDetection]
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means
    URL additions and removals.
    """

    name: Required[str]

    schedule: Required[MonitorsCreatePageExactMonitorRequestSchedule]
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    target: Required[MonitorsCreatePageExactMonitorRequestTarget]

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes."""

    webhook: Optional[MonitorsCreatePageExactMonitorRequestWebhook]


class MonitorsCreatePageExactMonitorRequestChangeDetection(TypedDict, total=False):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Required[Literal["exact"]]


class MonitorsCreatePageExactMonitorRequestSchedule(TypedDict, total=False):
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


class MonitorsCreatePageExactMonitorRequestTarget(TypedDict, total=False):
    type: Required[Literal["page"]]

    url: Required[str]

    normalize_whitespace: bool
    """Normalize whitespace before comparing or analyzing text."""


class MonitorsCreatePageExactMonitorRequestWebhook(TypedDict, total=False):
    url: Required[str]
    """Webhook URL called when a change is detected."""


class MonitorsCreateSitemapExactMonitorRequest(TypedDict, total=False):
    change_detection: Required[MonitorsCreateSitemapExactMonitorRequestChangeDetection]
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means
    URL additions and removals.
    """

    name: Required[str]

    schedule: Required[MonitorsCreateSitemapExactMonitorRequestSchedule]
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    target: Required[MonitorsCreateSitemapExactMonitorRequestTarget]

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes."""

    webhook: Optional[MonitorsCreateSitemapExactMonitorRequestWebhook]


class MonitorsCreateSitemapExactMonitorRequestChangeDetection(TypedDict, total=False):
    """Detect exact changes.

    For page targets, this means visible text diffs. For sitemap targets, this means URL additions and removals.
    """

    type: Required[Literal["exact"]]


class MonitorsCreateSitemapExactMonitorRequestSchedule(TypedDict, total=False):
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


class MonitorsCreateSitemapExactMonitorRequestTarget(TypedDict, total=False):
    type: Required[Literal["sitemap"]]

    url: Required[str]
    """Sitemap URL to monitor."""

    exclude: SequenceNotStr[str]
    """URL path patterns to exclude."""

    include: SequenceNotStr[str]
    """URL path patterns to include."""

    max_urls: int


class MonitorsCreateSitemapExactMonitorRequestWebhook(TypedDict, total=False):
    url: Required[str]
    """Webhook URL called when a change is detected."""


class MonitorsCreatePageSemanticMonitorRequest(TypedDict, total=False):
    change_detection: Required[MonitorsCreatePageSemanticMonitorRequestChangeDetection]
    """Detect meaning-level changes that match a natural language query."""

    name: Required[str]

    schedule: Required[MonitorsCreatePageSemanticMonitorRequestSchedule]
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    target: Required[MonitorsCreatePageSemanticMonitorRequestTarget]

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes."""

    webhook: Optional[MonitorsCreatePageSemanticMonitorRequestWebhook]


class MonitorsCreatePageSemanticMonitorRequestChangeDetection(TypedDict, total=False):
    """Detect meaning-level changes that match a natural language query."""

    query: Required[str]

    type: Required[Literal["semantic"]]

    confidence_threshold: float


class MonitorsCreatePageSemanticMonitorRequestSchedule(TypedDict, total=False):
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


class MonitorsCreatePageSemanticMonitorRequestTarget(TypedDict, total=False):
    type: Required[Literal["page"]]

    url: Required[str]

    normalize_whitespace: bool
    """Normalize whitespace before comparing or analyzing text."""


class MonitorsCreatePageSemanticMonitorRequestWebhook(TypedDict, total=False):
    url: Required[str]
    """Webhook URL called when a change is detected."""


class MonitorsCreateExtractSemanticMonitorRequest(TypedDict, total=False):
    change_detection: Required[MonitorsCreateExtractSemanticMonitorRequestChangeDetection]
    """Detect meaning-level changes that match a natural language query."""

    name: Required[str]

    schedule: Required[MonitorsCreateExtractSemanticMonitorRequestSchedule]
    """Run the monitor on a fixed interval defined by a frequency and a unit, e.g.

    every 6 hours or every 2 days. The total interval (frequency × unit) must be
    between 10 minutes and 1 year.
    """

    target: Required[MonitorsCreateExtractSemanticMonitorRequestTarget]

    tags: SequenceNotStr[str]
    """User-defined tags for grouping and filtering monitors and their changes."""

    webhook: Optional[MonitorsCreateExtractSemanticMonitorRequestWebhook]


class MonitorsCreateExtractSemanticMonitorRequestChangeDetection(TypedDict, total=False):
    """Detect meaning-level changes that match a natural language query."""

    query: Required[str]

    type: Required[Literal["semantic"]]

    confidence_threshold: float


class MonitorsCreateExtractSemanticMonitorRequestSchedule(TypedDict, total=False):
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


class MonitorsCreateExtractSemanticMonitorRequestTarget(TypedDict, total=False):
    type: Required[Literal["extract"]]

    url: Required[str]
    """Root URL to extract structured data from."""

    follow_subdomains: bool

    instructions: str
    """Optional natural-language instructions guiding what to extract."""

    max_depth: int
    """Optional maximum link depth from the starting URL (0 = only the starting page)."""

    max_pages: int
    """Maximum number of pages to analyze during extraction."""

    schema: Dict[str, object]
    """JSON Schema describing the structured data to extract and watch for changes.

    If omitted, a default summary + key-points schema is used.
    """


class MonitorsCreateExtractSemanticMonitorRequestWebhook(TypedDict, total=False):
    url: Required[str]
    """Webhook URL called when a change is detected."""


MonitorCreateParams: TypeAlias = Union[
    MonitorsCreatePageExactMonitorRequest,
    MonitorsCreateSitemapExactMonitorRequest,
    MonitorsCreatePageSemanticMonitorRequest,
    MonitorsCreateExtractSemanticMonitorRequest,
]
