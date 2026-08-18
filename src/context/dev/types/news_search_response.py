# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["NewsSearchResponse", "Data", "DataMatch", "DataSource", "Meta", "KeyMetadata"]


class DataMatch(BaseModel):
    """How the article relates to the company you searched for."""

    confidence: Optional[float] = None
    """How confident the match is, from 0 to 1. Null when a score is unavailable."""

    level: Literal["primary", "secondary"]
    """
    primary when the article is mainly about the company, secondary when the company
    is mentioned but is not the main subject.
    """


class DataSource(BaseModel):
    """The publication that published the article."""

    direct: bool
    """True when Context observed this article in the publisher-owned feed."""

    domain: str
    """Website domain of the publication."""

    name: str
    """Name of the publication, such as Reuters."""


class Data(BaseModel):
    id: str
    """Stable unique identifier for this article.

    Use it to deduplicate or reference an article across requests.
    """

    authors: List[str]
    """Bylined authors. Empty when no byline is available."""

    description: Optional[str] = None
    """Short summary or excerpt of the article, when the publisher provides one."""

    image_url: Optional[str] = None
    """Lead image for the article, when one is available."""

    language: Optional[str] = None
    """Language the article is written in, as a lowercase ISO 639-1 code such as en.

    Null when unknown.
    """

    match: DataMatch
    """How the article relates to the company you searched for."""

    published_at: Optional[datetime] = None
    """When the article was published, as an ISO 8601 timestamp.

    Null when the publisher does not state a reliable date.
    """

    source: DataSource
    """The publication that published the article."""

    story_id: str
    """Shared by articles covering the same story on the same day.

    Use it to group or collapse syndicated copies of one announcement across
    outlets.
    """

    title: str
    """Article headline."""

    type: Literal["editorial", "press_release", "regulatory_filing", "advisory"]
    """Kind of coverage.

    Use it to separate independent reporting (editorial) from company-issued content
    (press_release, regulatory_filing, advisory).
    """

    url: str
    """Link to the article on the publisher site."""


class Meta(BaseModel):
    """Summary information about this response."""

    count: int
    """Number of articles in this page."""


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class NewsSearchResponse(BaseModel):
    data: List[Data]
    """Articles matching the search, in the requested order."""

    has_more: bool
    """True when more results are available beyond this page."""

    meta: Meta
    """Summary information about this response."""

    next_cursor: Optional[str] = None
    """Pass as cursor in the next request to fetch the following page.

    Null when there are no more results.
    """

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
