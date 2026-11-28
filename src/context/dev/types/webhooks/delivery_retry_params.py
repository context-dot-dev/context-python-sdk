# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["DeliveryRetryParams"]


class DeliveryRetryParams(TypedDict, total=False):
    force: bool
    """Resend even if the delivery already succeeded."""

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    idempotency_key: Annotated[str, PropertyInfo(alias="Idempotency-Key")]
    """Unique key for this retry.

    Repeating the request with the same key does not send the payload again.
    """
