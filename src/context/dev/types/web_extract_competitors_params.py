# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebExtractCompetitorsParams", "TimeoutOpts"]


class WebExtractCompetitorsParams(TypedDict, total=False):
    domain: Required[str]
    """Company domain, such as `stripe.com`. Full URLs are reduced to their domain."""

    num_competitors: Annotated[int, PropertyInfo(alias="numCompetitors")]
    """Exact number of direct competitors to return."""

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """

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
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """
