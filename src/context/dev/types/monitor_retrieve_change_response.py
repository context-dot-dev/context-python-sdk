# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorRetrieveChangeResponse", "Evidence"]


class Evidence(BaseModel):
    after: str
    """Snapshot of the content after the change."""

    before: str
    """Snapshot of the content before the change."""

    url: Optional[str] = None
    """Optional URL the evidence relates to. Absent for whole-target diffs."""


class MonitorRetrieveChangeResponse(BaseModel):
    """A detected change.

    `mode` is the constant `web`; `target_type` and `change_detection_type` describe the change, and which optional fields are present depends on them (page: `diff` + excerpts; sitemap: `added_urls`/`removed_urls`; semantic: `query`/`confidence`/`importance`/`evidence`/`matched_urls`).
    """

    id: str

    change_detection_type: Literal["exact", "semantic"]

    detected_at: datetime

    mode: Literal["web"]
    """Top-level monitor category.

    Always `web` today; the concrete behavior is described by `target` and
    `change_detection`.
    """

    monitor_id: str

    run_id: str
    """The run that detected this change."""

    summary: str

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

    matched_url_count: Optional[int] = None

    matched_urls: Optional[List[str]] = None
    """At most 500 URLs are included; the corresponding count field is always exact."""

    removed_url_count: Optional[int] = None

    removed_urls: Optional[List[str]] = None
    """At most 500 URLs are included; the corresponding count field is always exact."""

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""
