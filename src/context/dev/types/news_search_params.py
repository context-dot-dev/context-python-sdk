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
    What to search for: a specific company, or a natural-language query across all
    news.
    """

    cursor: Optional[str]
    """Opaque next_cursor from the previous response, or null for the first page."""

    filter_by: Annotated[FilterBy, PropertyInfo(alias="filterBy")]
    """Optional result filters.

    Use at most one of sourceDomain, sourceCountry, articleLanguage, or articleType.
    A date range may accompany that category; date.from must not exceed date.to.
    """

    limit: int
    """Maximum results to return. Defaults to 10."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply. A URL must pass every policy."""

    sort_by: Annotated[SortBy, PropertyInfo(alias="sortBy")]
    """Result ordering.

    Defaults to newest for entity searches. Natural-language searches are always
    ordered by relevance.
    """

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


class SearchByNewsSearchByNaturalLanguage(TypedDict, total=False):
    """Search all news with a plain-language query.

    Returns up to 100 matches, ordered by relevance.
    """

    query: Required[str]
    """
    What to search for, in plain language, such as "chip export restrictions to
    China".
    """

    type: Required[Literal["natural_language"]]
    """Use `natural_language` to search all news with a plain-language query."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByName(TypedDict, total=False):
    """Identify the company by name."""

    name: Required[str]
    """Company name."""

    type: Required[Literal["name"]]
    """Use `name` to identify the company by name."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByDomain(TypedDict, total=False):
    """Identify the company by website domain."""

    domain: Required[str]
    """Company website domain, such as apple.com."""

    type: Required[Literal["domain"]]
    """Use `domain` to identify the company by website domain."""


class SearchByNewsSearchByEntityEntityNewsSearchEntityByTicker(TypedDict, total=False):
    """Identify the company by stock ticker, optionally scoped to an exchange."""

    ticker: Required[str]
    """Public-company ticker."""

    type: Required[Literal["ticker"]]
    """Use `ticker` to identify a publicly traded company."""

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
    """
    Stock exchange the ticker trades on, used to disambiguate tickers listed on
    multiple exchanges.
    """


class SearchByNewsSearchByEntityEntityNewsSearchEntityByIsin(TypedDict, total=False):
    """Identify the company by International Securities Identification Number."""

    isin: Required[str]
    """International Securities Identification Number."""

    type: Required[Literal["isin"]]
    """Use `isin` to identify the company by its securities identifier."""


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
    """Use `entity` to find news about a specific company."""


SearchBy: TypeAlias = Union[SearchByNewsSearchByNaturalLanguage, SearchByNewsSearchByEntity]

_FilterByDateReservedKeywords = TypedDict(
    "_FilterByDateReservedKeywords",
    {
        "from": int,
    },
    total=False,
)


class FilterByDate(_FilterByDateReservedKeywords, total=False):
    """Published-at window in epoch milliseconds. from must be before or equal to to."""

    to: int
    """Inclusive end of the published-at window, in epoch milliseconds."""


class FilterBy(TypedDict, total=False):
    """Optional result filters.

    Use at most one of sourceDomain, sourceCountry, articleLanguage, or articleType. A date range may accompany that category; date.from must not exceed date.to.
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
    """Article languages to include. Up to 3."""

    article_type: Annotated[
        List[Literal["editorial", "press_release", "regulatory_filing", "advisory"]], PropertyInfo(alias="articleType")
    ]
    """Article types to include. Up to 3."""

    date: FilterByDate
    """Published-at window in epoch milliseconds. from must be before or equal to to."""

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
    """Publisher countries to include, as lowercase ISO 3166-1 alpha-2 codes. Up to 3."""

    source_domain: Annotated[SequenceNotStr[str], PropertyInfo(alias="sourceDomain")]
    """Publisher domains to include. Up to 3."""


class SortBy(TypedDict, total=False):
    """Result ordering.

    Defaults to newest for entity searches. Natural-language searches are always ordered by relevance.
    """

    type: Required[Literal["relevance", "newest"]]
    """Result ordering."""
