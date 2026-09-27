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
    """Credits remaining for your organization."""


class MonitorGetLimitsResponse(BaseModel):
    monitors_limit: int
    """Most monitors you can have: your plan's allowance or a custom limit."""

    monitors_used: int
    """Number of monitors the account currently has."""

    plan: Literal["free", "starter", "pro", "scale"]
    """
    `starter` means Developer; `pro` means Pro or Growth; `scale` means Scale or
    Enterprise.
    """

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
