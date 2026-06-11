# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeHTMLResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


class WebWebScrapeHTMLResponse(BaseModel):
    html: str
    """The scraped content of the page.

    For normal pages this is the raw HTML. When the page is a sitemap or feed served
    behind an XSL stylesheet (which browsers render into HTML), this is the
    underlying XML instead — see the `type` field.
    """

    success: Literal[True]
    """Indicates success"""

    type: Literal["html", "xml", "json", "text", "csv", "markdown", "svg", "pdf"]
    """Detected content type of the returned `html` field.

    Sitemaps and feeds are surfaced as `xml`; ordinary pages are `html`.
    """

    url: str
    """The URL that was scraped"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """
