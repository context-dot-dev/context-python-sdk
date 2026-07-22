# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List

from .._models import BaseModel

__all__ = ["MonitorGetCreditUsageResponse", "Data"]


class Data(BaseModel):
    credits: int
    """Credits charged to this monitor over the window."""

    monitor_id: str

    name: str
    """Monitor name (falls back to the id when the monitor was deleted)."""

    runs: int
    """Number of billed runs over the window."""


class MonitorGetCreditUsageResponse(BaseModel):
    data: List[Data]

    total_credits: int
    """Sum of credits across all monitors in the window."""
