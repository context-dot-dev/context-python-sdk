# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "NewsSearchParams",
    "SearchBy",
    "SearchByEntity",
    "SearchByEntityNewsSearchEntityByName",
    "SearchByEntityNewsSearchEntityByDomain",
    "SearchByEntityNewsSearchEntityByTicker",
    "SearchByEntityNewsSearchEntityByIsin",
    "FilterBy",
    "FilterByDate",
    "SortBy",
]


class NewsSearchParams(TypedDict, total=False):
    search_by: Required[Annotated[SearchBy, PropertyInfo(alias="searchBy")]]
    """What to search for."""

    cursor: Optional[str]
    """Opaque next_cursor from the previous response, or null for the first page."""

    filter_by: Annotated[FilterBy, PropertyInfo(alias="filterBy")]
    """Optional result filters.

    Use at most one of sourceDomain, sourceCountry, articleLanguage, or articleType.
    A date range may accompany that category; date.from must not exceed date.to.
    """

    limit: int
    """Maximum results to return. Defaults to 10."""

    sort_by: Annotated[SortBy, PropertyInfo(alias="sortBy")]
    """Result ordering. Defaults to newest."""

    tags: SequenceNotStr[str]
    """Labels for filtering usage in the dashboard."""


class SearchByEntityNewsSearchEntityByName(TypedDict, total=False):
    """Identify the company by name."""

    name: Required[str]
    """Company name."""

    type: Required[Literal["name"]]
    """Use `name` to identify the company by name."""


class SearchByEntityNewsSearchEntityByDomain(TypedDict, total=False):
    """Identify the company by website domain."""

    domain: Required[str]
    """Company website domain, such as apple.com."""

    type: Required[Literal["domain"]]
    """Use `domain` to identify the company by website domain."""


class SearchByEntityNewsSearchEntityByTicker(TypedDict, total=False):
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


class SearchByEntityNewsSearchEntityByIsin(TypedDict, total=False):
    """Identify the company by International Securities Identification Number."""

    isin: Required[str]
    """International Securities Identification Number."""

    type: Required[Literal["isin"]]
    """Use `isin` to identify the company by its securities identifier."""


SearchByEntity: TypeAlias = Union[
    SearchByEntityNewsSearchEntityByName,
    SearchByEntityNewsSearchEntityByDomain,
    SearchByEntityNewsSearchEntityByTicker,
    SearchByEntityNewsSearchEntityByIsin,
]


class SearchBy(TypedDict, total=False):
    """What to search for."""

    entity: Required[SearchByEntity]
    """The company to search news for, identified by name, domain, ticker, or ISIN."""

    type: Required[Literal["entity"]]
    """How to search. Only entity search is supported."""


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
        List[Literal["ar", "de", "en", "es", "fr", "hi", "it", "ja", "ko", "nl", "pt", "ru", "zh"]],
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
    """Result ordering. Defaults to newest."""

    type: Required[Literal["relevance", "newest"]]
    """Result ordering."""
