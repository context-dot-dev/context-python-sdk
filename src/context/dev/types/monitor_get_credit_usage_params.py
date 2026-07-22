# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["MonitorGetCreditUsageParams"]


class MonitorGetCreditUsageParams(TypedDict, total=False):
    since: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items at or after this ISO 8601 timestamp."""

    until: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include items before this ISO 8601 timestamp."""
