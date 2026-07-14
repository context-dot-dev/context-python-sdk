# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorListChangesParams"]


class MonitorListChangesParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response."""

    limit: int
    """Maximum number of items to return per page (1-100). Defaults to 25."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items at or after this ISO 8601 timestamp."""

    tag: str
    """Filter to items that have this tag."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items before this ISO 8601 timestamp."""
