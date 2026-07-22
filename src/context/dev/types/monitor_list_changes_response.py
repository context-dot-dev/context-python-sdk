# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorListChangesResponse", "Data"]


class Data(BaseModel):
    """A lightweight change summary.

    `mode` is the constant `web`; `target_type` and `change_detection_type` describe the change, and which optional fields are present depends on them (e.g. sitemap changes include `added_url_count`/`removed_url_count`; semantic changes include `confidence`/`importance`).
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

    summary: str

    target_type: Literal["page", "sitemap", "extract"]

    title: str

    url: str

    added_url_count: Optional[int] = None

    confidence: Optional[float] = None

    importance: Optional[Literal["low", "medium", "high"]] = None

    matched_url_count: Optional[int] = None

    removed_url_count: Optional[int] = None

    tags: Optional[List[str]] = None
    """User-defined tags for grouping and filtering monitors and their changes.

    Duplicates are removed.
    """


class MonitorListChangesResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
