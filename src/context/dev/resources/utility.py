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
    """Prefetch brand and styleguide data so later lookups return sooner."""

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
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: utility_prefetch_params.TimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UtilityPrefetchResponse:
        """
        Start fetching a domain's brand or styleguide data in the background so a later
        lookup returns faster. Accepts a domain or a work email.

        Args:
          identifier: Domain or work email to prefetch. Provide exactly one.

          type: Data to prefetch.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline. The request fails with 408 when it passes.

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
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
                },
                utility_prefetch_params.UtilityPrefetchParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UtilityPrefetchResponse,
        )


class AsyncUtilityResource(AsyncAPIResource):
    """Prefetch brand and styleguide data so later lookups return sooner."""

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
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_opts: utility_prefetch_params.TimeoutOpts | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UtilityPrefetchResponse:
        """
        Start fetching a domain's brand or styleguide data in the background so a later
        lookup returns faster. Accepts a domain or a work email.

        Args:
          identifier: Domain or work email to prefetch. Provide exactly one.

          type: Data to prefetch.

          policies: Access policy IDs to apply; each URL must pass all of them. Requires access
              policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Labels for this request. Filter usage and request logs by them in the dashboard
              or with `GET /org/logs`.

          timeout_opts: Request deadline. The request fails with 408 when it passes.

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
                    "policies": policies,
                    "tags": tags,
                    "timeout_opts": timeout_opts,
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
