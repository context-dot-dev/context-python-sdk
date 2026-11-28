# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorListAccountChangesParams"]


class MonitorListAccountChangesParams(TypedDict, total=False):
    change_detection_type: Literal["exact", "semantic"]
    """Filter by change detection type."""

    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of changes to return per page. Defaults to 25."""

    monitor_id: str
    """Return only changes from this monitor."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only changes detected at or after this time."""

    tag: str
    """Return only changes that have this tag."""

    target_type: Literal["page", "sitemap", "extract", "search"]
    """Filter by target type."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only changes detected at or before this time."""
