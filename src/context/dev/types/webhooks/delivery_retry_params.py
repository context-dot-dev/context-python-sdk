# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DeliveryRetryParams"]


class DeliveryRetryParams(TypedDict, total=False):
    force: bool

    tags: SequenceNotStr[str]
    """Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
