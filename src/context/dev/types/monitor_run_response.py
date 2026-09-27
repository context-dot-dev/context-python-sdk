# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["MonitorRunResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class MonitorRunResponse(BaseModel):
    monitor_id: str

    queued: bool

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    run_id: str
    """ID of the queued run; pass it to Retrieve a monitor run."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
