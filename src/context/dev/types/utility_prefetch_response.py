# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UtilityPrefetchResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class UtilityPrefetchResponse(BaseModel):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    domain: Optional[str] = None
    """The domain that was queued for prefetching"""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    message: Optional[str] = None
    """Success message"""

    status: Optional[str] = None
    """Always `ok` on success."""

    type: Optional[Literal["brand", "styleguide"]] = None
    """The type of prefetch that was queued, echoed from the request"""
