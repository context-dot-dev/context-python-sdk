# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["Attempt", "Error"]


class Error(BaseModel):
    """Why the attempt failed. `null` when it did not fail."""

    code: str
    """Machine-readable error code."""

    message: str
    """Human-readable explanation of the error."""


class Attempt(BaseModel):
    attempt: int
    """Attempt number, starting at 1."""

    completed_at: Optional[datetime] = None
    """When the attempt finished. `null` while in progress."""

    error: Optional[Error] = None
    """Why the attempt failed. `null` when it did not fail."""

    http_status: Optional[int] = None
    """HTTP status your endpoint returned. `null` when no response was received."""

    started_at: datetime
    """When the attempt started."""

    trigger: Literal["initial", "automatic", "manual"]
    """
    What started the attempt: `initial` is the first send, `automatic` is a
    scheduled retry, and `manual` came from
    `POST /webhooks/deliveries/{delivery_id}/retry`.
    """

    url: str
    """URL this attempt was sent to."""
