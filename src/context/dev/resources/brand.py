# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from typing_extensions import Literal, overload

import httpx

from ..types import brand_search_params, brand_retrieve_params, brand_retrieve_simplified_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import required_args, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.brand_search_response import BrandSearchResponse
from ..types.brand_retrieve_response import BrandRetrieveResponse
from ..types.brand_retrieve_simplified_response import BrandRetrieveSimplifiedResponse

__all__ = ["BrandResource", "AsyncBrandResource"]


class BrandResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return BrandResourceWithStreamingResponse(self)

    @overload
    def retrieve(
        self,
        *,
        domain: str,
        type: Literal["by_domain"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDomainRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'stripe.com').

          type: Discriminator for domain-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def retrieve(
        self,
        *,
        name: str,
        type: Literal["by_name"],
        country_gl: str | Omit = omit,
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByNameRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc').

          type: Discriminator for name-based brand retrieval.

          country_gl: Optional country code hint (GL parameter) to specify the country when looking up
              by company name.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def retrieve(
        self,
        *,
        email: str,
        type: Literal["by_email"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByEmailRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          email: Email address to retrieve brand data for (e.g., 'jane@stripe.com').

          type: Discriminator for email-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def retrieve(
        self,
        *,
        ticker: str,
        type: Literal["by_ticker"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker_exchange: str | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByTickerRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL').

          type: Discriminator for ticker-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          ticker_exchange: Optional stock exchange for the ticker. Defaults to NASDAQ if not specified.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def retrieve(
        self,
        *,
        direct_url: str,
        type: Literal["by_direct_url"],
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDirectURLRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          direct_url: Full http(s) URL to fetch brand data from (e.g.,
              'https://stripe.com/enterprise'). Only this URL is fetched — not the entire
              internet.

          type: Discriminator for direct-URL-based brand retrieval.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def retrieve(
        self,
        *,
        transaction_info: str,
        type: Literal["by_transaction"],
        city: str | Omit = omit,
        country_gl: str | Omit = omit,
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
        | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        max_speed: bool | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveFromTransactionRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          transaction_info: Transaction information to identify the brand.

          type: Discriminator for transaction-based brand retrieval.

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Optional country code hint (GL parameter) to specify the country when
              identifying a transaction.

          high_confidence_only: When set to true, the API performs additional verification to ensure the
              identified brand matches the transaction with high confidence.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business category or
              industry.

          phone: Optional phone number from the transaction to help verify brand match.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["domain", "type"],
        ["name", "type"],
        ["email", "type"],
        ["ticker", "type"],
        ["direct_url", "type"],
        ["transaction_info", "type"],
    )
    def retrieve(
        self,
        *,
        domain: str | Omit = omit,
        type: Literal["by_domain"]
        | Literal["by_name"]
        | Literal["by_email"]
        | Literal["by_ticker"]
        | Literal["by_direct_url"]
        | Literal["by_transaction"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDomainRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByNameRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByEmailRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByTickerRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByDirectURLRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveFromTransactionRequestTimeoutOpts
        | Omit = omit,
        name: str | Omit = omit,
        country_gl: str | Omit = omit,
        email: str | Omit = omit,
        ticker: str | Omit = omit,
        ticker_exchange: str | Omit = omit,
        direct_url: str | Omit = omit,
        transaction_info: str | Omit = omit,
        city: str | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        return self._post(
            "/brand/retrieve",
            body=maybe_transform(
                {
                    "domain": domain,
                    "type": type,
                    "force_language": force_language,
                    "max_age_ms": max_age_ms,
                    "max_speed": max_speed,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "name": name,
                    "country_gl": country_gl,
                    "email": email,
                    "ticker": ticker,
                    "ticker_exchange": ticker_exchange,
                    "direct_url": direct_url,
                    "transaction_info": transaction_info,
                    "city": city,
                    "high_confidence_only": high_confidence_only,
                    "mcc": mcc,
                    "phone": phone,
                },
                brand_retrieve_params.BrandRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    def retrieve_simplified(
        self,
        *,
        domain: str,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        timeout_opts: brand_retrieve_simplified_params.TimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. Optimized for faster
        responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          theme: Optional theme preference used when selecting brand assets.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "theme": theme,
                        "timeout_opts": timeout_opts,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )

    def search(
        self,
        *,
        query: str,
        autocomplete: bool | Omit = omit,
        query_by: List[Literal["name", "domain"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        typo_tolerance: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSearchResponse:
        """
        Search indexed brands by name or domain

        Args:
          query: Search term, matched against the fields selected by queryBy (e.g. 'nike',
              'nike.com', 'nik').

          autocomplete: Whether the search term matches by prefix, so partial words match as they are
              typed (e.g. 'nik' matches Nike). Set to false to match whole words only.

          query_by: Fields to match the search term against, as a comma-separated list or repeated
              parameter: 'name', 'domain', or both. Defaults to both.

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          typo_tolerance: Maximum number of typos tolerated when matching, from 0 to 2. Defaults to 0 (no
              typo tolerance).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/brand/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "query": query,
                        "autocomplete": autocomplete,
                        "query_by": query_by,
                        "tags": tags,
                        "typo_tolerance": typo_tolerance,
                    },
                    brand_search_params.BrandSearchParams,
                ),
            ),
            cast_to=BrandSearchResponse,
        )


class AsyncBrandResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBrandResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBrandResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBrandResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncBrandResourceWithStreamingResponse(self)

    @overload
    async def retrieve(
        self,
        *,
        domain: str,
        type: Literal["by_domain"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDomainRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          domain: Domain name to retrieve brand data for (e.g., 'stripe.com').

          type: Discriminator for domain-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def retrieve(
        self,
        *,
        name: str,
        type: Literal["by_name"],
        country_gl: str | Omit = omit,
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByNameRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          name: Company name to retrieve brand data for (e.g., 'Apple Inc').

          type: Discriminator for name-based brand retrieval.

          country_gl: Optional country code hint (GL parameter) to specify the country when looking up
              by company name.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def retrieve(
        self,
        *,
        email: str,
        type: Literal["by_email"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByEmailRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          email: Email address to retrieve brand data for (e.g., 'jane@stripe.com').

          type: Discriminator for email-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def retrieve(
        self,
        *,
        ticker: str,
        type: Literal["by_ticker"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        ticker_exchange: str | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByTickerRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          ticker: Stock ticker symbol to retrieve brand data for (e.g., 'AAPL').

          type: Discriminator for ticker-based brand retrieval.

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          ticker_exchange: Optional stock exchange for the ticker. Defaults to NASDAQ if not specified.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def retrieve(
        self,
        *,
        direct_url: str,
        type: Literal["by_direct_url"],
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDirectURLRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          direct_url: Full http(s) URL to fetch brand data from (e.g.,
              'https://stripe.com/enterprise'). Only this URL is fetched — not the entire
              internet.

          type: Discriminator for direct-URL-based brand retrieval.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def retrieve(
        self,
        *,
        transaction_info: str,
        type: Literal["by_transaction"],
        city: str | Omit = omit,
        country_gl: str | Omit = omit,
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
        | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        max_speed: bool | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveFromTransactionRequestTimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        """Retrieve logos, backdrops, colors, industry, description, and more.

        Provide
        exactly one lookup identifier in the request body: a domain, company name, email
        address, stock ticker, transaction descriptor, or direct URL. Note:
        `by_direct_url` fetches brand data only from the provided URL — not from the
        entire internet.

        Args:
          transaction_info: Transaction information to identify the brand.

          type: Discriminator for transaction-based brand retrieval.

          city: Optional city name to prioritize when searching for the brand.

          country_gl: Optional country code hint (GL parameter) to specify the country when
              identifying a transaction.

          high_confidence_only: When set to true, the API performs additional verification to ensure the
              identified brand matches the transaction with high confidence.

          max_speed: Optional parameter to optimize the API call for maximum speed. When set to true,
              the API will skip time-consuming operations for faster response at the cost of
              less comprehensive data.

          mcc: Optional Merchant Category Code (MCC) to help identify the business category or
              industry.

          phone: Optional phone number from the transaction to help verify brand match.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["domain", "type"],
        ["name", "type"],
        ["email", "type"],
        ["ticker", "type"],
        ["direct_url", "type"],
        ["transaction_info", "type"],
    )
    async def retrieve(
        self,
        *,
        domain: str | Omit = omit,
        type: Literal["by_domain"]
        | Literal["by_name"]
        | Literal["by_email"]
        | Literal["by_ticker"]
        | Literal["by_direct_url"]
        | Literal["by_transaction"],
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
        | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_speed: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: brand_retrieve_params.BrandRetrieveByDomainRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByNameRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByEmailRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByTickerRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveByDirectURLRequestTimeoutOpts
        | brand_retrieve_params.BrandRetrieveFromTransactionRequestTimeoutOpts
        | Omit = omit,
        name: str | Omit = omit,
        country_gl: str | Omit = omit,
        email: str | Omit = omit,
        ticker: str | Omit = omit,
        ticker_exchange: str | Omit = omit,
        direct_url: str | Omit = omit,
        transaction_info: str | Omit = omit,
        city: str | Omit = omit,
        high_confidence_only: bool | Omit = omit,
        mcc: Union[str, float] | Omit = omit,
        phone: Union[str, float] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveResponse:
        return await self._post(
            "/brand/retrieve",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "type": type,
                    "force_language": force_language,
                    "max_age_ms": max_age_ms,
                    "max_speed": max_speed,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                    "name": name,
                    "country_gl": country_gl,
                    "email": email,
                    "ticker": ticker,
                    "ticker_exchange": ticker_exchange,
                    "direct_url": direct_url,
                    "transaction_info": transaction_info,
                    "city": city,
                    "high_confidence_only": high_confidence_only,
                    "mcc": mcc,
                    "phone": phone,
                },
                brand_retrieve_params.BrandRetrieveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BrandRetrieveResponse,
        )

    async def retrieve_simplified(
        self,
        *,
        domain: str,
        max_age_ms: Optional[int] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        theme: Literal["light", "dark"] | Omit = omit,
        timeout_opts: brand_retrieve_simplified_params.TimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandRetrieveSimplifiedResponse:
        """
        Returns a simplified version of brand data containing only essential
        information: domain, title, colors, logos, and backdrops. Optimized for faster
        responses and reduced data transfer.

        Args:
          domain: Domain name to retrieve simplified brand data for

          max_age_ms: Maximum age in milliseconds for cached brand data before the API performs a hard
              refresh. Defaults to 3 months (7776000000 ms). Set to 0 to always perform a hard
              refresh. Negative values are clamped to 0; values above 1 year (31536000000 ms)
              are clamped to 1 year.

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          theme: Optional theme preference used when selecting brand assets.

          timeout_opts: Optional request deadline and behavior on timeout. For GET requests, use
              timeoutOpts[milliseconds]=30000&timeoutOpts[behavior]=fail or a JSON-encoded
              timeoutOpts object.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/retrieve-simplified",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "domain": domain,
                        "max_age_ms": max_age_ms,
                        "tags": tags,
                        "theme": theme,
                        "timeout_opts": timeout_opts,
                    },
                    brand_retrieve_simplified_params.BrandRetrieveSimplifiedParams,
                ),
            ),
            cast_to=BrandRetrieveSimplifiedResponse,
        )

    async def search(
        self,
        *,
        query: str,
        autocomplete: bool | Omit = omit,
        query_by: List[Literal["name", "domain"]] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        typo_tolerance: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BrandSearchResponse:
        """
        Search indexed brands by name or domain

        Args:
          query: Search term, matched against the fields selected by queryBy (e.g. 'nike',
              'nike.com', 'nik').

          autocomplete: Whether the search term matches by prefix, so partial words match as they are
              typed (e.g. 'nik' matches Nike). Set to false to match whole words only.

          query_by: Fields to match the search term against, as a comma-separated list or repeated
              parameter: 'name', 'domain', or both. Defaults to both.

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          typo_tolerance: Maximum number of typos tolerated when matching, from 0 to 2. Defaults to 0 (no
              typo tolerance).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/brand/search",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "query": query,
                        "autocomplete": autocomplete,
                        "query_by": query_by,
                        "tags": tags,
                        "typo_tolerance": typo_tolerance,
                    },
                    brand_search_params.BrandSearchParams,
                ),
            ),
            cast_to=BrandSearchResponse,
        )


class BrandResourceWithRawResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_raw_response_wrapper(
            brand.retrieve,
        )
        self.retrieve_simplified = to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.search = to_raw_response_wrapper(
            brand.search,
        )


class AsyncBrandResourceWithRawResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_raw_response_wrapper(
            brand.retrieve,
        )
        self.retrieve_simplified = async_to_raw_response_wrapper(
            brand.retrieve_simplified,
        )
        self.search = async_to_raw_response_wrapper(
            brand.search,
        )


class BrandResourceWithStreamingResponse:
    def __init__(self, brand: BrandResource) -> None:
        self._brand = brand

        self.retrieve = to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.retrieve_simplified = to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.search = to_streamed_response_wrapper(
            brand.search,
        )


class AsyncBrandResourceWithStreamingResponse:
    def __init__(self, brand: AsyncBrandResource) -> None:
        self._brand = brand

        self.retrieve = async_to_streamed_response_wrapper(
            brand.retrieve,
        )
        self.retrieve_simplified = async_to_streamed_response_wrapper(
            brand.retrieve_simplified,
        )
        self.search = async_to_streamed_response_wrapper(
            brand.search,
        )
