# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MonitorListParams"]


class MonitorListParams(TypedDict, total=False):
    change_detection_type: Literal["exact", "semantic"]

    cursor: str

    limit: int

    status: Literal["active", "paused", "failed"]

    tag: str
    """Filter to items that have this tag."""

    target_type: Literal["page", "sitemap", "extract"]
