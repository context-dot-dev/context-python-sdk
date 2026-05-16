# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebSearchResponse", "Result", "ResultMarkdown"]


class ResultMarkdown(BaseModel):
    """Markdown scrape status and content for this result."""

    code: Literal["SUCCESS", "NOT_REQUESTED", "TIMEOUT", "WEBSITE_ACCESS_ERROR", "ERROR"]
    """Per-result scrape outcome. Inspect this before reading `markdown`."""

    markdown: Optional[str] = None
    """GFM Markdown of the page.

    Null unless markdownOptions.enabled is true and scraping succeeded.
    """


class Result(BaseModel):
    description: str
    """Snippet excerpt from the page."""

    markdown: ResultMarkdown
    """Markdown scrape status and content for this result."""

    relevance: Literal["high", "medium", "low"]
    """Relevance to the original query."""

    title: str
    """Page title."""

    url: str
    """Canonical result URL."""


class WebSearchResponse(BaseModel):
    query: str
    """Echo of the original query (useful when fanout was enabled)."""

    results: List[Result]
