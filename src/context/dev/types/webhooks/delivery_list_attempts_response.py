# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .attempt import Attempt
from ..._models import BaseModel

__all__ = ["DeliveryListAttemptsResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

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
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
