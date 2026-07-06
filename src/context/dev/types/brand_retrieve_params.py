# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "BrandRetrieveParams",
    "BrandRetrieveByDomainRequest",
    "BrandRetrieveByNameRequest",
    "BrandRetrieveByEmailRequest",
    "BrandRetrieveByTickerRequest",
    "BrandRetrieveFromTransactionRequest",
]


class BrandRetrieveByDomainRequest(TypedDict, total=False):
    domain: Required[str]
    """Domain name to retrieve brand data for (e.g., 'stripe.com')."""

    type: Required[Literal["by_domain"]]
    """Discriminator for domain-based brand retrieval."""

    force_language: Literal[
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

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class BrandRetrieveByNameRequest(TypedDict, total=False):
    name: Required[str]
    """Company name to retrieve brand data for (e.g., 'Apple Inc')."""

    type: Required[Literal["by_name"]]
    """Discriminator for name-based brand retrieval."""

    country_gl: str
    """
    Optional country code hint (GL parameter) to specify the country when looking up
    by company name.
    """

    force_language: Literal[
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

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class BrandRetrieveByEmailRequest(TypedDict, total=False):
    email: Required[str]
    """Email address to retrieve brand data for (e.g., 'jane@stripe.com')."""

    type: Required[Literal["by_email"]]
    """Discriminator for email-based brand retrieval."""

    force_language: Literal[
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

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data.
    """

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class BrandRetrieveByTickerRequest(TypedDict, total=False):
    ticker: Required[str]
    """Stock ticker symbol to retrieve brand data for (e.g., 'AAPL')."""

    type: Required[Literal["by_ticker"]]
    """Discriminator for ticker-based brand retrieval."""

    force_language: Literal[
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

    max_age_ms: Annotated[int, PropertyInfo(alias="maxAgeMs")]
    """
    Maximum age in milliseconds for cached brand data before the API performs a hard
    refresh. Defaults to 3 months (7776000000 ms). Values below 1 day (86400000 ms)
    are clamped to 1 day; values above 1 year (31536000000 ms) are clamped to 1
    year.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data.
    """

    ticker_exchange: str
    """Optional stock exchange for the ticker. Defaults to NASDAQ if not specified."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


class BrandRetrieveFromTransactionRequest(TypedDict, total=False):
    transaction_info: Required[str]
    """Transaction information to identify the brand."""

    type: Required[Literal["by_transaction"]]
    """Discriminator for transaction-based brand retrieval."""

    city: str
    """Optional city name to prioritize when searching for the brand."""

    country_gl: str
    """
    Optional country code hint (GL parameter) to specify the country when
    identifying a transaction.
    """

    force_language: Literal[
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

    high_confidence_only: bool
    """
    When set to true, the API performs additional verification to ensure the
    identified brand matches the transaction with high confidence.
    """

    max_speed: Annotated[bool, PropertyInfo(alias="maxSpeed")]
    """Optional parameter to optimize the API call for maximum speed.

    When set to true, the API will skip time-consuming operations for faster
    response at the cost of less comprehensive data.
    """

    mcc: int
    """
    Optional Merchant Category Code (MCC) to help identify the business category or
    industry.
    """

    phone: float
    """Optional phone number from the transaction to help verify brand match."""

    timeout_ms: Annotated[int, PropertyInfo(alias="timeoutMS")]
    """Optional timeout in milliseconds for the request.

    If the request takes longer than this value, it will be aborted with a 408
    status code. Maximum allowed value is 300000ms (5 minutes).
    """


BrandRetrieveParams: TypeAlias = Union[
    BrandRetrieveByDomainRequest,
    BrandRetrieveByNameRequest,
    BrandRetrieveByEmailRequest,
    BrandRetrieveByTickerRequest,
    BrandRetrieveFromTransactionRequest,
]
