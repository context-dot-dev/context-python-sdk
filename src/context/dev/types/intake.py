# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from .._models import BaseModel

__all__ = ["Intake"]


class Intake(BaseModel):
    """What the submission accepted."""

    duplicates: int
    """URLs dropped before reserving because another entry resolved to the same page.

    Non-zero for sitemap crawls too, whose sitemaps routinely list a page more than
    once.
    """

    invalid: Optional[int] = None
    """Rejected input URLs; `null` for a crawl."""

    reserved: int
    """Pages accepted; progress counts toward this total."""

    reserved_is_ceiling: bool
    """True when `reserved` is a crawl ceiling; false when it is an exact URL count."""

    submitted: Optional[int] = None
    """URLs in the list you sent, before validation and de-duplication.

    Null for a crawl, which is given a source rather than a list.
    """
