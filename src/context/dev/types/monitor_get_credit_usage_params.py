# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorGetCreditUsageParams"]


class MonitorGetCreditUsageParams(TypedDict, total=False):
    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Count only runs created at or after this time."""

    tag: str
    """Return usage only for monitors that currently have this tag.

    Deleted monitors are excluded.
    """

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Count only runs created at or before this time."""
