# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .webhook_delivery import WebhookDelivery

__all__ = ["MonitorRetrieveRunResponse", "Error", "KeyMetadata"]


class Error(BaseModel):
    code: str
    """Machine-readable error code, such as `fetch_failed`."""

    message: str
    """Human-readable explanation of the error."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class MonitorRetrieveRunResponse(BaseModel):
    id: str
    """Unique ID of the run."""

    baseline_created: bool
    """
    `true` when this run captured the monitor's baseline instead of checking for
    changes.
    """

    change_detected: bool
    """Whether the run detected a change."""

    change_detection_type: Literal["exact", "semantic"]
    """Change detection type the monitor uses."""

    credits_charged: int
    """Credits charged for this run. `0` for skipped and failed runs."""

    monitor_id: str
    """ID of the monitor this run belongs to."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    run_type: Literal["baseline", "scheduled"]
    """
    `baseline` runs capture a fresh baseline after creation or a target or detection
    change. `scheduled` runs, including on-demand ones, check for changes.
    """

    status: Literal["queued", "running", "completed", "failed", "skipped"]
    """Run status. `skipped` runs never executed; `skip_reason` says why."""

    target_type: Literal["page", "sitemap", "extract", "search"]
    """Type of target the monitor watches."""

    change_id: Optional[str] = None
    """ID of the change this run detected. `null` when it found none."""

    completed_at: Optional[datetime] = None
    """When the run ended. `null` until it ends."""

    error: Optional[Error] = None

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    skip_reason: Optional[Literal["insufficient_credits", "monitor_paused", "superseded"]] = None
    """
    Why the run was skipped; `superseded` means a concurrent run took its place or
    the monitor was deleted. `null` unless `status` is `skipped`.
    """

    started_at: Optional[datetime] = None
    """When the run started. `null` until it starts."""

    webhook_deliveries: Optional[List[WebhookDelivery]] = None
    """Webhook deliveries for this run, one per subscribed event that fired.

    Omitted when no delivery was attempted.
    """

    webhook_delivery: Optional[WebhookDelivery] = None
    """Deprecated. Use `webhook_deliveries` for all attempts."""

    webhook_delivery_ids: Optional[List[str]] = None
    """IDs of the webhook deliveries sent for this run."""
