# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MonitorListAccountRunsParams"]


class MonitorListAccountRunsParams(TypedDict, total=False):
    cursor: str
    """Opaque pagination cursor from a previous response."""

    limit: int
    """Maximum number of items to return per page (1-100). Defaults to 25."""

    status: Literal["queued", "running", "completed", "failed", "skipped"]
    """Filter runs by lifecycle status."""
