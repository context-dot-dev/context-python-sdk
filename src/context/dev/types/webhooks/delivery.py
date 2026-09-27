# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from datetime import datetime
from typing_extensions import Literal, TypeAlias

from .attempt import Attempt
from ..._models import BaseModel
from ..retry_config import RetryConfig

__all__ = ["Delivery", "LastError", "Source", "SourceBatch", "SourceMonitor"]


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
    """Which deliveries to list: `batch` or `monitor`."""


class SourceMonitor(BaseModel):
    monitor_id: str
    """Monitor ID."""

    run_id: str
    """Monitor run ID."""

    type: Literal["monitor"]
    """Which deliveries to list: `batch` or `monitor`."""


Source: TypeAlias = Union[SourceBatch, SourceMonitor]


class Delivery(BaseModel):
    id: str
    """Delivery ID."""

    created_at: datetime
    """Event creation time."""

    delivered_at: Optional[datetime] = None
    """Last successful delivery time, or null if never delivered."""

    event: Literal["batch.completed", "batch.failed", "batch.cancelled", "change.detected", "run.completed"]
    """Webhook event type."""

    event_id: str
    """Stable event ID for deduplicating received webhooks."""

    last_attempt: Optional[Attempt] = None
    """Latest attempt, or null if none."""

    last_error: Optional[LastError] = None
    """Latest delivery error, or null if none."""

    next_attempt_at: Optional[datetime] = None
    """Next scheduled attempt, or null if none."""

    retry: RetryConfig
    """Webhook retry settings. Use {} for the default schedule."""

    retry_expires_at: datetime
    """Last time you can retry manually (7 days after the event)."""

    source: Source
    """Batch or monitor run that produced the event."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """
    `pending`, `delivering`, `retrying`, `delivered`, `failed`, or `cancelled`
    (source or its webhook was removed).
    """

    url: str
    """Webhook destination URL."""
