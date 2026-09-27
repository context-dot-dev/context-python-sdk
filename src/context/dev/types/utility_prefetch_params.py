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
    """Data to prefetch."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    timeout_opts: Annotated[TimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""


class IdentifierUtilityPrefetchDomainIdentifier(TypedDict, total=False):
    """Prefetch by domain."""

    domain: Required[str]
    """Domain, e.g. `stripe.com`."""


class IdentifierUtilityPrefetchEmailIdentifier(TypedDict, total=False):
    """Prefetch by email. The domain will be extracted and validated."""

    email: Required[str]
    """Email address to prefetch data for.

    The domain will be extracted from the email. Free email providers (gmail.com,
    yahoo.com, etc.) and disposable email addresses are not allowed.
    """


Identifier: TypeAlias = Union[IdentifierUtilityPrefetchDomainIdentifier, IdentifierUtilityPrefetchEmailIdentifier]


class TimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail"]
    """Only "fail" is supported: return 408 at the deadline."""
