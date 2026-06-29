# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorListRunsResponse", "Data", "DataError"]


class DataError(BaseModel):
    code: str

    message: str


class Data(BaseModel):
    id: str

    baseline_created: bool
    """
    True when this run established the monitor's initial baseline; baseline runs
    perform no change detection.
    """

    change_detected: bool

    change_detection_type: Literal["exact", "semantic"]

    monitor_id: str

    run_type: Literal["baseline", "scheduled"]
    """The first run after monitor creation is a baseline run."""

    status: Literal["queued", "running", "completed", "failed"]

    target_type: Literal["page", "sitemap", "extract"]

    change_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    error: Optional[DataError] = None

    started_at: Optional[datetime] = None


class MonitorListRunsResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
