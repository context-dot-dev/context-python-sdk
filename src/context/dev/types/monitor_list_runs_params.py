# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["MonitorListRunsParams"]


class MonitorListRunsParams(TypedDict, total=False):
    cursor: str
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    limit: int
    """Maximum number of runs to return per page. Defaults to 25."""

    status: Literal["queued", "running", "completed", "failed", "skipped"]
    """Filter by run status."""
