# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .delivery import Delivery
from ..._models import BaseModel

__all__ = ["DeliveryRetrieveResponse", "DeliveryRetrieveResponseKeyMetadata"]


class DeliveryRetrieveResponseKeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class DeliveryRetrieveResponse(Delivery):
    key_metadata: Optional[DeliveryRetrieveResponseKeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
