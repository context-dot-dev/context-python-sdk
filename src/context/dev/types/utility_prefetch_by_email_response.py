# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["UtilityPrefetchByEmailResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class UtilityPrefetchByEmailResponse(BaseModel):
    domain: Optional[str] = None
    """The domain that was queued for prefetching"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    message: Optional[str] = None
    """Success message"""

    status: Optional[str] = None
    """Status of the response, e.g., 'ok'"""
