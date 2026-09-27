# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .delivery import Delivery
from ..._models import BaseModel

__all__ = ["DeliveryRetrieveResponse", "DeliveryRetrieveResponseKeyMetadata"]


class DeliveryRetrieveResponseKeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class DeliveryRetrieveResponse(Delivery):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[DeliveryRetrieveResponseKeyMetadata] = None
    """Credits this request used and your remaining balance."""
