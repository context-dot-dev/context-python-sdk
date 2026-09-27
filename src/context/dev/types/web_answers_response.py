# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from .._models import BaseModel

__all__ = ["WebAnswersResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class WebAnswersResponse(BaseModel):
    json_content: Dict[str, object]
    """The answer, in the shape requested by json_format."""

    sources: List[str]
    """
    Public evidence URLs from searches, pages, or company/profile records, in
    first-seen order. A listed URL may identify a record without its page being
    read.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """
    True when the request deadline ended research and the answer uses the evidence
    collected so far.
    """
