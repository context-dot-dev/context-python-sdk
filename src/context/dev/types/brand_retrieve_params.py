# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = [
    "BrandRetrieveParams",
    "BrandRetrieveByDomainRequest",
    "BrandRetrieveByDomainRequestTimeoutOpts",
    "BrandRetrieveByNameRequest",
    "BrandRetrieveByNameRequestTimeoutOpts",
    "BrandRetrieveByEmailRequest",
    "BrandRetrieveByEmailRequestTimeoutOpts",
    "BrandRetrieveByTickerRequest",
    "BrandRetrieveByTickerRequestTimeoutOpts",
    "BrandRetrieveByDirectURLRequest",
    "BrandRetrieveByDirectURLRequestTimeoutOpts",
    "BrandRetrieveFromTransactionRequest",
    "BrandRetrieveFromTransactionRequestTimeoutOpts",
]


class BrandRetrieveByDomainRequest(TypedDict, total=False):
    domain: Required[str]
    """Domain of the brand, such as `stripe.com`."""

    type: Required[Literal["by_domain"]]
    """Set to `by_domain` to look up a brand by domain."""

    force_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ]
    """Translate the brand's `title`, `description`, and `slogan` into this language."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of cached brand data, in milliseconds.

    `0` always fetches fresh. Defaults to 90 days (7776000000 ms). Values above 1
    year (31536000000 ms) are capped at 1 year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Skip slower enrichment steps for a faster, less detailed response."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[BrandRetrieveByDomainRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveByDomainRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


class BrandRetrieveByNameRequest(TypedDict, total=False):
    name: Required[str]
    """Company name, such as `Apple Inc`."""

    type: Required[Literal["by_name"]]
    """Set to `by_name` to look up a brand by company name."""

    country: Literal[
        "af",
        "al",
        "dz",
        "as",
        "ad",
        "ao",
        "ai",
        "aq",
        "ag",
        "ar",
        "am",
        "aw",
        "au",
        "at",
        "az",
        "bs",
        "bh",
        "bd",
        "bb",
        "by",
        "be",
        "bz",
        "bj",
        "bm",
        "bt",
        "bo",
        "ba",
        "bw",
        "bv",
        "br",
        "io",
        "bn",
        "bg",
        "bf",
        "bi",
        "kh",
        "cm",
        "ca",
        "cv",
        "ky",
        "cf",
        "td",
        "cl",
        "cn",
        "cx",
        "cc",
        "co",
        "km",
        "cg",
        "cd",
        "ck",
        "cr",
        "ci",
        "hr",
        "cu",
        "cy",
        "cz",
        "dk",
        "dj",
        "dm",
        "do",
        "ec",
        "eg",
        "sv",
        "gq",
        "er",
        "ee",
        "et",
        "fk",
        "fo",
        "fj",
        "fi",
        "fr",
        "gf",
        "pf",
        "tf",
        "ga",
        "gm",
        "ge",
        "de",
        "gh",
        "gi",
        "gr",
        "gl",
        "gd",
        "gp",
        "gu",
        "gt",
        "gn",
        "gw",
        "gy",
        "ht",
        "hm",
        "va",
        "hn",
        "hk",
        "hu",
        "is",
        "in",
        "id",
        "ir",
        "iq",
        "ie",
        "il",
        "it",
        "jm",
        "jp",
        "jo",
        "kz",
        "ke",
        "ki",
        "kp",
        "kr",
        "kw",
        "kg",
        "la",
        "lv",
        "lb",
        "ls",
        "lr",
        "ly",
        "li",
        "lt",
        "lu",
        "mo",
        "mk",
        "mg",
        "mw",
        "my",
        "mv",
        "ml",
        "mt",
        "mh",
        "mq",
        "mr",
        "mu",
        "yt",
        "mx",
        "fm",
        "md",
        "mc",
        "mn",
        "ms",
        "ma",
        "mz",
        "mm",
        "na",
        "nr",
        "np",
        "nl",
        "an",
        "nc",
        "nz",
        "ni",
        "ne",
        "ng",
        "nu",
        "nf",
        "mp",
        "no",
        "om",
        "pk",
        "pw",
        "ps",
        "pa",
        "pg",
        "py",
        "pe",
        "ph",
        "pn",
        "pl",
        "pt",
        "pr",
        "qa",
        "re",
        "ro",
        "ru",
        "rw",
        "sh",
        "kn",
        "lc",
        "pm",
        "vc",
        "ws",
        "sm",
        "st",
        "sa",
        "sn",
        "rs",
        "sc",
        "sl",
        "sg",
        "sk",
        "si",
        "sb",
        "so",
        "za",
        "gs",
        "es",
        "lk",
        "sd",
        "sr",
        "sj",
        "sz",
        "se",
        "ch",
        "sy",
        "tw",
        "tj",
        "tz",
        "th",
        "tl",
        "tg",
        "tk",
        "to",
        "tt",
        "tn",
        "tr",
        "tm",
        "tc",
        "tv",
        "ug",
        "ua",
        "ae",
        "gb",
        "us",
        "um",
        "uy",
        "uz",
        "vu",
        "ve",
        "vn",
        "vg",
        "vi",
        "wf",
        "eh",
        "ye",
        "zm",
        "zw",
    ]
    """Lowercase ISO 3166-1 alpha-2 country code, such as `us`."""

    force_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ]
    """Translate the brand's `title`, `description`, and `slogan` into this language."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of cached brand data, in milliseconds.

    `0` always fetches fresh. Defaults to 90 days (7776000000 ms). Values above 1
    year (31536000000 ms) are capped at 1 year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Skip slower enrichment steps for a faster, less detailed response."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[BrandRetrieveByNameRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveByNameRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


class BrandRetrieveByEmailRequest(TypedDict, total=False):
    email: Required[str]
    """Work email address, such as `jane@stripe.com`.

    The brand is looked up from its domain.
    """

    type: Required[Literal["by_email"]]
    """Set to `by_email` to look up a brand from a work email address."""

    force_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ]
    """Translate the brand's `title`, `description`, and `slogan` into this language."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of cached brand data, in milliseconds.

    `0` always fetches fresh. Defaults to 90 days (7776000000 ms). Values above 1
    year (31536000000 ms) are capped at 1 year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Skip slower enrichment steps for a faster, less detailed response."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[BrandRetrieveByEmailRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveByEmailRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


class BrandRetrieveByTickerRequest(TypedDict, total=False):
    ticker: Required[str]
    """Stock ticker symbol, such as `AAPL`."""

    type: Required[Literal["by_ticker"]]
    """Set to `by_ticker` to look up a brand by stock ticker."""

    force_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ]
    """Translate the brand's `title`, `description`, and `slogan` into this language."""

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """Maximum age of cached brand data, in milliseconds.

    `0` always fetches fresh. Defaults to 90 days (7776000000 ms). Values above 1
    year (31536000000 ms) are capped at 1 year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Skip slower enrichment steps for a faster, less detailed response."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    ticker_exchange: Literal[
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
    """Stock exchange code, such as `NASDAQ` or `LSE`."""

    timeout_opts: Annotated[BrandRetrieveByTickerRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveByTickerRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


class BrandRetrieveByDirectURLRequest(TypedDict, total=False):
    direct_url: Required[str]
    """
    Full `http` or `https` URL of the page to read, such as
    `https://stripe.com/enterprise`. Only this page is fetched.
    """

    type: Required[Literal["by_direct_url"]]
    """Set to `by_direct_url` to extract brand data from a single page."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[BrandRetrieveByDirectURLRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveByDirectURLRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


class BrandRetrieveFromTransactionRequest(TypedDict, total=False):
    transaction_info: Required[str]
    """
    Transaction descriptor from a card or bank statement, such as `SQ *COFFEE SHOP`.
    """

    type: Required[Literal["by_transaction"]]
    """
    Set to `by_transaction` to identify the merchant behind a transaction
    descriptor.
    """

    city: str
    """City where the transaction took place. Brands in this city are preferred."""

    country: Literal[
        "af",
        "al",
        "dz",
        "as",
        "ad",
        "ao",
        "ai",
        "aq",
        "ag",
        "ar",
        "am",
        "aw",
        "au",
        "at",
        "az",
        "bs",
        "bh",
        "bd",
        "bb",
        "by",
        "be",
        "bz",
        "bj",
        "bm",
        "bt",
        "bo",
        "ba",
        "bw",
        "bv",
        "br",
        "io",
        "bn",
        "bg",
        "bf",
        "bi",
        "kh",
        "cm",
        "ca",
        "cv",
        "ky",
        "cf",
        "td",
        "cl",
        "cn",
        "cx",
        "cc",
        "co",
        "km",
        "cg",
        "cd",
        "ck",
        "cr",
        "ci",
        "hr",
        "cu",
        "cy",
        "cz",
        "dk",
        "dj",
        "dm",
        "do",
        "ec",
        "eg",
        "sv",
        "gq",
        "er",
        "ee",
        "et",
        "fk",
        "fo",
        "fj",
        "fi",
        "fr",
        "gf",
        "pf",
        "tf",
        "ga",
        "gm",
        "ge",
        "de",
        "gh",
        "gi",
        "gr",
        "gl",
        "gd",
        "gp",
        "gu",
        "gt",
        "gn",
        "gw",
        "gy",
        "ht",
        "hm",
        "va",
        "hn",
        "hk",
        "hu",
        "is",
        "in",
        "id",
        "ir",
        "iq",
        "ie",
        "il",
        "it",
        "jm",
        "jp",
        "jo",
        "kz",
        "ke",
        "ki",
        "kp",
        "kr",
        "kw",
        "kg",
        "la",
        "lv",
        "lb",
        "ls",
        "lr",
        "ly",
        "li",
        "lt",
        "lu",
        "mo",
        "mk",
        "mg",
        "mw",
        "my",
        "mv",
        "ml",
        "mt",
        "mh",
        "mq",
        "mr",
        "mu",
        "yt",
        "mx",
        "fm",
        "md",
        "mc",
        "mn",
        "ms",
        "ma",
        "mz",
        "mm",
        "na",
        "nr",
        "np",
        "nl",
        "an",
        "nc",
        "nz",
        "ni",
        "ne",
        "ng",
        "nu",
        "nf",
        "mp",
        "no",
        "om",
        "pk",
        "pw",
        "ps",
        "pa",
        "pg",
        "py",
        "pe",
        "ph",
        "pn",
        "pl",
        "pt",
        "pr",
        "qa",
        "re",
        "ro",
        "ru",
        "rw",
        "sh",
        "kn",
        "lc",
        "pm",
        "vc",
        "ws",
        "sm",
        "st",
        "sa",
        "sn",
        "rs",
        "sc",
        "sl",
        "sg",
        "sk",
        "si",
        "sb",
        "so",
        "za",
        "gs",
        "es",
        "lk",
        "sd",
        "sr",
        "sj",
        "sz",
        "se",
        "ch",
        "sy",
        "tw",
        "tj",
        "tz",
        "th",
        "tl",
        "tg",
        "tk",
        "to",
        "tt",
        "tn",
        "tr",
        "tm",
        "tc",
        "tv",
        "ug",
        "ua",
        "ae",
        "gb",
        "us",
        "um",
        "uy",
        "uz",
        "vu",
        "ve",
        "vn",
        "vg",
        "vi",
        "wf",
        "eh",
        "ye",
        "zm",
        "zw",
    ]
    """Lowercase ISO 3166-1 alpha-2 country code, such as `us`."""

    force_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ]
    """Translate the brand's `title`, `description`, and `slogan` into this language."""

    high_confidence_only: bool
    """
    Run extra verification so the returned brand matches the transaction with high
    confidence.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Skip slower enrichment steps for a faster, less detailed response."""

    mcc: Union[str, float]
    """Merchant Category Code (MCC) from the transaction.

    Helps identify the type of business.
    """

    phone: Union[str, float]
    """Merchant phone number from the transaction. Helps confirm the match."""

    policies: SequenceNotStr[str]
    """Access policy IDs to apply; each URL must pass all of them.

    Requires access policies enabled for your organization; otherwise returns
    `ACCESS_POLICIES_NOT_ENABLED`.
    """

    tags: SequenceNotStr[str]
    """Labels for this request.

    Filter usage and request logs by them in the dashboard or with `GET /org/logs`.
    """

    timeout_opts: Annotated[BrandRetrieveFromTransactionRequestTimeoutOpts, PropertyInfo(alias="timeoutOpts")]
    """Request deadline and what to return when it passes."""

    zdr: Literal["enabled", "disabled"]
    """
    `enabled` turns off request logs and traces and keeps request and response
    content out of usage logs. Brand data and hosted assets may still be stored.
    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


class BrandRetrieveFromTransactionRequestTimeoutOpts(TypedDict, total=False):
    """Request deadline and what to return when it passes."""

    milliseconds: Required[int]
    """Deadline in milliseconds."""

    behavior: Literal["fail", "return-partial"]
    """`fail` returns 408 at the deadline.

    `return-partial` returns the results collected so far and marks the response as
    partial.
    """


BrandRetrieveParams: TypeAlias = Union[
    BrandRetrieveByDomainRequest,
    BrandRetrieveByNameRequest,
    BrandRetrieveByEmailRequest,
    BrandRetrieveByTickerRequest,
    BrandRetrieveByDirectURLRequest,
    BrandRetrieveFromTransactionRequest,
]
