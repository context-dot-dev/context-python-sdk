# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from ..._types import SequenceNotStr

__all__ = ["DeliveryListAttemptsParams"]


class DeliveryListAttemptsParams(TypedDict, total=False):
    cursor: str
    """The next_cursor from the previous response."""

    limit: int
    """Number of attempts to return."""

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""
