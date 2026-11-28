# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FeedbackSubmitResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class FeedbackSubmitResponse(BaseModel):
    already_submitted: bool
    """`true` when feedback for this `request_id` was already recorded.

    `feedback_id` is then the original ID.
    """

    feedback_id: str
    """Unique ID of the feedback."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
