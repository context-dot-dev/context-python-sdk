# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["MonitorGetLimitsResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class MonitorGetLimitsResponse(BaseModel):
    monitors_limit: int
    """
    Maximum number of monitors your organization can have, from your plan or a
    custom limit.
    """

    monitors_used: int
    """Number of monitors your organization has."""

    plan: Literal["free", "starter", "pro", "scale"]
    """Your plan tier.

    `free` is Free, `starter` is Developer, `pro` is Pro or Growth, and `scale` is
    Scale or Enterprise.
    """

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
