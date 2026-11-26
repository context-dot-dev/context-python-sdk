# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from .._utils import PropertyInfo
from .._models import BaseModel

__all__ = [
    "CrawlControls",
    "Exclude",
    "ExcludeCrawlRegexMatcher",
    "ExcludeCrawlProductMatcher",
    "Follow",
    "FollowCrawlRegexMatcher",
    "FollowCrawlPaginationMatcher",
    "FollowCrawlProductMatcher",
    "Scrape",
    "ScrapeCrawlRegexMatcher",
    "ScrapeCrawlProductMatcher",
    "Source",
    "SourceStartURL",
    "SourceSitemap",
]


class ExcludeCrawlRegexMatcher(BaseModel):
    """Pages whose URL matches a regex pattern."""

    kind: Literal["regex"]
    """Match pages by URL pattern."""

    pattern: str
    """Regex pattern for the page URL."""


class ExcludeCrawlProductMatcher(BaseModel):
    """Product detail pages."""

    kind: Literal["product"]
    """Match product detail pages."""


Exclude: TypeAlias = Annotated[
    Union[ExcludeCrawlRegexMatcher, ExcludeCrawlProductMatcher], PropertyInfo(discriminator="kind")
]


class FollowCrawlRegexMatcher(BaseModel):
    """Pages whose URL matches a regex pattern."""

    kind: Literal["regex"]
    """Match pages by URL pattern."""

    pattern: str
    """Regex pattern for the page URL."""


class FollowCrawlPaginationMatcher(BaseModel):
    """Further pages of a paginated list, such as page 2 of a catalog."""

    kind: Literal["pagination"]
    """Match the further pages of a paginated list."""


class FollowCrawlProductMatcher(BaseModel):
    """Product detail pages."""

    kind: Literal["product"]
    """Match product detail pages."""


Follow: TypeAlias = Annotated[
    Union[FollowCrawlRegexMatcher, FollowCrawlPaginationMatcher, FollowCrawlProductMatcher],
    PropertyInfo(discriminator="kind"),
]


class ScrapeCrawlRegexMatcher(BaseModel):
    """Pages whose URL matches a regex pattern."""

    kind: Literal["regex"]
    """Match pages by URL pattern."""

    pattern: str
    """Regex pattern for the page URL."""


class ScrapeCrawlProductMatcher(BaseModel):
    """Product detail pages."""

    kind: Literal["product"]
    """Match product detail pages."""


Scrape: TypeAlias = Annotated[
    Union[ScrapeCrawlRegexMatcher, ScrapeCrawlProductMatcher], PropertyInfo(discriminator="kind")
]


class SourceStartURL(BaseModel):
    """The crawl discovered pages by following links from one URL."""

    type: Literal["start_url"]

    url: str
    """Page the crawl started from."""


class SourceSitemap(BaseModel):
    """The crawl scraped the pages listed in the domain's sitemap."""

    domain: str
    """Domain whose sitemap supplied the pages."""

    type: Literal["sitemap"]


Source: TypeAlias = Union[SourceStartURL, SourceSitemap]


class CrawlControls(BaseModel):
    """Crawl settings as submitted."""

    exclude: Optional[List[Exclude]] = None
    """Pages the crawl skipped. Null when it skipped none."""

    exclude_url_pattern: Optional[str] = None
    """Regex pattern URLs must not match to be crawled. Null when the crawl set none."""

    follow: Optional[List[Follow]] = None
    """Links the crawl followed. Null when it followed every link."""

    follow_subdomains: bool
    """Whether links to subdomains were followed. Always false for a sitemap crawl."""

    languages: Union[
        Literal["same_as_start_url"],
        List[
            Literal[
                "am",
                "ar",
                "az",
                "be",
                "bg",
                "bn",
                "ca",
                "ceb",
                "cs",
                "cy",
                "da",
                "de",
                "el",
                "en",
                "es",
                "et",
                "eu",
                "fa",
                "fi",
                "fr",
                "gu",
                "ha",
                "haw",
                "he",
                "hi",
                "hr",
                "hu",
                "hy",
                "id",
                "is",
                "it",
                "ja",
                "ka",
                "kk",
                "kn",
                "ko",
                "ku",
                "ky",
                "lo",
                "lt",
                "lv",
                "mk",
                "ml",
                "mn",
                "mr",
                "ms",
                "ne",
                "nl",
                "no",
                "or",
                "pa",
                "pl",
                "ps",
                "pt",
                "ro",
                "ru",
                "sk",
                "sl",
                "so",
                "sq",
                "sr",
                "sv",
                "sw",
                "ta",
                "te",
                "th",
                "tl",
                "tr",
                "uk",
                "ur",
                "uz",
                "vi",
                "yo",
                "zh",
            ]
        ],
        None,
    ] = None
    """Languages whose pages were followed; null when all languages were."""

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

    scrape: Optional[List[Scrape]] = None
    """Pages the crawl returned. Null when it returned every fetched page."""

    source: Source
    """Where the crawl started."""

    url_pattern: Optional[str] = None
    """Regex pattern URLs had to match to be crawled. Null when the crawl set none."""
