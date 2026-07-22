# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BrandRetrieveSimplifiedParams"]


class BrandRetrieveSimplifiedParams(TypedDict, total=False):
    domain: Required[str]
    """Domain name to retrieve simplified brand data for"""

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    theme: Literal["light", "dark"]
    """Optional theme preference used when selecting brand assets."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
