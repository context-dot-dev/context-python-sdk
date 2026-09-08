# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from ..._models import BaseModel

__all__ = ["DeliverySummary", "LastError", "Source", "SourceBatch", "SourceMonitor"]


class LastError(BaseModel):
    """Latest delivery error, or null if none."""

    code: str
    """Error code."""

    message: str
    """Error details."""


class SourceBatch(BaseModel):
    batch_id: str
    """Batch ID."""

    type: Literal["batch"]
    """Delivery source."""


class SourceMonitor(BaseModel):
    monitor_id: str
    """Monitor ID."""

    run_id: str
    """Monitor run ID."""

    type: Literal["monitor"]
    """Delivery source."""


Source: TypeAlias = Union[SourceBatch, SourceMonitor]


class DeliverySummary(BaseModel):
    id: str
    """Delivery ID."""

    created_at: datetime
    """Event creation time."""

    delivered_at: Optional[datetime] = None
    """Last successful delivery time, or null if never delivered."""

    event: Literal["batch.completed", "batch.failed", "batch.cancelled", "change.detected", "run.completed"]
    """Webhook event type."""

    last_error: Optional[LastError] = None
    """Latest delivery error, or null if none."""

    next_attempt_at: Optional[datetime] = None
    """Next scheduled attempt, or null if none."""

    retry_expires_at: datetime
    """Manual retry deadline, seven days after event creation."""

    source: Source
    """Batch or monitor run that produced the event."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Current delivery status."""

    url: str
    """Webhook destination URL."""
