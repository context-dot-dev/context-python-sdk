# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ScholarSearchParams", "FilterBy", "FilterByDate"]


class ScholarSearchParams(TypedDict, total=False):
    query: Required[str]
    """Topic or question to search for.

    Append one `arxiv:`, `pmcid:`, `pmid:`, or `doi:` ID to search within that
    paper, such as `protein folding pmid:34265844`, or send the ID on its own.
    """

    cursor: Optional[str]
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    filter_by: Annotated[FilterBy, PropertyInfo(alias="filterBy")]
    """Filter by publication date."""

    limit: int
    """Maximum number of papers to return per page."""

    sort: Literal["relevance", "date_desc"]
    """
    `relevance` puts the closest matches first; `date_desc` puts the newest papers
    first, with undated papers last. Both orders apply to the top 250 matches.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """


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
