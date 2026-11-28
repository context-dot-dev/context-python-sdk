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
    """
    Inspect your organization's API requests, including retained inputs and responses.
    """

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
        """Retrieve a request's metadata, retained input, and response.

        A request that just
        finished can return 404 `NOT_FOUND` for a few seconds, so retry shortly.

        Args:
          request_id: ID of the request, from its response's `request_id` or `X-Request-Id` header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            path_template("/org/logs/{request_id}", request_id=request_id),
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
        """List your organization's API requests, newest first.

        Filter by time, endpoint,
        API key, status, error code, tags, or text. Includes batch settlements and
        monitor runs.

        Args:
          error_code: Filter by the `error_code` returned in the response.

          errors_only: Return only requests that failed with a 4xx or 5xx status.

          from_: Return requests at or after this time. Defaults to 24 hours before `to`.

          key_id: Filter by the ID of the API key that made the request.

          limit: Maximum number of log entries to return per page.

          page: Page number, starting at 1.

          path: Filter by endpoint path, with or without the `/v1` prefix.

          search: Case-insensitive text to find in the request query or body, such as a domain.

          status_code: Filter by exact HTTP status code.

          tags: Comma-separated tags. Returns log entries that have any of them. Up to 20 tags
              of 1 to 50 characters each.

          to: Return requests at or before this time. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/org/logs",
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
    """
    Inspect your organization's API requests, including retained inputs and responses.
    """

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
        """Retrieve a request's metadata, retained input, and response.

        A request that just
        finished can return 404 `NOT_FOUND` for a few seconds, so retry shortly.

        Args:
          request_id: ID of the request, from its response's `request_id` or `X-Request-Id` header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            path_template("/org/logs/{request_id}", request_id=request_id),
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
        """List your organization's API requests, newest first.

        Filter by time, endpoint,
        API key, status, error code, tags, or text. Includes batch settlements and
        monitor runs.

        Args:
          error_code: Filter by the `error_code` returned in the response.

          errors_only: Return only requests that failed with a 4xx or 5xx status.

          from_: Return requests at or after this time. Defaults to 24 hours before `to`.

          key_id: Filter by the ID of the API key that made the request.

          limit: Maximum number of log entries to return per page.

          page: Page number, starting at 1.

          path: Filter by endpoint path, with or without the `/v1` prefix.

          search: Case-insensitive text to find in the request query or body, such as a domain.

          status_code: Filter by exact HTTP status code.

          tags: Comma-separated tags. Returns log entries that have any of them. Up to 20 tags
              of 1 to 50 characters each.

          to: Return requests at or before this time. Defaults to now.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/org/logs",
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
