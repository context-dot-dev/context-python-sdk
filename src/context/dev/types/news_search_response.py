# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NewsSearchResponse", "Data", "DataMatch", "DataSource", "Meta", "KeyMetadata"]


class DataMatch(BaseModel):
    """How the article relates to the company you searched for.

    `null` for natural-language searches.
    """

    confidence: Optional[float] = None
    """Confidence in the match, from 0 to 1. `null` when no score is available."""

    level: Literal["primary", "secondary"]
    """
    `primary` when the article is mainly about the company; `secondary` when the
    company is mentioned but is not the main subject.
    """


class DataSource(BaseModel):
    """Publication that published the article."""

    direct: bool
    """
    Whether the article came directly from the publisher's own feed rather than
    through an aggregator.
    """

    domain: str
    """Website domain of the publication, such as `reuters.com`."""

    name: str
    """Name of the publication, such as Reuters."""


class Data(BaseModel):
    id: str
    """Unique ID of the article.

    It stays the same across requests, so you can use it to deduplicate.
    """

    authors: List[str]
    """Authors named in the byline. Empty when there is no byline."""

    description: Optional[str] = None
    """Summary or excerpt of the article.

    For natural-language searches, it includes the matching passages, up to 2,000
    characters.
    """

    image_url: Optional[str] = None
    """URL of the article's lead image. `null` when there is none."""

    language: Optional[str] = None
    """Language of the article, as an ISO 639-1 code such as `en`.

    `null` when unknown.
    """

    match: Optional[DataMatch] = None
    """How the article relates to the company you searched for.

    `null` for natural-language searches.
    """

    published_at: Optional[datetime] = None
    """When the article was published.

    `null` when the publisher does not give a reliable date.
    """

    source: DataSource
    """Publication that published the article."""

    story_id: str
    """ID shared by articles that cover the same story on the same day.

    Use it to group syndicated copies of one announcement across outlets.
    """

    title: str
    """Headline of the article."""

    type: Literal["editorial", "press_release", "regulatory_filing", "advisory"]
    """Type of coverage.

    Use it to separate independent reporting (`editorial`) from company-issued
    content (`press_release`, `regulatory_filing`, `advisory`).
    """

    url: str
    """URL of the article on the publisher's site."""


class Meta(BaseModel):
    """Summary of this page."""

    count: int
    """Number of articles on this page."""


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class NewsSearchResponse(BaseModel):
    data: List[Data]
    """Articles on this page, in the requested order."""

    has_more: bool
    """Whether more results are available after this page."""

    meta: Meta
    """Summary of this page."""

    next_cursor: Optional[str] = None
    """Pass as `cursor` to fetch the next page. `null` on the last page."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""
