# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from .._models import BaseModel

__all__ = ["MonitorGetCreditUsageResponse", "Data", "KeyMetadata"]


class Data(BaseModel):
    credits: int
    """Credits charged to the monitor in the window."""

    monitor_id: str
    """ID of the monitor."""

    name: str
    """Name of the monitor, or its ID if the monitor was deleted."""

    runs: int
    """Number of billed runs in the window."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class MonitorGetCreditUsageResponse(BaseModel):
    data: List[Data]
    """Usage per monitor, highest first."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    total_credits: int
    """Total credits across the monitors in `data`."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
