# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorListChangesParams"]


class MonitorListChangesParams(TypedDict, total=False):
    cursor: str

    limit: int

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    tag: str
    """Filter to items that have this tag."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
