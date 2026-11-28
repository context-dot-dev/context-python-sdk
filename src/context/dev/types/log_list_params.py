# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["LogListParams"]


class LogListParams(TypedDict, total=False):
    error_code: str
    """Filter by the `error_code` returned in the response."""

    errors_only: bool
    """Return only requests that failed with a 4xx or 5xx status."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Return requests at or after this time. Defaults to 24 hours before `to`."""

    key_id: str
    """Filter by the ID of the API key that made the request."""

    limit: int
    """Maximum number of log entries to return per page."""

    page: int
    """Page number, starting at 1."""

    path: str
    """Filter by endpoint path, with or without the `/v1` prefix."""

    search: str
    """Case-insensitive text to find in the request query or body, such as a domain."""

    status_code: int
    """Filter by exact HTTP status code."""

    tags: str
    """Comma-separated tags.

    Returns log entries that have any of them. Up to 20 tags of 1 to 50 characters
    each.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Return requests at or before this time. Defaults to now."""
