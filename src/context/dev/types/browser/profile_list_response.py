# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProfileListResponse", "Data", "KeyMetadata"]


class Data(BaseModel):
    id: str
    """Profile ID to pass as `sharedParams.profile.profileId` on `/web/scrape`."""

    created_at: datetime
    """When the profile was created."""

    description: Optional[str] = None
    """The description supplied when the profile was created, or null."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class ProfileListResponse(BaseModel):
    data: List[Data]
    """Browser profiles, newest first."""

    has_more: bool
    """Whether a next page exists."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
