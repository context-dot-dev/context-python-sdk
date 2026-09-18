# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["AIExtractProductParams", "TimeoutOpts"]


class AIExtractProductParams(TypedDict, total=False):
    url: Required[str]
    """The product page URL to extract product data from."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Return a cached result if a prior scrape for the same parameters exists and is
    younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
    omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.
    """

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Asset uploads are skipped, so hosted image URLs are
    omitted. Requires zero data retention to be enabled for your organization
    (contact support@context.dev), otherwise the request fails with ZDR_NOT_ENABLED.
    Successful ZDR responses include X-Context-ZDR: true.
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
