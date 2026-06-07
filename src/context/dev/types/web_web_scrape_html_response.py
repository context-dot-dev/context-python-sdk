# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["WebWebScrapeHTMLResponse"]


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
