# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebhookDelivery", "Error"]


class Error(BaseModel):
    code: str
    """Machine-readable error code, such as `fetch_failed`."""

    message: str
    """Human-readable explanation of the error."""


class WebhookDelivery(BaseModel):
    attempted_at: datetime
    """When the delivery was attempted."""

    error: Optional[Error] = None

    event: Literal["change.detected", "run.completed"]
    """Event this delivery carried."""

    event_id: str
    """Event ID, sent in the `X-Context-Id` header."""

    http_status: Optional[int] = None
    """Final HTTP status from your endpoint. `null` when no response was received."""

    status: Literal["delivered", "rejected", "failed", "skipped_unsafe_url"]
    """
    Outcome of the delivery: `delivered` (2xx response), `rejected` (non-2xx
    response), `failed` (no response), or `skipped_unsafe_url` (the URL isn't a safe
    public endpoint).
    """

    delivery_id: Optional[str] = None
    """ID for looking up or retrying this delivery, when available."""
