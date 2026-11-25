# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ScholarSearchParams", "FilterBy", "FilterByDate"]


class ScholarSearchParams(TypedDict, total=False):
    query: Required[str]
    """A topic or question.

    Append one arxiv:, pmcid:, pmid:, or doi: ID to search within an indexed paper.
    """

    cursor: Optional[str]
    """Use next_cursor to fetch the next page."""

    filter_by: Annotated[FilterBy, PropertyInfo(alias="filterBy")]
    """Filter by publication date."""

    limit: int
    """Papers per page."""

    sort: Literal["relevance", "date_desc"]
    """Order the top 250 matches.

    date_desc puts newest first, with undated papers last.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


_FilterByDateReservedKeywords = TypedDict(
    "_FilterByDateReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class FilterByDate(_FilterByDateReservedKeywords, total=False):
    """Publication date range. Undated papers are excluded."""

    to: int
    """Inclusive end date, in Unix milliseconds."""


class FilterBy(TypedDict, total=False):
    """Filter by publication date."""

    date: FilterByDate
    """Publication date range. Undated papers are excluded."""
