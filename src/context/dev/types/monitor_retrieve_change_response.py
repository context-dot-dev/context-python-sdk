# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorRetrieveChangeResponse", "Evidence", "KeyMetadata"]


class Evidence(BaseModel):
    after: str
    """Snapshot of the content after the change."""

    before: str
    """Snapshot of the content before the change."""

    url: Optional[str] = None
    """Optional URL the evidence relates to. Absent for whole-target diffs."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class MonitorRetrieveChangeResponse(BaseModel):
    id: str

    change_detection_type: Literal["exact", "semantic"]

    detected_at: datetime

    mode: Literal["web"]
    """Always `web`. Optional."""

    monitor_id: str

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    run_id: str
    """The run that detected this change."""

    summary: str

    tags: List[str]
    """Labels for filtering monitors, their changes, and their usage."""

    target_type: Literal["page", "sitemap", "extract"]

    title: str

    url: str

    added_url_count: Optional[int] = None

    added_urls: Optional[List[str]] = None
    """At most 500 URLs are included; the corresponding count field is always exact."""

    after_text_excerpt: Optional[str] = None

    before_text_excerpt: Optional[str] = None

    confidence: Optional[float] = None

    diff: Optional[str] = None
    """Text diff between the previous and current page baseline (page targets)."""

    evidence: Optional[List[Evidence]] = None

    importance: Optional[Literal["low", "medium", "high"]] = None

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    matched_url_count: Optional[int] = None

    matched_urls: Optional[List[str]] = None
    """At most 500 URLs are included; the corresponding count field is always exact."""

    removed_url_count: Optional[int] = None

    removed_urls: Optional[List[str]] = None
    """At most 500 URLs are included; the corresponding count field is always exact."""
