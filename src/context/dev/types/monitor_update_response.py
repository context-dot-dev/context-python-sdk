# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from .._utils import PropertyInfo
from .._models import BaseModel
from .retry_config import RetryConfig

__all__ = [
    "MonitorUpdateResponse",
    "ChangeDetection",
    "ChangeDetectionMonitorsExactChangeDetection",
    "ChangeDetectionMonitorsSemanticChangeDetection",
    "Target",
    "TargetMonitorsPageTarget",
    "TargetMonitorsPageTargetAction",
    "TargetMonitorsPageTargetActionWebScrapeWaitAction",
    "TargetMonitorsPageTargetActionWebScrapePerformAction",
    "TargetMonitorsPageTargetActionWebScrapeScrollAction",
    "TargetMonitorsSitemapTarget",
    "TargetMonitorsExtractTarget",
    "TargetMonitorsSearchTarget",
    "Baseline",
    "BaselineMonitorsPageBaseline",
    "BaselineMonitorsSitemapBaseline",
    "BaselineMonitorsExtractBaseline",
    "BaselineMonitorsSearchBaseline",
    "BaselineMonitorsSearchBaselineResult",
    "KeyMetadata",
    "LastError",
    "Schedule",
    "Webhook",
    "WebhookFailure",
]


class ChangeDetectionMonitorsExactChangeDetection(BaseModel):
    """
    Report every change: visible-text diffs for pages, added or removed URLs for sitemaps, and every new result for searches.
    """

    type: Literal["exact"]
    """Use `exact` to compare visible text, sitemap URLs, or search results."""


class ChangeDetectionMonitorsSemanticChangeDetection(BaseModel):
    """
    Report only changes that matter, judged against the target's `instructions` and, for extract targets, its `schema`.
    """

    type: Literal["semantic"]
    """Use `semantic` to report only changes that match the target's `instructions`."""

    confidence_threshold: Optional[float] = None
    """Minimum confidence a change needs to be reported.

    Higher values mean fewer, more certain alerts.
    """


ChangeDetection: TypeAlias = Annotated[
    Union[ChangeDetectionMonitorsExactChangeDetection, ChangeDetectionMonitorsSemanticChangeDetection],
    PropertyInfo(discriminator="type"),
]


class TargetMonitorsPageTargetActionWebScrapeWaitAction(BaseModel):
    """Pause for a fixed time before the next action."""

    do: Literal["wait"]
    """Use `wait` to pause for a fixed duration."""

    time_ms: int = FieldInfo(alias="timeMs")
    """Time to pause in milliseconds before the next action."""


class TargetMonitorsPageTargetActionWebScrapePerformAction(BaseModel):
    """Perform one browser instruction written in plain language."""

    action: str
    """One browser instruction, such as clicking a button or entering text."""

    do: Literal["perform"]
    """Use `perform` for a plain-language browser instruction."""


class TargetMonitorsPageTargetActionWebScrapeScrollAction(BaseModel):
    """Scroll the page or a scrollable container.

    Waits for new content to settle after each scroll.
    """

    do: Literal["scroll"]
    """Use `scroll` to move through the page or a container."""

    amount: Union[int, Literal["viewport", "max"], None] = None
    """Distance per scroll: pixels, one `viewport`, or `max` to reach the end."""

    container: Optional[str] = None
    """Scroll the first container matching this CSS selector. Omit to scroll the page."""

    direction: Optional[Literal["up", "down", "left", "right"]] = None
    """Direction to scroll."""

    max_scrolls: Optional[int] = FieldInfo(alias="maxScrolls", default=None)
    """Maximum number of scroll steps. Stops early when the page stops changing."""


TargetMonitorsPageTargetAction: TypeAlias = Annotated[
    Union[
        TargetMonitorsPageTargetActionWebScrapeWaitAction,
        TargetMonitorsPageTargetActionWebScrapePerformAction,
        TargetMonitorsPageTargetActionWebScrapeScrollAction,
    ],
    PropertyInfo(discriminator="do"),
]


class TargetMonitorsPageTarget(BaseModel):
    """Watch one web page.

    `exact` detection reports any change to the visible text; `semantic` detection reports only confirmed changes that match `instructions`.
    """

    type: Literal["page"]
    """Use `page` to watch one web page."""

    url: str
    """Public HTTP(S) URL of the page to watch."""

    actions: Optional[List[TargetMonitorsPageTargetAction]] = None
    """Browser actions to run in order after the page loads and before each capture.

    Requires a paid plan. Changing it resets the baseline.
    """

    exclude_selectors: Optional[List[str]] = None
    """CSS selectors for regions to ignore, applied after `include_selectors`.

    Changing it resets the baseline.
    """

    include_selectors: Optional[List[str]] = None
    """CSS selectors for the regions to watch.

    Omit or leave empty to watch the main content. Changing it resets the baseline.
    """

    instructions: Optional[str] = None
    """Plain-language description of the changes that matter.

    Requires `semantic` detection, which is selected when `change_detection` is
    omitted.
    """

    normalize_whitespace: Optional[bool] = None
    """
    Collapse whitespace before comparing text, so spacing-only edits are not
    reported.
    """


class TargetMonitorsSitemapTarget(BaseModel):
    """Watch a sitemap and report URLs that are added or removed."""

    type: Literal["sitemap"]
    """Use `sitemap` to watch a site for added or removed URLs."""

    url: str
    """Public HTTP(S) URL of the sitemap to watch."""

    exclude: Optional[List[str]] = None
    """Path patterns of URLs to ignore, such as `/legal/*`."""

    include: Optional[List[str]] = None
    """Path patterns of URLs to track, such as `/blog/*`."""

    max_urls: Optional[int] = None
    """Maximum number of URLs to track."""


class TargetMonitorsExtractTarget(BaseModel):
    """
    Extract structured data from the most relevant pages of a site and report meaningful changes. Pages are chosen from `schema` and `instructions`, and the page set is refreshed periodically.
    """

    instructions: str
    """
    Plain-language description of the pages and facts to track and the changes to
    report.
    """

    type: Literal["extract"]
    """Use `extract` to watch structured data across selected pages."""

    url: str
    """Public HTTP(S) URL where page discovery starts, usually the site home page."""

    follow_subdomains: Optional[bool] = None
    """Also discover pages on subdomains of the site."""

    max_depth: Optional[int] = None
    """Maximum link depth from `url`. `0` tracks only the starting page."""

    max_pages: Optional[int] = None
    """Maximum number of pages to track."""

    schema_: Optional[Dict[str, object]] = FieldInfo(alias="schema", default=None)
    """
    JSON Schema for the data to extract, up to 20,000 characters; it also guides
    which pages are tracked. Defaults to a `summary` string and a `key_points` list.
    """


class TargetMonitorsSearchTarget(BaseModel):
    """
    Search the web on every run and report results not seen before, listed in the change's `matched_urls` and `evidence`. `semantic` detection reports only results about a new development that matches `instructions`; `exact` detection reports every new result.
    """

    query: str
    """Web search query to run on every check.

    Supports `site:`, `-site:`, and quoted phrases.
    """

    type: Literal["search"]
    """Use `search` to watch the web for new results about a topic."""

    instructions: Optional[str] = None
    """Plain-language description of the new results that matter.

    Defaults to `query`. Not allowed with `exact` detection.
    """


Target: TypeAlias = Annotated[
    Union[
        TargetMonitorsPageTarget, TargetMonitorsSitemapTarget, TargetMonitorsExtractTarget, TargetMonitorsSearchTarget
    ],
    PropertyInfo(discriminator="type"),
]


class BaselineMonitorsPageBaseline(BaseModel):
    """Baseline for a `page` target: the page's visible text from the last capture."""

    captured_at: datetime
    """When the baseline was last captured or updated."""

    text: str
    """Visible page text from the last capture."""


class BaselineMonitorsSitemapBaseline(BaseModel):
    """
    Baseline for a `sitemap` target: the normalized set of URLs from the last capture.
    """

    captured_at: datetime
    """When the baseline was last captured or updated."""

    url_count: int
    """Number of URLs in the baseline."""

    urls: List[str]
    """Normalized sitemap URLs from the last capture, sorted."""


class BaselineMonitorsExtractBaseline(BaseModel):
    """
    Baseline for an `extract` target: the tracked pages and the data last extracted from them.
    """

    captured_at: datetime
    """When the baseline was last captured or updated."""

    data: object
    """Latest extracted data, matching the target's `schema`.

    Refreshed at most once a day; `null` before the first capture.
    """

    urls_analyzed: List[str]
    """Pages the monitor tracks for changes."""


class BaselineMonitorsSearchBaselineResult(BaseModel):
    description: str
    """Result snippet."""

    published_at: Optional[datetime] = None
    """When the result was published. `null` when unknown."""

    title: str
    """Title of the result."""

    url: str
    """URL of the result."""


class BaselineMonitorsSearchBaseline(BaseModel):
    """Baseline for a `search` target: the results from the last capture."""

    captured_at: datetime
    """When the baseline was last captured or updated."""

    results: List[BaselineMonitorsSearchBaselineResult]
    """Search results from the last capture."""


Baseline: TypeAlias = Union[
    BaselineMonitorsPageBaseline,
    BaselineMonitorsSitemapBaseline,
    BaselineMonitorsExtractBaseline,
    BaselineMonitorsSearchBaseline,
    None,
]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class LastError(BaseModel):
    """Error from the most recent failed run. `null` when the last run succeeded."""

    code: str
    """Machine-readable error code, such as `fetch_failed`."""

    message: str
    """Human-readable explanation of the error."""


class Schedule(BaseModel):
    """Run the monitor at a fixed interval, such as every 6 hours or every 2 days.

    The interval must be between 10 minutes and 1 year.
    """

    frequency: int
    """Number of `unit` periods between runs.

    The interval must be between 10 minutes and 1 year, so at least `10` with
    `minutes` and at most `365` with `days`.
    """

    type: Literal["interval"]
    """Use `interval` to run on a repeating schedule."""

    unit: Literal["minutes", "hours", "days"]
    """Time unit for `frequency`."""


class Webhook(BaseModel):
    """Webhook that receives monitor events. `null` when no webhook is configured."""

    url: str
    """Public HTTP(S) URL that receives events.

    Slack and GovSlack webhook URLs get formatted messages.
    """

    events: Optional[List[Literal["change.detected", "run.completed"]]] = None
    """Events to send.

    Defaults to `change.detected`. Add `run.completed` to get a delivery after every
    completed run, including runs with no change.
    """

    retry: Optional[RetryConfig] = None
    """Automatic retry settings. Pass `{}` for the default schedule."""

    secret: Optional[str] = None
    """Signing secret for verifying deliveries, generated by Context.dev.

    Returned only to API keys with full access or the `monitors:write` permission.
    """


class WebhookFailure(BaseModel):
    """Details of failing webhook deliveries.

    `null` when deliveries succeed or no webhook is configured; cleared by the next successful delivery or a new webhook URL.
    """

    consecutive_failures: int
    """Number of failed delivery attempts in a row."""

    last_failed_at: datetime
    """When the most recent delivery failed."""

    last_message: str
    """Human-readable explanation of the most recent failure."""

    last_status: Literal["rejected", "failed", "skipped_unsafe_url"]
    """
    Outcome of the most recent failed delivery: `rejected` (non-2xx response),
    `failed` (no response), or `skipped_unsafe_url` (the URL isn't a safe public
    endpoint).
    """


class MonitorUpdateResponse(BaseModel):
    id: str
    """Unique ID of the monitor."""

    change_detection: ChangeDetection
    """How changes are judged.

    Defaults to `semantic` for extract and search targets and for page targets with
    `instructions`; otherwise `exact`. Sitemap targets support only `exact`, and
    extract targets only `semantic`.
    """

    created_at: datetime
    """When the monitor was created."""

    mode: Literal["web"]
    """Monitor category. Always `web`."""

    name: str
    """Display name of the monitor."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: Literal["active", "paused", "failed"]
    """`active` monitors run on schedule.

    `failed` monitors keep running after a failed run and return to `active` on the
    next success. `paused` monitors don't run until you set `status` to `active`;
    Context.dev also pauses monitors after repeated failures or credit shortfalls.
    """

    target: Target
    """
    What to watch: a page, a sitemap, data extracted from a site, or web search
    results.
    """

    updated_at: datetime
    """When the monitor was last updated."""

    baseline: Optional[Baseline] = None
    """What the next run compares against.

    Returned only by `GET /monitors/{monitor_id}`; `null` until the first capture
    finishes or after the target changes.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    last_change_at: Optional[datetime] = None
    """When the monitor last detected a change. `null` until it detects one."""

    last_error: Optional[LastError] = None
    """Error from the most recent failed run. `null` when the last run succeeded."""

    last_run_at: Optional[datetime] = None
    """When the most recent run ended. `null` until the first run ends."""

    next_run_at: Optional[datetime] = None
    """When the next scheduled run is due. `null` while paused."""

    policies: Optional[List[str]] = None
    """Access policy IDs applied to every run."""

    schedule: Optional[Schedule] = None
    """Run the monitor at a fixed interval, such as every 6 hours or every 2 days.

    The interval must be between 10 minutes and 1 year.
    """

    tags: Optional[List[str]] = None
    """Labels for grouping monitors.

    Filter monitors, changes, and credit usage by tag.
    """

    webhook: Optional[Webhook] = None
    """Webhook that receives monitor events. `null` when no webhook is configured."""

    webhook_failure: Optional[WebhookFailure] = None
    """Details of failing webhook deliveries.

    `null` when deliveries succeed or no webhook is configured; cleared by the next
    successful delivery or a new webhook URL.
    """
