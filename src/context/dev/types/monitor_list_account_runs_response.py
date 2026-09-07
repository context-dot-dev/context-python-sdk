# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["MonitorListAccountRunsResponse", "Data", "DataError"]


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

    webhook_deliveries: Optional[List[WebhookDelivery]] = None
    """
    All webhook deliveries attempted by this run — one per subscribed event that
    fired. Omitted when no webhook was attempted, including runs created before
    event selection was added.
    """

    webhook_delivery: Optional[WebhookDelivery] = None
    """
    Deprecated: use `webhook_deliveries`, which records every attempt now that a run
    can deliver multiple events. Omitted when no webhook was attempted, including
    historical runs created before delivery tracking was added.
    """

    webhook_delivery_ids: Optional[List[str]] = None
    """Retained webhook deliveries for this run.

    Inspect their live state and attempt history through /webhooks/deliveries. With
    webhook.retry configured, delivery is asynchronous and the legacy
    webhook_delivery/webhook_deliveries outcomes are omitted.
    """


class MonitorListAccountRunsResponse(BaseModel):
    data: List[Data]

    has_more: bool

    next_cursor: Optional[str] = None
