# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["IndustryRetrieveNaicsParams", "TimeoutOpts"]


class IndustryRetrieveNaicsParams(TypedDict, total=False):
    input: Required[str]
    """Brand domain or title to retrieve NAICS code for.

    If a valid domain is provided, it will be used for classification, otherwise, we
    will search for the brand using the provided title.
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of NAICS codes to return.

    Must be between 1 and 10. Defaults to 5.
    """

    min_results: Annotated[int, PropertyInfo(alias="minResults")]
    """Minimum number of NAICS codes to return. Must be at least 1. Defaults to 1."""

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """\"fail" returns 408 at the deadline.

    "return-partial" returns available results; inspect the response’s partial flag.
    """
