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
    """Only include requests that returned a 4xx or 5xx status."""

    from_: Annotated[Union[str, datetime], PropertyInfo(alias="from", format="iso8601")]
    """Only include requests at or after this ISO 8601 timestamp.

    Defaults to 24 hours before `to`.
    """

    key_id: str
    """Filter by the API key that made the request."""

    limit: int
    """Number of log entries per page."""

    page: int
    """Page number, starting at 1."""

    path: str
    """Filter by endpoint path, with or without the /v1 prefix."""

    search: str
    """Case-insensitive substring match against the request query and body, e.g.

    a domain.
    """

    status_code: int
    """Filter by exact HTTP status code."""

    tags: str
    """Comma-separated request tags.

    Matches requests carrying any of them. Up to 20 tags, each 1-50 characters.
    """

    to: Annotated[Union[str, datetime], PropertyInfo(format="iso8601")]
    """Only include requests at or before this ISO 8601 timestamp. Defaults to now."""
