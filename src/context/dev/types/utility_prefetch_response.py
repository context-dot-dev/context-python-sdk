# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UtilityPrefetchResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class UtilityPrefetchResponse(BaseModel):
    domain: Optional[str] = None
    """The domain that was queued for prefetching"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    message: Optional[str] = None
    """Success message"""

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""

    type: Optional[Literal["brand", "styleguide"]] = None
    """The type of prefetch that was queued, echoed from the request"""
