# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["BatchDeleteResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class BatchDeleteResponse(BaseModel):
    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    id: Optional[str] = None
    """ID of the deleted batch."""

    deleted: Optional[bool] = None
    """Always true on success."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
