# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["FeedbackSubmitResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class FeedbackSubmitResponse(BaseModel):
    already_submitted: bool
    """
    True when feedback for this request_id was already recorded; the original
    feedback_id is returned.
    """

    feedback_id: str
    """ID of the stored feedback."""

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
