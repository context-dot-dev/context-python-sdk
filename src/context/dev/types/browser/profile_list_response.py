# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["ProfileListResponse", "Data", "KeyMetadata"]


class Data(BaseModel):
    id: str
    """Unique ID of the browser profile.

    Pass it as `sharedParams.profile.profileId` on `POST /web/scrape`.
    """

    created_at: datetime
    """When the browser profile was created."""

    description: Optional[str] = None
    """Label set when the profile was created. `null` when none was set."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class ProfileListResponse(BaseModel):
    data: List[Data]
    """Browser profiles on this page, newest first."""

    has_more: bool
    """Whether more results are available after this page."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. `null` on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
