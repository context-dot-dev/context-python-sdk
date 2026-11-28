# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "UtilityPrefetchParams",
    "Identifier",
    "IdentifierUtilityPrefetchDomainIdentifier",
    "IdentifierUtilityPrefetchEmailIdentifier",
    "TimeoutOpts",
]


class UtilityPrefetchParams(TypedDict, total=False):
    identifier: Required[Identifier]
    """Domain or work email to prefetch. Provide exactly one."""

    type: Required[Literal["brand", "styleguide"]]
    """Data to prefetch."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline. The request fails with 408 when it passes."""


class IdentifierUtilityPrefetchDomainIdentifier(TypedDict, total=False):
    """Prefetch by domain."""

    domain: Required[str]
    """Domain to prefetch, such as `stripe.com`."""


class IdentifierUtilityPrefetchEmailIdentifier(TypedDict, total=False):
    """Prefetch by work email. Context.dev uses the email's domain."""

    email: Required[str]
    """Work email whose domain to prefetch.

    Free email providers such as `gmail.com` and disposable addresses are rejected
    with 422.
    """


Identifier: TypeAlias = Union[IdentifierUtilityPrefetchDomainIdentifier, IdentifierUtilityPrefetchEmailIdentifier]


class TimeoutOpts(TypedDict, total=False):
    """Request deadline. The request fails with 408 when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail"]
    """Only `fail` is supported: the request returns 408 at the deadline."""
