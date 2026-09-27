# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["MonitorRetrieveRunResponse", "Error", "KeyMetadata"]


class Error(BaseModel):
    code: str

    message: str


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class MonitorRetrieveRunResponse(BaseModel):
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

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    run_type: Literal["baseline", "scheduled"]
    """A baseline run follows creation or a target or detection change."""

    status: Literal["queued", "running", "completed", "failed", "skipped"]
    """Lifecycle status of a run.

    `skipped` runs never executed — see `skip_reason` (insufficient credits, monitor
    paused, or superseded by a concurrent run).
    """

    target_type: Literal["page", "sitemap", "extract"]

    change_id: Optional[str] = None

    completed_at: Optional[datetime] = None

    error: Optional[Error] = None

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

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
    """Deprecated. Use `webhook_deliveries` for all attempts."""

    webhook_delivery_ids: Optional[List[str]] = None
    """Webhook delivery IDs for this run."""
