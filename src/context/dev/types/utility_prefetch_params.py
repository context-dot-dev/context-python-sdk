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
    """Identifier of the target to prefetch. Provide exactly one of domain or email."""

    type: Required[Literal["brand", "styleguide"]]
    """
    What to prefetch: 'brand' warms the brand data cache, 'styleguide' warms the
    styleguide cache.
    """

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail
    or a JSON-encoded timeoutOpts object.
    """


class IdentifierUtilityPrefetchDomainIdentifier(TypedDict, total=False):
    """Prefetch by domain."""

    domain: Required[str]
    """Domain name to prefetch data for"""


class IdentifierUtilityPrefetchEmailIdentifier(TypedDict, total=False):
    """Prefetch by email. The domain will be extracted and validated."""

    email: Required[str]
    """Email address to prefetch data for.

    The domain will be extracted from the email. Free email providers (gmail.com,
    yahoo.com, etc.) and disposable email addresses are not allowed.
    """


Identifier: TypeAlias = Union[IdentifierUtilityPrefetchDomainIdentifier, IdentifierUtilityPrefetchEmailIdentifier]


class TimeoutOpts(TypedDict, total=False):
    """Optional request deadline and behavior on timeout.

    For GET requests, use timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded timeoutOpts object.
    """

    milliseconds: Required[int]
    """Request deadline in milliseconds. Maximum: 300000 (5 minutes)."""

    behavior: Literal["fail"]
    """What to do at the deadline.

    This endpoint supports "fail": return 408 REQUEST_TIMEOUT without charging
    credits.
    """
