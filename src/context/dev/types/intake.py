# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Intake"]


class Intake(BaseModel):
    """What submission took in, and what it charged for."""

    duplicates: int
    """URLs dropped before reserving because another entry resolved to the same page.

    Non-zero for sitemap crawls too, whose sitemaps routinely list a page more than
    once.
    """

    invalid: Optional[int] = None
    """
    URLs from your list rejected as unusable; the same ones are itemised in
    `invalid_urls` at submission. Null for a crawl — a crawl that resolves no usable
    page is rejected outright with a 400 rather than accepted with an empty list.
    """

    reserved: int
    """Pages credits were reserved for.

    Everything else — progress, the refund, the completion percentage — is measured
    against this.
    """

    reserved_is_ceiling: bool
    """Whether `reserved` is an upper bound the batch may finish under.

    True only for a crawl that follows links, whose reachable page count is
    unknowable until it runs. False for a scrape and for a sitemap crawl, where
    `reserved` is an exact page count.
    """

    submitted: Optional[int] = None
    """URLs in the list you sent, before validation and de-duplication.

    Null for a crawl, which is given a source rather than a list.
    """
