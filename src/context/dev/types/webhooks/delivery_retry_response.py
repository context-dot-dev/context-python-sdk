# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .delivery import Delivery
from ..._models import BaseModel

__all__ = ["DeliveryRetryResponse", "DeliveryRetryResponseKeyMetadata"]


class DeliveryRetryResponseKeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class DeliveryRetryResponse(Delivery):
    key_metadata: Optional[DeliveryRetryResponseKeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
