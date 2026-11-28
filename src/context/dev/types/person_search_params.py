# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonSearchParams", "Filters"]


class PersonSearchParams(TypedDict, total=False):
    query: Required[str]
    """Plain-language description of the people to find.

    Up to 500 characters in `fast` mode and 5000 in `ultra` mode.
    """

    cursor: str
    """Cursor from the previous page's `next_cursor`.

    Omit for the first page. Send the same `query`, `mode`, and `filters` with it.
    """

    filters: Filters
    """Constraints every result must match, in addition to `query`."""

    mode: Literal["fast", "ultra"]
    """
    `fast` matches people on basic criteria such as role, location, or background;
    `ultra` runs a deeper search, checks every candidate against each criterion in
    your query, and adds a `match` score. Complex `ultra` searches can take up to 30
    seconds, so set your client timeout to match.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class Filters(TypedDict, total=False):
    """Constraints every result must match, in addition to `query`."""

    countries: SequenceNotStr[str]
    """
    Only return people who live in these countries, as ISO 3166-1 alpha-2 codes such
    as `US`.
    """

    years_of_experience_max: int
    """Maximum years of professional experience."""

    years_of_experience_min: int
    """Minimum years of professional experience."""
