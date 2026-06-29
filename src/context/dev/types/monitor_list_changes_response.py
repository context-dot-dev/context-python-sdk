# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = [
    "MonitorListChangesResponse",
    "Data",
    "DataMonitorsPageExactChangeSummary",
    "DataMonitorsSitemapExactChangeSummary",
    "DataMonitorsPageSemanticChangeSummary",
    "DataMonitorsExtractSemanticChangeSummary",
]


class DataMonitorsPageExactChangeSummary(BaseModel):
    id: str

    change_detection_type: Literal["exact"]

    detected_at: datetime

    monitor_id: str

    summary: str

    target_type: Literal["page"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class DataMonitorsSitemapExactChangeSummary(BaseModel):
    id: str

    added_url_count: int

    change_detection_type: Literal["exact"]

    detected_at: datetime

    monitor_id: str

    removed_url_count: int

    summary: str

    target_type: Literal["sitemap"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class DataMonitorsPageSemanticChangeSummary(BaseModel):
    id: str

    change_detection_type: Literal["semantic"]

    confidence: float

    detected_at: datetime

    importance: Literal["low", "medium", "high"]

    monitor_id: str

    summary: str

    target_type: Literal["page"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


class DataMonitorsExtractSemanticChangeSummary(BaseModel):
    id: str

    change_detection_type: Literal["semantic"]

    confidence: float

    detected_at: datetime

    importance: Literal["low", "medium", "high"]

    matched_url_count: int

    monitor_id: str

    summary: str

    target_type: Literal["extract"]

    title: str

    url: str

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes."""


Data: TypeAlias = Union[
    DataMonitorsPageExactChangeSummary,
    DataMonitorsSitemapExactChangeSummary,
    DataMonitorsPageSemanticChangeSummary,
    DataMonitorsExtractSemanticChangeSummary,
]


class MonitorListChangesResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
