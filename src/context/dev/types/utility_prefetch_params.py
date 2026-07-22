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
]


class UtilityPrefetchParams(TypedDict, total=False):
    identifier: Required[Identifier]
    """Identifier of the brand to prefetch. Provide exactly one of domain or email."""

    type: Required[Literal["brand"]]
    """What to prefetch. Currently only 'brand' is supported."""

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class IdentifierUtilityPrefetchDomainIdentifier(TypedDict, total=False):
    """Prefetch brand data by domain."""

    domain: Required[str]
    """Domain name to prefetch brand data for"""


class IdentifierUtilityPrefetchEmailIdentifier(TypedDict, total=False):
    """Prefetch brand data by email. The domain will be extracted and validated."""

    email: Required[str]
    """Email address to prefetch brand data for.

    The domain will be extracted from the email. Free email providers (gmail.com,
    yahoo.com, etc.) and disposable email addresses are not allowed.
    """


Identifier: TypeAlias = Union[IdentifierUtilityPrefetchDomainIdentifier, IdentifierUtilityPrefetchEmailIdentifier]
