# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["WebExtractCompetitorsParams"]


class WebExtractCompetitorsParams(TypedDict, total=False):
    domain: Required[str]
    """Company domain to analyze, such as `stripe.com`.

    Full http(s) URLs are accepted and normalized to their domain.
    """

    num_competitors: Annotated[int, PropertyInfo(alias="numCompetitors")]
    """Exact number of direct competitors to return. Defaults to 5."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """
