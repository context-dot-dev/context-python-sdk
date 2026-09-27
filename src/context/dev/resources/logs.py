# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime

import httpx

from ..types import log_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.log_list_response import LogListResponse
from ..types.log_retrieve_response import LogRetrieveResponse

__all__ = ["LogsResource", "AsyncLogsResource"]


class LogsResource(SyncAPIResource):
    """Read your organization's API request logs."""

    @cached_property
    def with_raw_response(self) -> LogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return LogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return LogsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieve a request’s metadata, retained input, and response.

        Args:
          request_id: The request ID of the logged API call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/logs/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogRetrieveResponse,
        )

    def list(
        self,
        *,
        error_code: str | Omit = omit,
        errors_only: bool | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        key_id: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        search: str | Omit = omit,
        status_code: int | Omit = omit,
        tags: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogListResponse:
        """List your organization’s request logs with filters and pagination.

        Logs also
        include batch settlements and monitor runs.

        Args:
          error_code: Filter by the `error_code` returned in the response.

          errors_only: Only include requests that returned a 4xx or 5xx status.

          from_: Only include requests at or after this ISO 8601 timestamp. Defaults to 24 hours
              before `to`.

          key_id: Filter by the API key that made the request.

          limit: Number of log entries per page.

          page: Page number, starting at 1.

          path: Filter by endpoint path, with or without the /v1 prefix.

          search: Case-insensitive substring match against the request query and body, e.g. a
              domain.

          status_code: Filter by exact HTTP status code.

          tags: Comma-separated request tags. Matches requests carrying any of them. Up to 20
              tags, each 1-50 characters.

          to: Only include requests at or before this ISO 8601 timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "error_code": error_code,
                        "errors_only": errors_only,
                        "from_": from_,
                        "key_id": key_id,
                        "limit": limit,
                        "page": page,
                        "path": path,
                        "search": search,
                        "status_code": status_code,
                        "tags": tags,
                        "to": to,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=LogListResponse,
        )


class AsyncLogsResource(AsyncAPIResource):
    """Read your organization's API request logs."""

    @cached_property
    def with_raw_response(self) -> AsyncLogsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncLogsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLogsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncLogsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogRetrieveResponse:
        """
        Retrieve a request’s metadata, retained input, and response.

        Args:
          request_id: The request ID of the logged API call.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/logs/{request_id}", request_id=request_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LogRetrieveResponse,
        )

    async def list(
        self,
        *,
        error_code: str | Omit = omit,
        errors_only: bool | Omit = omit,
        from_: Union[str, datetime] | Omit = omit,
        key_id: str | Omit = omit,
        limit: int | Omit = omit,
        page: int | Omit = omit,
        path: str | Omit = omit,
        search: str | Omit = omit,
        status_code: int | Omit = omit,
        tags: str | Omit = omit,
        to: Union[str, datetime] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LogListResponse:
        """List your organization’s request logs with filters and pagination.

        Logs also
        include batch settlements and monitor runs.

        Args:
          error_code: Filter by the `error_code` returned in the response.

          errors_only: Only include requests that returned a 4xx or 5xx status.

          from_: Only include requests at or after this ISO 8601 timestamp. Defaults to 24 hours
              before `to`.

          key_id: Filter by the API key that made the request.

          limit: Number of log entries per page.

          page: Page number, starting at 1.

          path: Filter by endpoint path, with or without the /v1 prefix.

          search: Case-insensitive substring match against the request query and body, e.g. a
              domain.

          status_code: Filter by exact HTTP status code.

          tags: Comma-separated request tags. Matches requests carrying any of them. Up to 20
              tags, each 1-50 characters.

          to: Only include requests at or before this ISO 8601 timestamp. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/logs",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "error_code": error_code,
                        "errors_only": errors_only,
                        "from_": from_,
                        "key_id": key_id,
                        "limit": limit,
                        "page": page,
                        "path": path,
                        "search": search,
                        "status_code": status_code,
                        "tags": tags,
                        "to": to,
                    },
                    log_list_params.LogListParams,
                ),
            ),
            cast_to=LogListResponse,
        )


class LogsResourceWithRawResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_raw_response_wrapper(
            logs.retrieve,
        )
        self.list = to_raw_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithRawResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_raw_response_wrapper(
            logs.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            logs.list,
        )


class LogsResourceWithStreamingResponse:
    def __init__(self, logs: LogsResource) -> None:
        self._logs = logs

        self.retrieve = to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            logs.list,
        )


class AsyncLogsResourceWithStreamingResponse:
    def __init__(self, logs: AsyncLogsResource) -> None:
        self._logs = logs

        self.retrieve = async_to_streamed_response_wrapper(
            logs.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            logs.list,
        )
