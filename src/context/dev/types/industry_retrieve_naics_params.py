# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["IndustryRetrieveNaicsParams"]


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
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
