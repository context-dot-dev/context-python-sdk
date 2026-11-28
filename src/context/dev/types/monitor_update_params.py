# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo
from .retry_config_param import RetryConfigParam

__all__ = [
    "MonitorUpdateParams",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Schedule",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsPageTargetAction",
    "TargetMonitorsPageTargetActionWebScrapeWaitAction",
    "TargetMonitorsPageTargetActionWebScrapePerformAction",
    "TargetMonitorsPageTargetActionWebScrapeScrollAction",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "TargetMonitorsSearchTarget",
    "Webhook",
]


class MonitorUpdateParams(TypedDict, total=False):
    change_detection: ChangeDetection
    """How changes are judged.

    Defaults to `semantic` for extract and search targets and for page targets with
    `instructions`; otherwise `exact`. Sitemap targets support only `exact`, and
    extract targets only `semantic`.
    """

    name: str
    """Display name for the monitor."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply to every run, or an empty list to remove them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    schedule: Schedule
    """Run the monitor at a fixed interval, such as every 6 hours or every 2 days.

    The interval must be between 10 minutes and 1 year.
    """

    status: Literal["active", "paused"]
    """Set `paused` to stop scheduled runs or `active` to resume them.

    A resumed monitor runs promptly instead of waiting a full interval.
    """

    tags: SequenceNotStr[str]
    """Labels for grouping monitors.

    Filter monitors, changes, and credit usage by tag.
    """

    target: Target
    """
    What to watch: a page, a sitemap, data extracted from a site, or web search
    results.
    """

    webhook: Optional[Webhook]
    """Set to `null` to remove the webhook. Changing `url` generates a new secret."""


class ChangeDetectionMonitorsExactChangeDetection(TypedDict, total=False):
    """
    Report every change: visible-text diffs for pages, added or removed URLs for sitemaps, and every new result for searches.
    """

    type: Required[Literal["exact"]]
    """Use `exact` to compare visible text, sitemap URLs, or search results."""


class ChangeDetectionMonitorsSemanticChangeDetection(TypedDict, total=False):
    """
    Report only changes that matter, judged against the target's `instructions` and, for extract targets, its `schema`.
    """

    type: Required[Literal["semantic"]]
    """Use `semantic` to report only changes that match the target's `instructions`."""

    confidence_threshold: float
    """Minimum confidence a change needs to be reported.

    Higher values mean fewer, more certain alerts.
    """


ChangeDetection: TypeAlias = Union[
    ChangeDetectionMonitorsExactChangeDetection, ChangeDetectionMonitorsSemanticChangeDetection
]


class Schedule(TypedDict, total=False):
    """Run the monitor at a fixed interval, such as every 6 hours or every 2 days.

    The interval must be between 10 minutes and 1 year.
    """

    frequency: Required[int]
    """Number of `unit` periods between runs.

    The interval must be between 10 minutes and 1 year, so at least `10` with
    `minutes` and at most `365` with `days`.
    """

    type: Required[Literal["interval"]]
    """Use `interval` to run on a repeating schedule."""

    unit: Required[Literal["minutes", "hours", "days"]]
    """Time unit for `frequency`."""


class TargetMonitorsPageTargetActionWebScrapeWaitAction(TypedDict, total=False):
    """Pause for a fixed time before the next action."""

    do: Required[Literal["wait"]]
    """Use `wait` to pause for a fixed duration."""

    time_ms: Required[Annotated[int, PropertyInfo(alias="timeMs")]]
    """Time to pause in milliseconds before the next action."""


class TargetMonitorsPageTargetActionWebScrapePerformAction(TypedDict, total=False):
    """Perform one browser instruction written in plain language."""

    action: Required[str]
    """One browser instruction, such as clicking a button or entering text."""

    do: Required[Literal["perform"]]
    """Use `perform` for a plain-language browser instruction."""


class TargetMonitorsPageTargetActionWebScrapeScrollAction(TypedDict, total=False):
    """Scroll the page or a scrollable container.

    Waits for new content to settle after each scroll.
    """

    do: Required[Literal["scroll"]]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"]]
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    container: str
    """Scroll the first container matching this CSS selector. Omit to scroll the page."""

    direction: Literal["up", "down", "left", "right"]
    """Direction to scroll."""

    max_scrolls: Annotated[int, PropertyInfo(alias="maxScrolls")]
    """Maximum number of scroll steps. Stops early when the page stops changing."""


TargetMonitorsPageTargetAction: TypeAlias = Union[
    TargetMonitorsPageTargetActionWebScrapeWaitAction,
    TargetMonitorsPageTargetActionWebScrapePerformAction,
    TargetMonitorsPageTargetActionWebScrapeScrollAction,
]


class TargetMonitorsPageTarget(TypedDict, total=False):
    """Watch one web page.

    `exact` detection reports any change to the visible text; `semantic` detection reports only confirmed changes that match `instructions`.
    """

    type: Required[Literal["page"]]
    """Use `page` to watch one web page."""

    url: Required[str]
    """Public HTTP(S) URL of the page to watch."""

    actions: Optional[Iterable[TargetMonitorsPageTargetAction]]
    """Browser actions to run in order after the page loads and before each capture.

    Requires a paid plan. Changing it resets the baseline.
    """

    exclude_selectors: SequenceNotStr[str]
    """CSS selectors for regions to ignore, applied after `include_selectors`.

    Changing it resets the baseline.
    """

    include_selectors: SequenceNotStr[str]
    """CSS selectors for the regions to watch.

    Omit or leave empty to watch the main content. Changing it resets the baseline.
    """

    instructions: str
    """Plain-language description of the changes that matter.

    Requires `semantic` detection, which is selected when `change_detection` is
    omitted.
    """

    normalize_whitespace: bool
    """
    Collapse whitespace before comparing text, so spacing-only edits are not
    reported.
    """


class TargetMonitorsSitemapTarget(TypedDict, total=False):
    """Watch a sitemap and report URLs that are added or removed."""

    type: Required[Literal["sitemap"]]
    """Use `sitemap` to watch a site for added or removed URLs."""

    url: Required[str]
    """Public HTTP(S) URL of the sitemap to watch."""

    exclude: SequenceNotStr[str]
    """Path patterns of URLs to ignore, such as `/legal/*`."""

    include: SequenceNotStr[str]
    """Path patterns of URLs to track, such as `/blog/*`."""

    max_urls: int
    """Maximum number of URLs to track."""


class TargetMonitorsExtractTarget(TypedDict, total=False):
    """
    Extract structured data from the most relevant pages of a site and report meaningful changes. Pages are chosen from `schema` and `instructions`, and the page set is refreshed periodically.
    """

    instructions: Required[str]
    """
    Plain-language description of the pages and facts to track and the changes to
    report.
    """

    type: Required[Literal["extract"]]
    """Use `extract` to watch structured data across selected pages."""

    url: Required[str]
    """Public HTTP(S) URL where page discovery starts, usually the site home page."""

    follow_subdomains: bool
    """Also discover pages on subdomains of the site."""

    max_depth: int
    """Maximum link depth from `url`. `0` tracks only the starting page."""

    max_pages: int
    """Maximum number of pages to track."""

    schema: Dict[str, object]
    """
    JSON Schema for the data to extract, up to 20,000 characters; it also guides
    which pages are tracked. Defaults to a `summary` string and a `key_points` list.
    """


class TargetMonitorsSearchTarget(TypedDict, total=False):
    """
    Search the web on every run and report results not seen before, listed in the change's `matched_urls` and `evidence`. `semantic` detection reports only results about a new development that matches `instructions`; `exact` detection reports every new result.
    """

    query: Required[str]
    """Web search query to run on every check.

    Supports `site:`, `-site:`, and quoted phrases.
    """

    type: Required[Literal["search"]]
    """Use `search` to watch the web for new results about a topic."""

    instructions: str
    """Plain-language description of the new results that matter.

    Defaults to `query`. Not allowed with `exact` detection.
    """


Target: TypeAlias = Union[
    TargetMonitorsPageTarget, TargetMonitorsSitemapTarget, TargetMonitorsExtractTarget, TargetMonitorsSearchTarget
]


class Webhook(TypedDict, total=False):
    """Set to `null` to remove the webhook. Changing `url` generates a new secret."""

    url: Required[str]
    """Public HTTP(S) URL that receives events.

    Slack and GovSlack webhook URLs get formatted messages.
    """

    events: List[Literal["change.detected", "run.completed"]]
    """Events to send.

    Defaults to `change.detected`. Add `run.completed` to get a delivery after every
    completed run, including runs with no change.
    """

    retry: RetryConfigParam
    """Automatic retry settings. Pass `{}` for the default schedule."""
