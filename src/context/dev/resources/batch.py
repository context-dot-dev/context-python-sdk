# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal

import httpx

from ..types import batch_list_params, batch_submit_params, batch_get_results_params
from .._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from .._utils import path_template, maybe_transform, strip_not_given, async_maybe_transform
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
from ..types.batch_delete_response import BatchDeleteResponse
from ..types.batch_submit_response import BatchSubmitResponse
from ..types.batch_retrieve_response import BatchRetrieveResponse
from ..types.batch_get_results_response import BatchGetResultsResponse

__all__ = ["BatchResource", "AsyncBatchResource"]


class BatchResource(SyncAPIResource):
    """Scrape many pages or crawl a site asynchronously."""

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
        """Get batch progress and result download links.

        Result files are deleted 7 days
        after the batch finishes.

        Args:
          batch_id: Batch ID.

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
        tags: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List your batches, newest first, with optional filters.

        Args:
          cursor: Cursor from the previous page.

          limit: Batches per page. Defaults to 25.

          q: Free-text search term, matched against the batch id, crawl source (start URL or
              sitemap domain), and tags.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter by status.

          tags: Tags to filter by (matches batches having any of them). Pass repeated `tags`
              params or one comma-separated list, e.g. `tags=docs,competitor`.

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

    def delete(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """Permanently delete a finished batch and its results.

        Its webhook deliveries can
        no longer be retried.

        Args:
          batch_id: Batch ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return self._delete(
            path_template("/batch/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
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

        Pages already in progress finish before
        the batch becomes cancelled.

        Args:
          batch_id: Batch ID.

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
        """Page through a finished batch’s results as JSON.

        Results remain available for 7
        days.

        Args:
          batch_id: Batch ID.

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
        input: batch_submit_params.Input,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: batch_submit_params.Webhook | Omit = omit,
        webhook_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """Scrape up to 25,000 URLs, or crawl a site, asynchronously.

        Poll the batch ID or
        receive a webhook when it finishes.

        Args:
          input: Choose a URL list or a site crawl.

          tags: Tags stored on the batch. Filter the batch list by them later.

          webhook: Where to send the batch's final-status event. Omit `retry` for one attempt; `{}`
              uses the default retry schedule.

          webhook_url: Legacy URL notified when the batch finishes. Preserves one best-effort attempt.
              Cannot be combined with webhook.

          idempotency_key: Unique key per submission. Retrying with the same key and body returns the
              original batch; a different body returns `409`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            "/batch/submit",
            body=maybe_transform(
                {
                    "input": input,
                    "tags": tags,
                    "webhook": webhook,
                    "webhook_url": webhook_url,
                },
                batch_submit_params.BatchSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSubmitResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    """Scrape many pages or crawl a site asynchronously."""

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
        """Get batch progress and result download links.

        Result files are deleted 7 days
        after the batch finishes.

        Args:
          batch_id: Batch ID.

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
        tags: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """
        List your batches, newest first, with optional filters.

        Args:
          cursor: Cursor from the previous page.

          limit: Batches per page. Defaults to 25.

          q: Free-text search term, matched against the batch id, crawl source (start URL or
              sitemap domain), and tags.

          search_type: `prefix` for as-you-type prefix matching (default), `exact` for full-token
              matching.

          status: Filter by status.

          tags: Tags to filter by (matches batches having any of them). Pass repeated `tags`
              params or one comma-separated list, e.g. `tags=docs,competitor`.

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

    async def delete(
        self,
        batch_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchDeleteResponse:
        """Permanently delete a finished batch and its results.

        Its webhook deliveries can
        no longer be retried.

        Args:
          batch_id: Batch ID.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not batch_id:
            raise ValueError(f"Expected a non-empty value for `batch_id` but received {batch_id!r}")
        return await self._delete(
            path_template("/batch/{batch_id}", batch_id=batch_id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchDeleteResponse,
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

        Pages already in progress finish before
        the batch becomes cancelled.

        Args:
          batch_id: Batch ID.

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
        """Page through a finished batch’s results as JSON.

        Results remain available for 7
        days.

        Args:
          batch_id: Batch ID.

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
        input: batch_submit_params.Input,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: batch_submit_params.Webhook | Omit = omit,
        webhook_url: str | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """Scrape up to 25,000 URLs, or crawl a site, asynchronously.

        Poll the batch ID or
        receive a webhook when it finishes.

        Args:
          input: Choose a URL list or a site crawl.

          tags: Tags stored on the batch. Filter the batch list by them later.

          webhook: Where to send the batch's final-status event. Omit `retry` for one attempt; `{}`
              uses the default retry schedule.

          webhook_url: Legacy URL notified when the batch finishes. Preserves one best-effort attempt.
              Cannot be combined with webhook.

          idempotency_key: Unique key per submission. Retrying with the same key and body returns the
              original batch; a different body returns `409`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            "/batch/submit",
            body=await async_maybe_transform(
                {
                    "input": input,
                    "tags": tags,
                    "webhook": webhook,
                    "webhook_url": webhook_url,
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
        self.delete = to_raw_response_wrapper(
            batch.delete,
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
        self.delete = async_to_raw_response_wrapper(
            batch.delete,
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
        self.delete = to_streamed_response_wrapper(
            batch.delete,
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
        self.delete = async_to_streamed_response_wrapper(
            batch.delete,
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
