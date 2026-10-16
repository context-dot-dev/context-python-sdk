# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["ProfileListParams"]


class ProfileListParams(TypedDict, total=False):
    cursor: str
    """The `next_cursor` from the previous page."""

    limit: int
    """Number of profiles per page."""
