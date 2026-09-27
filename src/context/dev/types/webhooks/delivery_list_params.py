# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DeliveryListParams", "ByBatch", "ByMonitor"]


class ByBatch(TypedDict, total=False):
    type: Required[Literal["batch"]]
    """Delivery source."""

    batch_id: str
    """Filter by batch ID."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include events created after this ISO 8601 timestamp."""

    cursor: str
    """The next_cursor from the previous response."""

    limit: int
    """Number of deliveries to return."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Filter by delivery status."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


class ByMonitor(TypedDict, total=False):
    type: Required[Literal["monitor"]]
    """Delivery source."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include events created after this ISO 8601 timestamp."""

    cursor: str
    """The next_cursor from the previous response."""

    limit: int
    """Number of deliveries to return."""

    monitor_id: str
    """Filter by monitor ID."""

    run_id: str
    """Filter by monitor run ID."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Filter by delivery status."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


DeliveryListParams: TypeAlias = Union[ByBatch, ByMonitor]
