# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.browser import profile_list_params
from ...types.browser.profile_list_response import ProfileListResponse

__all__ = ["ProfilesResource", "AsyncProfilesResource"]


class ProfilesResource(SyncAPIResource):
    """See the authenticated browser profiles your organization created."""

    @cached_property
    def with_raw_response(self) -> ProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return ProfilesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        List the browser profiles your organization created with `/web/scrape`, newest
        first.

        Args:
          cursor: The `next_cursor` from the previous page.

          limit: Number of profiles per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/org/browser/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            cast_to=ProfileListResponse,
        )


class AsyncProfilesResource(AsyncAPIResource):
    """See the authenticated browser profiles your organization created."""

    @cached_property
    def with_raw_response(self) -> AsyncProfilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncProfilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProfilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncProfilesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProfileListResponse:
        """
        List the browser profiles your organization created with `/web/scrape`, newest
        first.

        Args:
          cursor: The `next_cursor` from the previous page.

          limit: Number of profiles per page.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/org/browser/profiles",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                    },
                    profile_list_params.ProfileListParams,
                ),
            ),
            cast_to=ProfileListResponse,
        )


class ProfilesResourceWithRawResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_raw_response_wrapper(
            profiles.list,
        )


class AsyncProfilesResourceWithRawResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_raw_response_wrapper(
            profiles.list,
        )


class ProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: ProfilesResource) -> None:
        self._profiles = profiles

        self.list = to_streamed_response_wrapper(
            profiles.list,
        )


class AsyncProfilesResourceWithStreamingResponse:
    def __init__(self, profiles: AsyncProfilesResource) -> None:
        self._profiles = profiles

        self.list = async_to_streamed_response_wrapper(
            profiles.list,
        )
