# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import utility_prefetch_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.utility_prefetch_response import UtilityPrefetchResponse

__all__ = ["UtilityResource", "AsyncUtilityResource"]


class UtilityResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UtilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return UtilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UtilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return UtilityResourceWithStreamingResponse(self)

    def prefetch(
        self,
        *,
        identifier: utility_prefetch_params.Identifier,
        type: Literal["brand", "styleguide"],
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UtilityPrefetchResponse:
        """Signal that you may fetch data soon to improve latency.

        The type field selects
        what to prefetch ('brand' queues a brand data fetch, 'styleguide' queues a
        styleguide extraction) and identifier carries exactly one lookup key: a domain,
        or an email whose domain is extracted and validated (free email providers and
        disposable email addresses are not allowed).

        Args:
          identifier: Identifier of the target to prefetch. Provide exactly one of domain or email.

          type: What to prefetch: 'brand' warms the brand data cache, 'styleguide' warms the
              styleguide cache.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/utility/prefetch",
            body=maybe_transform(
                {
                    "identifier": identifier,
                    "type": type,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                utility_prefetch_params.UtilityPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchResponse,
        )


class AsyncUtilityResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUtilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncUtilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUtilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncUtilityResourceWithStreamingResponse(self)

    async def prefetch(
        self,
        *,
        identifier: utility_prefetch_params.Identifier,
        type: Literal["brand", "styleguide"],
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UtilityPrefetchResponse:
        """Signal that you may fetch data soon to improve latency.

        The type field selects
        what to prefetch ('brand' queues a brand data fetch, 'styleguide' queues a
        styleguide extraction) and identifier carries exactly one lookup key: a domain,
        or an email whose domain is extracted and validated (free email providers and
        disposable email addresses are not allowed).

        Args:
          identifier: Identifier of the target to prefetch. Provide exactly one of domain or email.

          type: What to prefetch: 'brand' warms the brand data cache, 'styleguide' warms the
              styleguide cache.

          tags: Optional tags for tracking usage. Up to 20 tags, each 1 to 50 characters.

          timeout_ms: Optional timeout in milliseconds for the request. If the request takes longer
              than this value, it will be aborted with a 408 status code. Maximum allowed
              value is 300000ms (5 minutes).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/utility/prefetch",
            body=await async_maybe_transform(
                {
                    "identifier": identifier,
                    "type": type,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                utility_prefetch_params.UtilityPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchResponse,
        )


class UtilityResourceWithRawResponse:
    def __init__(self, utility: UtilityResource) -> None:
        self._utility = utility

        self.prefetch = to_raw_response_wrapper(
            utility.prefetch,
        )


class AsyncUtilityResourceWithRawResponse:
    def __init__(self, utility: AsyncUtilityResource) -> None:
        self._utility = utility

        self.prefetch = async_to_raw_response_wrapper(
            utility.prefetch,
        )


class UtilityResourceWithStreamingResponse:
    def __init__(self, utility: UtilityResource) -> None:
        self._utility = utility

        self.prefetch = to_streamed_response_wrapper(
            utility.prefetch,
        )


class AsyncUtilityResourceWithStreamingResponse:
    def __init__(self, utility: AsyncUtilityResource) -> None:
        self._utility = utility

        self.prefetch = async_to_streamed_response_wrapper(
            utility.prefetch,
        )
