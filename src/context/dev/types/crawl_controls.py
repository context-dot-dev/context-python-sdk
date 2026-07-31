# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from .._models import BaseModel

__all__ = ["CrawlControls", "Source", "SourceUnionMember0", "SourceUnionMember1"]


class SourceUnionMember0(BaseModel):
    type: Literal["start_url"]

    url: str
    """Page the crawl started from."""


class SourceUnionMember1(BaseModel):
    domain: str
    """Domain whose sitemap supplied the pages."""

    type: Literal["sitemap"]


Source: TypeAlias = Union[SourceUnionMember0, SourceUnionMember1]


class CrawlControls(BaseModel):
    """
    The crawl controls as submitted, so the limits requested can be compared against what the crawl reached.
    """

    follow_subdomains: bool
    """Whether links to subdomains were followed. Always false for a sitemap crawl."""

    max_depth: Optional[int] = None
    """Link depth limit.

    Always 0 for a sitemap crawl, which never follows links off its URLs; null when
    a `start_url` crawl set no limit.
    """

    max_pages: int
    """The `maxUrls` submitted with the crawl.

    A sitemap crawl scrapes only the URLs its sitemap actually lists, up to this
    many, so `input.reserved` is often lower.
    """

    source: Source
    """Where the crawl started."""

    url_pattern: Optional[str] = None
    """RE2 pattern URLs had to match to be crawled. Null when the crawl set none."""
