# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

from .._types import SequenceNotStr

__all__ = ["FeedbackSubmitParams"]


class FeedbackSubmitParams(TypedDict, total=False):
    category: Required[
        Literal["bug", "docs_mismatch", "friction", "feature_gap", "quality_degradation", "bad_brand", "other"]
    ]
    """Kind of issue.

    Use `quality_degradation` for wrong or incomplete results and `bad_brand` for
    wrong or outdated brand data, such as a logo or colors.
    """

    note: Required[str]
    """What went wrong and what you expected instead.

    Leave out API keys and personal data.
    """

    request_id: str
    """
    ID of the API call the feedback is about, from its `request_id` or
    `X-Request-Id` header. Send this, `url`, or both.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    url: str
    """URL the feedback is about, such as one page of a crawl or a docs page.

    Send this, `request_id`, or both.
    """
