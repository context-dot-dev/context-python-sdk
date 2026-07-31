# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import batch_list_params, batch_submit_params, batch_get_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ..types.batch_list_response import BatchListResponse
from ..types.batch_cancel_response import BatchCancelResponse
from ..types.batch_submit_response import BatchSubmitResponse
from ..types.batch_retrieve_response import BatchRetrieveResponse
from ..types.batch_get_results_response import BatchGetResultsResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return BatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return BatchResourceWithStreamingResponse(self)

    def retrieve(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchRetrieveResponse:
        """Check progress and get download links when the batch finishes.

        Also returns the
        rejected-URL list from submission. The webhook signing secret is not repeated
        here — it is returned once, by the submit response.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            path_template("/batch/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
        )

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        search_type: Literal["exact", "prefix"] | Omit = omit,
        status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """List your batches from newest to oldest.

        Filter by status or continue with a
        cursor.

        Args:
          cursor: Cursor from the previous page.

          limit: Batches per page. Defaults to 25.

          q: Free-text search term, matched against the batch id, crawl source (start URL or
              sitemap domain), and tags.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter by status.

          tags: Comma-separated list of tags to filter by (matches batches having any of them).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/batch/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "q": q,
                        "search_type": search_type,
                        "status": status,
                        "tags": tags,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    def cancel(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCancelResponse:
        """Stop a batch from starting new pages.

        In-progress pages finish, and unused
        credits are refunded.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._post(
            path_template("/batch/{batch_id}/cancel", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelResponse,
        )

    def get_results(
        self,
        batch_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchGetResultsResponse:
        """
        Page through the result records of a finished batch as JSON, in the same order
        as the downloadable result files. Use this instead of downloading and parsing
        the NDJSON files yourself.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          cursor: next_cursor from the previous page.

          limit: Records per page. Defaults to 25. A page can close early so its payload stays
              under ~8 MB; rely on next_cursor rather than counting records.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._get(
            path_template("/batch/{batch_id}/results", batch_id=batch_id),
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
                    batch_get_results_params.BatchGetResultsParams,
                ),
            ),
            cast_to=BatchGetResultsResponse,
        )

    def submit(
        self,
        *,
        identifiers: batch_submit_params.Identifiers,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """
        Retrieve and normalize a person profile from identifiers.

        Args:
          identifiers: Known identifiers for the person. At least one identifier is required.

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
            "/people/retrieve",
            body=maybe_transform(
                {
                    "identifiers": identifiers,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                batch_submit_params.BatchSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSubmitResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBatchResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncBatchResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBatchResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncBatchResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchRetrieveResponse:
        """Check progress and get download links when the batch finishes.

        Also returns the
        rejected-URL list from submission. The webhook signing secret is not repeated
        here — it is returned once, by the submit response.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            path_template("/batch/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchRetrieveResponse,
        )

    async def list(
        self,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        q: str | Omit = omit,
        search_type: Literal["exact", "prefix"] | Omit = omit,
        status: Literal["queued", "running", "cancelling", "completed", "cancelled", "failed"] | Omit = omit,
        tags: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """List your batches from newest to oldest.

        Filter by status or continue with a
        cursor.

        Args:
          cursor: Cursor from the previous page.

          limit: Batches per page. Defaults to 25.

          q: Free-text search term, matched against the batch id, crawl source (start URL or
              sitemap domain), and tags.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter by status.

          tags: Comma-separated list of tags to filter by (matches batches having any of them).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/batch/list",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "q": q,
                        "search_type": search_type,
                        "status": status,
                        "tags": tags,
                    },
                    batch_list_params.BatchListParams,
                ),
            ),
            cast_to=BatchListResponse,
        )

    async def cancel(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchCancelResponse:
        """Stop a batch from starting new pages.

        In-progress pages finish, and unused
        credits are refunded.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._post(
            path_template("/batch/{batch_id}/cancel", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchCancelResponse,
        )

    async def get_results(
        self,
        batch_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchGetResultsResponse:
        """
        Page through the result records of a finished batch as JSON, in the same order
        as the downloadable result files. Use this instead of downloading and parsing
        the NDJSON files yourself.

        Args:
          batch_id: ID of the batch to retrieve or cancel.

          cursor: next_cursor from the previous page.

          limit: Records per page. Defaults to 25. A page can close early so its payload stays
              under ~8 MB; rely on next_cursor rather than counting records.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._get(
            path_template("/batch/{batch_id}/results", batch_id=batch_id),
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
                    batch_get_results_params.BatchGetResultsParams,
                ),
            ),
            cast_to=BatchGetResultsResponse,
        )

    async def submit(
        self,
        *,
        identifiers: batch_submit_params.Identifiers,
        tags: SequenceNotStr[str] | Omit = omit,
        timeout_ms: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """
        Retrieve and normalize a person profile from identifiers.

        Args:
          identifiers: Known identifiers for the person. At least one identifier is required.

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
            "/people/retrieve",
            body=await async_maybe_transform(
                {
                    "identifiers": identifiers,
                    "tags": tags,
                    "timeout_ms": timeout_ms,
                },
                batch_submit_params.BatchSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSubmitResponse,
        )


class BatchResourceWithRawResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.retrieve = to_raw_response_wrapper(
            batch.retrieve,
        )
        self.list = to_raw_response_wrapper(
            batch.list,
        )
        self.cancel = to_raw_response_wrapper(
            batch.cancel,
        )
        self.get_results = to_raw_response_wrapper(
            batch.get_results,
        )
        self.submit = to_raw_response_wrapper(
            batch.submit,
        )


class AsyncBatchResourceWithRawResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.retrieve = async_to_raw_response_wrapper(
            batch.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            batch.list,
        )
        self.cancel = async_to_raw_response_wrapper(
            batch.cancel,
        )
        self.get_results = async_to_raw_response_wrapper(
            batch.get_results,
        )
        self.submit = async_to_raw_response_wrapper(
            batch.submit,
        )


class BatchResourceWithStreamingResponse:
    def __init__(self, batch: BatchResource) -> None:
        self._batch = batch

        self.retrieve = to_streamed_response_wrapper(
            batch.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            batch.list,
        )
        self.cancel = to_streamed_response_wrapper(
            batch.cancel,
        )
        self.get_results = to_streamed_response_wrapper(
            batch.get_results,
        )
        self.submit = to_streamed_response_wrapper(
            batch.submit,
        )


class AsyncBatchResourceWithStreamingResponse:
    def __init__(self, batch: AsyncBatchResource) -> None:
        self._batch = batch

        self.retrieve = async_to_streamed_response_wrapper(
            batch.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            batch.list,
        )
        self.cancel = async_to_streamed_response_wrapper(
            batch.cancel,
        )
        self.get_results = async_to_streamed_response_wrapper(
            batch.get_results,
        )
        self.submit = async_to_streamed_response_wrapper(
            batch.submit,
        )
