# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorListChangesParams"]


class MonitorListChangesParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of changes to return per page. Defaults to 25."""

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only changes detected at or after this time."""

    tag: str
    """Return only changes that have this tag."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return only changes detected at or before this time."""
