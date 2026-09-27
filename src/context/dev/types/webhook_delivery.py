# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookDelivery", "Error"]


class Error(BaseModel):
    code: str

    message: str


class WebhookDelivery(BaseModel):
    attempted_at: datetime

    error: Optional[Error] = None

    event: Literal["change.detected", "run.completed"]
    """The event this delivery carried.

    Deliveries recorded before event selection existed report change.detected.
    """

    event_id: str
    """Identifier sent in the X-Context-Id header."""

    http_status: Optional[int] = None
    """
    The endpoint's final HTTP response status, or null when no response was
    received.
    """

    status: Literal["delivered", "rejected", "failed", "skipped_unsafe_url"]
    """Outcome of the delivery attempt. Any 2xx response counts as delivered."""

    delivery_id: Optional[str] = None
    """Delivery ID for status checks and retries, when available."""
