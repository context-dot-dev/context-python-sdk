# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .attempt import Attempt
from ..._models import BaseModel
from ..retry_config import RetryConfig

__all__ = ["Delivery", "LastError", "Source", "SourceBatch", "SourceMonitor"]


class LastError(BaseModel):
    """Most recent delivery error. `null` when there is none."""

    code: str
    """Machine-readable error code."""

    message: str
    """Human-readable explanation of the error."""


class SourceBatch(BaseModel):
    batch_id: str
    """ID of the batch."""

    type: Literal["batch"]
    """The event came from a batch."""


class SourceMonitor(BaseModel):
    monitor_id: str
    """ID of the monitor."""

    run_id: str
    """ID of the monitor run."""

    type: Literal["monitor"]
    """The event came from a monitor run."""


Source: TypeAlias = Union[SourceBatch, SourceMonitor]


class Delivery(BaseModel):
    id: str
    """Unique ID of the delivery."""

    created_at: datetime
    """When the event was created."""

    delivered_at: Optional[datetime] = None
    """When the delivery last succeeded. `null` until it succeeds."""

    event: Literal["batch.completed", "batch.failed", "batch.cancelled", "change.detected", "run.completed"]
    """Event that triggered the delivery."""

    event_id: str
    """Event ID, sent as `X-Context-Id` and as `id` in the payload.

    It stays the same across retries, so use it to deduplicate.
    """

    last_attempt: Optional[Attempt] = None
    """Most recent attempt. `null` before the first attempt."""

    last_error: Optional[LastError] = None
    """Most recent delivery error. `null` when there is none."""

    next_attempt_at: Optional[datetime] = None
    """When the next attempt is scheduled. `null` when none is scheduled."""

    retry: RetryConfig
    """Automatic retry settings. Pass `{}` for the default schedule."""

    retry_expires_at: datetime
    """Last time you can retry the delivery manually, 7 days after the event."""

    source: Source
    """Batch or monitor run that produced the event."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Delivery state.

    `pending` is waiting for an attempt, `delivering` has an attempt in progress,
    `retrying` is waiting for an automatic retry, `delivered` was acknowledged with
    a 2xx, `failed` has no automatic retries left, and `cancelled` means the source
    or its webhook was removed.
    """

    url: str
    """URL the webhook is sent to."""
