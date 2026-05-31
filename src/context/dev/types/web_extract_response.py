# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["WebExtractResponse", "Metadata"]


class Metadata(BaseModel):
    max_crawl_depth: int = FieldInfo(alias="maxCrawlDepth")

    num_failed: int = FieldInfo(alias="numFailed")

    num_skipped: int = FieldInfo(alias="numSkipped")

    num_succeeded: int = FieldInfo(alias="numSucceeded")

    num_urls: int = FieldInfo(alias="numUrls")


class WebExtractResponse(BaseModel):
    data: Dict[str, object]
    """Extracted data matching the request schema"""

    metadata: Metadata

    status: str
    """Status of the response, e.g., 'ok'"""

    url: str
    """The starting URL that was analyzed"""

    urls_analyzed: List[str]
    """List of URLs whose Markdown was used for extraction"""
