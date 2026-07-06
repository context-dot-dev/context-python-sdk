# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["UtilityPrefetchParams", "Identifier"]


class UtilityPrefetchParams(TypedDict, total=False):
    identifier: Required[Identifier]
    """Identifier of the brand to prefetch. Provide exactly one of domain or email."""

    type: Required[Literal["brand"]]
    """What to prefetch. Currently only 'brand' is supported."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class Identifier(TypedDict, total=False):
    """Identifier of the brand to prefetch. Provide exactly one of domain or email."""

    domain: str
    """Domain name to prefetch brand data for"""

    email: str
    """Email address to prefetch brand data for.

    The domain will be extracted from the email. Free email providers (gmail.com,
    yahoo.com, etc.) and disposable email addresses are not allowed.
    """
