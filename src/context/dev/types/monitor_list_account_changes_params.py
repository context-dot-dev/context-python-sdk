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
    """Opaque pagination cursor from a previous response."""

    limit: int
    """Maximum number of items to return per page (1-100). Defaults to 25."""

    monitor_id: str
    """Filter changes to a single monitor."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items at or after this ISO 8601 timestamp."""

    tag: str
    """Filter to items that have this tag."""

    target_type: Literal["page", "sitemap", "extract"]
    """Filter by target type."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items before this ISO 8601 timestamp."""
