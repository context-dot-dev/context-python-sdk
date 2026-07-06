# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import overload

import httpx

from ..types import ai_extract_product_params, ai_extract_products_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.ai_extract_product_response import AIExtractProductResponse
from ..types.ai_extract_products_response import AIExtractProductsResponse

__all__ = ["AIResource", "AsyncAIResource"]


class AIResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AIResourceWithStreamingResponse(self)

    def extract_product(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductResponse:
        """
        Given a single URL, determines if it is a product page and extracts the product
        information.

        Args:
          url: The product page URL to extract product data from.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/brand/ai/product",
            body=maybe_transform(
                {
                    "url": url,
                    "max_age_ms": max_age_ms,
                    "timeout_ms": timeout_ms,
                },
                ai_extract_product_params.AIExtractProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractProductResponse,
        )

    @overload
    def extract_products(
        self,
        *,
        domain: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def extract_products(
        self,
        *,
        direct_url: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    def extract_products(
        self,
        *,
        domain: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        return self._post(
            "/brand/ai/products",
            body=maybe_transform(
                {
                    "domain": domain,
                    "max_age_ms": max_age_ms,
                    "max_products": max_products,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                ai_extract_products_params.AIExtractProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractProductsResponse,
        )


class AsyncAIResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAIResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncAIResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAIResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncAIResourceWithStreamingResponse(self)

    async def extract_product(
        self,
        *,
        url: str,
        max_age_ms: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductResponse:
        """
        Given a single URL, determines if it is a product page and extracts the product
        information.

        Args:
          url: The product page URL to extract product data from.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/brand/ai/product",
            body=await async_maybe_transform(
                {
                    "url": url,
                    "max_age_ms": max_age_ms,
                    "timeout_ms": timeout_ms,
                },
                ai_extract_product_params.AIExtractProductParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractProductResponse,
        )

    @overload
    async def extract_products(
        self,
        *,
        domain: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          domain: The domain name to analyze.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def extract_products(
        self,
        *,
        direct_url: str,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        """Extract product information from a brand's website.

        We will analyze the website
        and return a list of products with details such as name, description, image,
        pricing, features, and more.

        Args:
          direct_url: A specific URL to use directly as the starting point for extraction without
              domain resolution.

          max_age_ms: Return a cached result if a prior scrape for the same parameters exists and is
              younger than this many milliseconds. Defaults to 7 days (604800000 ms) when
              omitted. Max is 30 days (2592000000 ms). Set to 0 to always scrape fresh.

          max_products: Maximum number of products to extract.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["domain"], ["direct_url"])
    async def extract_products(
        self,
        *,
        domain: str | Omit = omit,
        max_age_ms: int | Omit = omit,
        max_products: int | Omit = omit,
        timeout_ms: int | Omit = omit,
        direct_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AIExtractProductsResponse:
        return await self._post(
            "/brand/ai/products",
            body=await async_maybe_transform(
                {
                    "domain": domain,
                    "max_age_ms": max_age_ms,
                    "max_products": max_products,
                    "timeout_ms": timeout_ms,
                    "direct_url": direct_url,
                },
                ai_extract_products_params.AIExtractProductsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AIExtractProductsResponse,
        )


class AIResourceWithRawResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.extract_product = to_raw_response_wrapper(
            ai.extract_product,
        )
        self.extract_products = to_raw_response_wrapper(
            ai.extract_products,
        )


class AsyncAIResourceWithRawResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.extract_product = async_to_raw_response_wrapper(
            ai.extract_product,
        )
        self.extract_products = async_to_raw_response_wrapper(
            ai.extract_products,
        )


class AIResourceWithStreamingResponse:
    def __init__(self, ai: AIResource) -> None:
        self._ai = ai

        self.extract_product = to_streamed_response_wrapper(
            ai.extract_product,
        )
        self.extract_products = to_streamed_response_wrapper(
            ai.extract_products,
        )


class AsyncAIResourceWithStreamingResponse:
    def __init__(self, ai: AsyncAIResource) -> None:
        self._ai = ai

        self.extract_product = async_to_streamed_response_wrapper(
            ai.extract_product,
        )
        self.extract_products = async_to_streamed_response_wrapper(
            ai.extract_products,
        )
