# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "NewsSearchParams",
    "SearchBy",
    "SearchByNewsSearchByNaturalLanguage",
    "SearchByNewsSearchByEntity",
    "SearchByNewsSearchByEntityEntity",
    "SearchByNewsSearchByEntityEntityNewsSearchEntityByName",
    "SearchByNewsSearchByEntityEntityNewsSearchEntityByDomain",
    "SearchByNewsSearchByEntityEntityNewsSearchEntityByTicker",
    "SearchByNewsSearchByEntityEntityNewsSearchEntityByIsin",
    "FilterBy",
    "FilterByDate",
    "SortBy",
]


class NewsSearchParams(TypedDict, total=False):
    search_by: Required[Annotated[SearchBy, PropertyInfo(alias="searchBy")]]
    """
    What to search for: news about a specific company, or a natural-language query
    across all news.
    """

    cursor: Optional[str]
    """Cursor from the previous page's `next_cursor`. Omit for the first page."""

    filter_by: Annotated[FilterBy, PropertyInfo(alias="filterBy")]
    """Filters for the results.

    Use at most one of `sourceDomain`, `sourceCountry`, `articleLanguage`, or
    `articleType`, optionally combined with `date`.
    """

    limit: int
    """Maximum number of articles to return per page."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    sort_by: Annotated[SortBy, PropertyInfo(alias="sortBy")]
    """How to order results.

    Company searches default to `newest`; natural-language searches always use
    `relevance`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """


class SearchByNewsSearchByNaturalLanguage(TypedDict, total=False):
    """Search all news with a plain-language query.

    Returns up to 100 matches, ordered by relevance.
    """

    query: Required[str]
    """
    What to search for, in plain language, such as
    `chip export restrictions to China`.
    """

    type: Required[Literal["natural_language"]]
    """Set to `natural_language` to search all news with a plain-language query."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByName(TypedDict, total=False):
    """Identify the company by name."""

    name: Required[str]
    """Company name, such as `Stripe`."""

    type: Required[Literal["name"]]
    """Set to `name` to identify the company by name."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByDomain(TypedDict, total=False):
    """Identify the company by website domain."""

    domain: Required[str]
    """Company website domain, such as `apple.com`."""

    type: Required[Literal["domain"]]
    """Set to `domain` to identify the company by website domain."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByTicker(TypedDict, total=False):
    """Identify the company by stock ticker, optionally on a specific exchange."""

    ticker: Required[str]
    """Stock ticker symbol, such as `AAPL`."""

    type: Required[Literal["ticker"]]
    """Set to `ticker` to identify a publicly traded company."""

    exchange: Literal[
        "AMEX",
        "AMS",
        "AQS",
        "ASX",
        "ATH",
        "BER",
        "BME",
        "BRU",
        "BSE",
        "BUD",
        "BUE",
        "BVC",
        "CBOE",
        "CNQ",
        "CPH",
        "DFM",
        "DOH",
        "DUB",
        "DUS",
        "DXE",
        "EGX",
        "FSX",
        "HAM",
        "HEL",
        "HKSE",
        "HOSE",
        "ICE",
        "IOB",
        "IST",
        "JKT",
        "JNB",
        "JPX",
        "KLS",
        "KOE",
        "KSC",
        "KUW",
        "LIS",
        "LSE",
        "MCX",
        "MEX",
        "MIL",
        "MUN",
        "NASDAQ",
        "NEO",
        "NSE",
        "NYSE",
        "NZE",
        "OSL",
        "OTC",
        "PAR",
        "PNK",
        "PRA",
        "RIS",
        "SAO",
        "SAU",
        "SES",
        "SET",
        "SGO",
        "SHH",
        "SHZ",
        "SIX",
        "STO",
        "STU",
        "TAI",
        "TAL",
        "TLV",
        "TSX",
        "TSXV",
        "TWO",
        "VIE",
        "WSE",
        "XETRA",
    ]
    """Exchange the ticker trades on.

    Use it when the same ticker is listed on more than one exchange.
    """


class SearchByNewsSearchByEntityEntityNewsSearchEntityByIsin(TypedDict, total=False):
    """Identify the company by International Securities Identification Number (ISIN)."""

    isin: Required[str]
    """International Securities Identification Number, such as `US0378331005`."""

    type: Required[Literal["isin"]]
    """
    Set to `isin` to identify the company by its International Securities
    Identification Number.
    """


SearchByNewsSearchByEntityEntity: TypeAlias = Union[
    SearchByNewsSearchByEntityEntityNewsSearchEntityByName,
    SearchByNewsSearchByEntityEntityNewsSearchEntityByDomain,
    SearchByNewsSearchByEntityEntityNewsSearchEntityByTicker,
    SearchByNewsSearchByEntityEntityNewsSearchEntityByIsin,
]


class SearchByNewsSearchByEntity(TypedDict, total=False):
    """Find news about a specific company."""

    entity: Required[SearchByNewsSearchByEntityEntity]
    """The company to search news for, identified by name, domain, ticker, or ISIN."""

    type: Required[Literal["entity"]]
    """Set to `entity` to find news about a specific company."""


SearchBy: TypeAlias = Union[SearchByNewsSearchByNaturalLanguage, SearchByNewsSearchByEntity]

_FilterByDateReservedKeywords = TypedDict(
    "_FilterByDateReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class FilterByDate(_FilterByDateReservedKeywords, total=False):
    """Publish date range, in epoch milliseconds. `from` must not be later than `to`."""

    to: int
    """Inclusive end of the publish date range, in epoch milliseconds."""


class FilterBy(TypedDict, total=False):
    """Filters for the results.

    Use at most one of `sourceDomain`, `sourceCountry`, `articleLanguage`, or `articleType`, optionally combined with `date`.
    """

    article_language: Annotated[
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
        PropertyInfo(alias="articleLanguage"),
    ]
    """Only return articles in these languages, as ISO 639 codes such as `en`."""

    article_type: Annotated[
        List[Literal["editorial", "press_release", "regulatory_filing", "advisory"]], PropertyInfo(alias="articleType")
    ]
    """Only return these types of coverage, such as `press_release`."""

    date: FilterByDate
    """Publish date range, in epoch milliseconds. `from` must not be later than `to`."""

    source_country: Annotated[
        List[
            Literal[
                "ae",
                "ar",
                "au",
                "ca",
                "cg",
                "ch",
                "cl",
                "cz",
                "de",
                "fi",
                "fr",
                "gb",
                "hk",
                "il",
                "in",
                "jp",
                "kr",
                "mx",
                "ng",
                "nl",
                "pk",
                "qa",
                "sa",
                "se",
                "sg",
                "us",
                "za",
            ]
        ],
        PropertyInfo(alias="sourceCountry"),
    ]
    """
    Only return articles from publishers in these countries, as ISO 3166-1 alpha-2
    codes such as `us`.
    """

    source_domain: Annotated[SequenceNotStr[str], PropertyInfo(alias="sourceDomain")]
    """Only return articles from these publisher domains, such as `reuters.com`."""


class SortBy(TypedDict, total=False):
    """How to order results.

    Company searches default to `newest`; natural-language searches always use `relevance`.
    """

    type: Required[Literal["relevance", "newest"]]
    """
    `newest` puts the most recently published articles first; `relevance` puts the
    closest matches first.
    """
