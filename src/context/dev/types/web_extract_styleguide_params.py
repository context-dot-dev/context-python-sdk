# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["WebExtractStyleguideParams", "TimeoutOpts"]


class WebExtractStyleguideParams(TypedDict, total=False):
    color_scheme: Annotated[Literal["light", "dark"], PropertyInfo(alias="colorScheme")]
    """Emulate a light or dark color scheme. Each scheme is cached separately."""

    direct_url: Annotated[str, PropertyInfo(alias="directUrl")]
    """Exact page URL to analyze. Provide either `domain` or `directUrl`, not both."""

    domain: str
    """Domain to analyze, such as `stripe.com`.

    Provide either `domain` or `directUrl`, not both.
    """

    max_age_ms: Annotated[Optional[int], PropertyInfo(alias="maxAgeMs")]
    """Maximum age of a cached result, in milliseconds.

    `0` always fetches fresh. Defaults to 90 days (7776000000 ms). Values above 1
    year (31536000000 ms) are capped at 1 year.
    """

    policies: SequenceNotStr[str]
    """Comma-separated access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial. `return-partial` requires at least 5000 ms. On `POST /web/scrape`, an
    output that is not ready in time fails with `REQUEST_TIMEOUT` inside a 200
    response under either behavior; 408 means the whole request could not respond by
    the deadline.
    """
