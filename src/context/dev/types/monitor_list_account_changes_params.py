# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorListAccountChangesParams"]


class MonitorListAccountChangesParams(TypedDict, total=False):
    change_detection_type: Literal["exact", "semantic"]

    cursor: str

    limit: int

    monitor_id: str

    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]

    tag: str
    """Filter to items that have this tag."""

    target_type: Literal["page", "sitemap", "extract"]

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
