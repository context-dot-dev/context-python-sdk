# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel
from .delivery_summary import DeliverySummary

__all__ = ["DeliveryListResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class DeliveryListResponse(BaseModel):
    data: List[DeliverySummary]
    """Webhook deliveries."""

    has_more: bool
    """Whether more deliveries are available."""

    next_cursor: Optional[str] = None
    """Next page cursor, or null on the last page."""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
