# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel

__all__ = ["DeliveryRetryResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class DeliveryRetryResponse(BaseModel):
    id: str
    """Delivery ID."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
