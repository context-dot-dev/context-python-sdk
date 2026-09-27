# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .attempt import Attempt
from ..._models import BaseModel

__all__ = ["DeliveryListAttemptsResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class DeliveryListAttemptsResponse(BaseModel):
    data: List[Attempt]
    """Delivery attempts."""

    has_more: bool
    """Whether more attempts are available."""

    next_cursor: Optional[str] = None
    """Next page cursor, or null on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
