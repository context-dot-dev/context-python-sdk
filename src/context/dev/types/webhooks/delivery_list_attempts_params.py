# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeliveryListAttemptsParams"]


class DeliveryListAttemptsParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of attempts to return per page."""

    tags: SequenceNotStr[str]
    """Comma-separated labels for this request, such as `production,team-alpha`.

    Filter usage and request logs by them.
    """
