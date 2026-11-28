# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorListAccountChangesResponse", "Data", "DataEvidence", "KeyMetadata"]


class DataEvidence(BaseModel):
    """Before and after excerpts that support a change."""

    after: str
    """Content after the change."""

    before: str
    """Content before the change. Empty for new search results."""

    url: Optional[str] = None
    """Page the evidence comes from.

    Omitted when the evidence covers the whole target.
    """


class Data(BaseModel):
    """
    A change detected by a monitor run, with a summary and, depending on the target, a text diff, added or removed URLs, matched results, and evidence.
    """

    id: str
    """Unique ID of the change."""

    change_detection_type: Literal["exact", "semantic"]
    """Change detection type the monitor uses."""

    detected_at: datetime
    """When the change was detected."""

    mode: Literal["web"]
    """Monitor category. Always `web`."""

    monitor_id: str
    """ID of the monitor that detected the change."""

    run_id: str
    """ID of the run that detected the change."""

    summary: str
    """Plain-language summary of what changed."""

    tags: List[str]
    """Tags the monitor had when the change was detected."""

    target_type: Literal["page", "sitemap", "extract", "search"]
    """Type of target the monitor watches."""

    title: str
    """Short headline for the change."""

    url: str
    """Monitored URL. For search targets, the first new result."""

    added_url_count: Optional[int] = None
    """Total number of URLs added."""

    added_urls: Optional[List[str]] = None
    """URLs added to the sitemap, up to 500. `added_url_count` has the full count."""

    after_text_excerpt: Optional[str] = None
    """Excerpt of the page text after the change. Page targets only."""

    before_text_excerpt: Optional[str] = None
    """Excerpt of the page text before the change. Page targets only."""

    confidence: Optional[float] = None
    """Confidence that the change matters, from 0 to 1.

    Set by `semantic` detection only.
    """

    diff: Optional[str] = None
    """Text diff of the change, for page and extract targets.

    Extract diffs have one section per changed page.
    """

    evidence: Optional[List[DataEvidence]] = None
    """Before and after excerpts that support the change."""

    importance: Optional[Literal["low", "medium", "high"]] = None
    """How important the change is. Set by `semantic` detection only."""

    matched_url_count: Optional[int] = None
    """Total number of matched URLs."""

    matched_urls: Optional[List[str]] = None
    """
    URLs where the change was found: the changed pages for page and extract targets,
    or the new results for search targets. Up to 500; `matched_url_count` has the
    full count.
    """

    removed_url_count: Optional[int] = None
    """Total number of URLs removed."""

    removed_urls: Optional[List[str]] = None
    """
    URLs removed from the sitemap, or pages no longer found for extract targets, up
    to 500. `removed_url_count` has the full count.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class MonitorListAccountChangesResponse(BaseModel):
    data: List[Data]
    """Changes on this page."""

    has_more: bool
    """Whether more results are available after this page."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. `null` on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
