# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["IndustryRetrieveSicParams"]


class IndustryRetrieveSicParams(TypedDict, total=False):
    input: Required[str]
    """Brand domain or title to retrieve SIC code for.

    If a valid domain is provided, it will be used for classification, otherwise, we
    will search for the brand using the provided title.
    """

    max_results: Annotated[int, PropertyInfo(alias="maxResults")]
    """Maximum number of SIC codes to return. Must be between 1 and 10. Defaults to 5."""

    min_results: Annotated[int, PropertyInfo(alias="minResults")]
    """Minimum number of SIC codes to return. Must be at least 1. Defaults to 1."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """

    type: Literal["original_sic", "latest_sec"]
    """Which SIC dataset to classify against.

    `original_sic` uses the 1987 Standard Industrial Classification system;
    `latest_sec` uses the current SIC list as published by the SEC. Defaults to
    `original_sic`.
    """
