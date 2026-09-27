# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MonitorGetCreditUsageResponse", "Data", "KeyMetadata"]


class Data(BaseModel):
    credits: int
    """Credits charged to this monitor over the window."""

    monitor_id: str

    name: str
    """Monitor name (falls back to the id when the monitor was deleted)."""

    runs: int
    """Number of billed runs over the window."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class MonitorGetCreditUsageResponse(BaseModel):
    data: List[Data]

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    total_credits: int
    """Sum of credits across all monitors in the window."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
