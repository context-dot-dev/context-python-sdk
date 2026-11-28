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
    """List batch webhook deliveries."""

    batch_id: str
    """Filter by batch ID."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include deliveries created after this time."""

    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of deliveries to return per page."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Filter by delivery status."""

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """


class ByMonitor(TypedDict, total=False):
    type: Required[Literal["monitor"]]
    """List monitor webhook deliveries."""

    created_after: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include deliveries created after this time."""

    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of deliveries to return per page."""

    monitor_id: str
    """Filter by monitor ID."""

    run_id: str
    """Filter by monitor run ID."""

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]
    """Filter by delivery status."""

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """


DeliveryListParams: TypeAlias = Union[ByBatch, ByMonitor]
