# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["FeedbackSubmitParams"]


class FeedbackSubmitParams(TypedDict, total=False):
    category: Required[Literal["bug", "docs_mismatch", "friction", "feature_gap", "quality_degradation", "other"]]
    """Kind of issue."""

    note: Required[str]
    """What went wrong and what you expected instead."""

    request_id: str
    """
    The request_id of the API call the feedback is about, from its response body or
    X-Request-Id header.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""

    url: str
    """The page the feedback is about, such as one page of a crawl or a docs page."""
