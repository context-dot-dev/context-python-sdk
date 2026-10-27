# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["PersonSearchParams", "Filters"]


class PersonSearchParams(TypedDict, total=False):
    query: Required[str]
    """Describe the people to find.

    Up to 500 characters in `fast` mode and 5000 in `ultra` mode.
    """

    cursor: str
    """Use next_cursor with the same query, mode and filters to fetch the next page."""

    filters: Filters
    """Additional constraints every result must match."""

    mode: Literal["fast", "ultra"]
    """`fast` matches people on basic criteria (e.g.

    their role, location or background); `ultra` plans a deeper search, judges each
    candidate against every criterion in the query and explains each match.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


class Filters(TypedDict, total=False):
    """Additional constraints every result must match."""

    countries: SequenceNotStr[str]
    """Countries people live in as two-letter codes, such as US or GB."""

    years_of_experience_max: int
    """Maximum years of professional experience."""

    years_of_experience_min: int
    """Minimum years of professional experience."""
