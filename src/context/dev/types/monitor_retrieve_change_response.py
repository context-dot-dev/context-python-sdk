# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MonitorRetrieveChangeResponse",
    "MonitorsPageExactChange",
    "MonitorsSitemapExactChange",
    "MonitorsPageSemanticChange",
    "MonitorsPageSemanticChangeEvidence",
    "MonitorsExtractSemanticChange",
    "MonitorsExtractSemanticChangeEvidence",
]


class MonitorsPageExactChange(BaseModel):
    id: str

    change_detection_type: Literal["exact"]

    detected_at: datetime

    diff: str
    """Text diff between the previous and current page baseline."""

    monitor_id: str

    summary: str

    target_type: Literal["page"]

    title: str

    url: str

    after_text_excerpt: Optional[str] = None

    before_text_excerpt: Optional[str] = None

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class MonitorsSitemapExactChange(BaseModel):
    id: str

    added_url_count: int

    added_urls: List[str]

    change_detection_type: Literal["exact"]

    detected_at: datetime

    monitor_id: str

    removed_url_count: int

    removed_urls: List[str]

    summary: str

    target_type: Literal["sitemap"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class MonitorsPageSemanticChangeEvidence(BaseModel):
    after: str

    before: str


class MonitorsPageSemanticChange(BaseModel):
    id: str

    change_detection_type: Literal["semantic"]

    confidence: float

    detected_at: datetime

    evidence: List[MonitorsPageSemanticChangeEvidence]

    importance: Literal["low", "medium", "high"]

    monitor_id: str

    query: str

    summary: str

    target_type: Literal["page"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class MonitorsExtractSemanticChangeEvidence(BaseModel):
    after: str
    """Snapshot of the extracted data after the change."""

    before: str
    """Snapshot of the extracted data before the change."""

    url: Optional[str] = None
    """Optional URL the evidence relates to. Absent for whole-target extract diffs."""


class MonitorsExtractSemanticChange(BaseModel):
    id: str

    change_detection_type: Literal["semantic"]

    confidence: float

    detected_at: datetime

    evidence: List[MonitorsExtractSemanticChangeEvidence]

    importance: Literal["low", "medium", "high"]

    matched_url_count: int

    matched_urls: List[str]

    monitor_id: str

    query: str

    summary: str

    target_type: Literal["extract"]

    title: str

    url: str
    """Root URL of the extract target."""

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


MonitorRetrieveChangeResponse: TypeAlias = Union[
    MonitorsPageExactChange, MonitorsSitemapExactChange, MonitorsPageSemanticChange, MonitorsExtractSemanticChange
]
