# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["BrandSearchParams"]


class BrandSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search term, matched against the fields selected by queryBy (e.g.

    'nike', 'nike.com', 'nik').
    """

    autocomplete: bool
    """
    Whether the search term matches by prefix, so partial words match as they are
    typed (e.g. 'nik' matches Nike). Set to false to match whole words only.
    """

    query_by: Annotated[List[Literal["name", "domain"]], PropertyInfo(alias="queryBy")]
    """
    Fields to match the search term against, as a comma-separated list or repeated
    parameter: 'name', 'domain', or both. Defaults to both.
    """

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    typo_tolerance: Annotated[int, PropertyInfo(alias="typoTolerance")]
    """Maximum number of typos tolerated when matching, from 0 to 2.

    Defaults to 0 (no typo tolerance).
    """
