# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeliveryListParams"]


class DeliveryListParams(TypedDict, total=False):
    batch_id: str

    cursor: str

    limit: int

    monitor_id: str

    run_id: str

    status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"]

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """
