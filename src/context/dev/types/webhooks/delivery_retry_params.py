# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DeliveryRetryParams"]


class DeliveryRetryParams(TypedDict, total=False):
    force: bool
    """Resend even if the delivery already succeeded. Defaults to false."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Unique key to prevent duplicate retry requests."""
