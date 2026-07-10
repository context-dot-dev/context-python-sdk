# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorListAccountRunsResponse", "Data", "DataError", "DataWebhookDelivery", "DataWebhookDeliveryError"]


class DataError(BaseModel):
    code: str

    message: str


class DataWebhookDeliveryError(BaseModel):
    code: str

    message: str


class DataWebhookDelivery(BaseModel):
    """The webhook delivery attempted for a change detected by this run.

    Omitted when no webhook was attempted, including historical runs created before delivery tracking was added.
    """

    attempted_at: datetime

    error: Optional[DataWebhookDeliveryError] = None

    event_id: str
    """Identifier sent in the X-Context-Id header."""

    http_status: Optional[int] = None
    """
    The endpoint's final HTTP response status, or null when no response was
    received.
    """

    status: Literal["delivered", "rejected", "failed", "skipped_unsafe_url"]
    """Delivery outcome.

    delivered means any 2xx response; rejected means a non-2xx response; failed
    means no HTTP response was received; skipped_unsafe_url means the URL failed the
    public-endpoint safety check.
    """


class Data(BaseModel):
    id: str

    baseline_created: bool
    """
    True when this run established the monitor's initial baseline; baseline runs
    perform no change detection.
    """

    change_detected: bool

    change_detection_type: Literal["exact", "semantic"]

    credits_charged: int
    """Credits charged for this run (0 for skipped/failed runs)."""

    monitor_id: str

    run_type: Literal["baseline", "scheduled"]
    """The first run after monitor creation is a baseline run."""

    status: Literal["queued", "running", "completed", "failed", "skipped"]
    """Lifecycle status of a run.

    `skipped` runs never executed — see `skip_reason` (insufficient credits, monitor
    paused, or superseded by a concurrent run).
    """

    target_type: Literal["page", "sitemap", "extract"]

    change_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    error: Optional[DataError] = None

    skip_reason: Optional[Literal["insufficient_credits", "monitor_paused", "superseded"]] = None
    """Why a skipped run never executed; null unless status is `skipped`."""

    started_at: Optional[datetime] = None

    webhook_delivery: Optional[DataWebhookDelivery] = None
    """The webhook delivery attempted for a change detected by this run.

    Omitted when no webhook was attempted, including historical runs created before
    delivery tracking was added.
    """


class MonitorListAccountRunsResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
