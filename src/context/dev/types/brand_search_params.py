# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["BrandSearchParams"]


class BrandSearchParams(TypedDict, total=False):
    query: Required[str]
    """Search term, matched against brand names and domains by prefix (e.g.

    'nike', 'nike.com', 'nik').
    """

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """
