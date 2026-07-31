# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BatchSubmitParams", "Identifiers"]


class BatchSubmitParams(TypedDict, total=False):
    identifiers: Required[Identifiers]
    """Known identifiers for the person. At least one identifier is required."""

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class Identifiers(TypedDict, total=False):
    """Known identifiers for the person. At least one identifier is required."""

    linkedin_url: Annotated[str, PropertyInfo(alias="linkedinUrl")]
    """LinkedIn profile URL, e.g. https://www.linkedin.com/in/yahia-bakour/."""
