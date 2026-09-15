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
    """Comma-separated tags for tracking request usage.

    Up to 20 tags, each 1-50 characters.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """


class TimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail", "return-partial"]
    """What to do at the deadline.

    "fail" returns 408 REQUEST_TIMEOUT without charging credits. "return-partial"
    returns usable results collected so far; if none are available, the request
    still fails without charging credits. Partial results are not cached as complete
    results.
    """
