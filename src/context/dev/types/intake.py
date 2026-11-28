# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Intake"]


class Intake(BaseModel):
    """Page counts from your submission."""

    duplicates: int
    """URLs dropped because another entry resolved to the same page.

    Sitemap crawls report duplicates too, since sitemaps often list a page more than
    once.
    """

    invalid: Optional[int] = None
    """URLs rejected as invalid. `null` for a crawl."""

    reserved: int
    """Pages accepted for scraping. `progress` counts toward this total."""

    reserved_is_ceiling: bool
    """
    `true` when `reserved` is a crawl ceiling, `false` when it is an exact URL
    count.
    """

    submitted: Optional[int] = None
    """URLs in your list before validation and de-duplication. `null` for a crawl."""
