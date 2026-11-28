# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of profiles to return per page."""
