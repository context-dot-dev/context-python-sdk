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
    """Scrape up to 100,000 URLs or crawl a site asynchronously."""

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
        """
        Retrieve a batch's status, progress, and credit usage, plus links to download
        its results once it finishes. Result files are deleted 180 days after the batch
        finishes.

        Args:
          batch_id: ID of the batch.

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
        status: Literal["pending", "queued", "running", "cancelling", "completed", "cancelled", "failed"] | Omit = omit,
        tags: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """List your batches, newest first.

        Filter by status or tags, or search by batch
        ID, crawl source, or tag.

        Args:
          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of batches to return per page.

          q: Search term matched against batch IDs, crawl sources (start URL or sitemap
              domain), and tags.

          search_type: How `q` matches: `prefix` matches the start of a term, for search-as-you-type,
              and `exact` matches whole terms. Defaults to `prefix`.

          status: Filter by batch status.

          tags: Comma-separated tags. Returns batches that have any of them. You can also repeat
              the `tags` parameter.

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
          batch_id: ID of the batch.

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

        Pages already in progress finish, then the
        batch becomes `cancelled` and unused credits are refunded.

        Args:
          batch_id: ID of the batch.

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
        """Page through a finished batch's results as JSON.

        Each record's `result` has the
        same outputs and per-format errors as `POST /web/scrape`. Results are kept for
        180 days after the batch finishes.

        Args:
          batch_id: ID of the batch.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of results to return per page. A page can hold fewer to stay
              under about 8 MB, so page with `next_cursor` instead of counting records.

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
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: batch_submit_params.Webhook | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """
        Scrape up to 100,000 URLs, or crawl a site, asynchronously with every Scrape
        Anything format and option from `POST /web/scrape`. Poll `GET /batch/{batch_id}`
        or pass `webhook` to be notified when the batch finishes. URLs and credits are
        checked after the batch is accepted, so a batch that fails those checks ends as
        `failed` with a `failure` code instead of returning an error.

        Args:
          input: What to scrape: a list of URLs (`scrape`) or a site crawl (`crawl`).

          policies: Access policy IDs to apply to every page; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Tags to store on the batch. Filter `GET /batch/list` by them later.

          webhook: Webhook to notify when the batch finishes. Omit `retry` for a single attempt, or
              pass `retry: {}` for the default retry schedule.

          idempotency_key: Unique key for this submission. Retrying with the same key and body returns the
              original batch instead of creating another; a different body returns `409`.

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
                    "policies": policies,
                    "tags": tags,
                    "webhook": webhook,
                },
                batch_submit_params.BatchSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BatchSubmitResponse,
        )


class AsyncBatchResource(AsyncAPIResource):
    """Scrape up to 100,000 URLs or crawl a site asynchronously."""

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
        """
        Retrieve a batch's status, progress, and credit usage, plus links to download
        its results once it finishes. Result files are deleted 180 days after the batch
        finishes.

        Args:
          batch_id: ID of the batch.

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
        status: Literal["pending", "queued", "running", "cancelling", "completed", "cancelled", "failed"] | Omit = omit,
        tags: Union[str, SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchListResponse:
        """List your batches, newest first.

        Filter by status or tags, or search by batch
        ID, crawl source, or tag.

        Args:
          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of batches to return per page.

          q: Search term matched against batch IDs, crawl sources (start URL or sitemap
              domain), and tags.

          search_type: How `q` matches: `prefix` matches the start of a term, for search-as-you-type,
              and `exact` matches whole terms. Defaults to `prefix`.

          status: Filter by batch status.

          tags: Comma-separated tags. Returns batches that have any of them. You can also repeat
              the `tags` parameter.

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
          batch_id: ID of the batch.

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

        Pages already in progress finish, then the
        batch becomes `cancelled` and unused credits are refunded.

        Args:
          batch_id: ID of the batch.

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
        """Page through a finished batch's results as JSON.

        Each record's `result` has the
        same outputs and per-format errors as `POST /web/scrape`. Results are kept for
        180 days after the batch finishes.

        Args:
          batch_id: ID of the batch.

          cursor: Cursor from the previous page's `next_cursor`. Omit for the first page.

          limit: Maximum number of results to return per page. A page can hold fewer to stay
              under about 8 MB, so page with `next_cursor` instead of counting records.

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
        policies: SequenceNotStr[str] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        webhook: batch_submit_params.Webhook | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BatchSubmitResponse:
        """
        Scrape up to 100,000 URLs, or crawl a site, asynchronously with every Scrape
        Anything format and option from `POST /web/scrape`. Poll `GET /batch/{batch_id}`
        or pass `webhook` to be notified when the batch finishes. URLs and credits are
        checked after the batch is accepted, so a batch that fails those checks ends as
        `failed` with a `failure` code instead of returning an error.

        Args:
          input: What to scrape: a list of URLs (`scrape`) or a site crawl (`crawl`).

          policies: Access policy IDs to apply to every page; each URL must pass all of them.
              Requires access policies enabled for your organization; otherwise returns
              `ACCESS_POLICIES_NOT_ENABLED`.

          tags: Tags to store on the batch. Filter `GET /batch/list` by them later.

          webhook: Webhook to notify when the batch finishes. Omit `retry` for a single attempt, or
              pass `retry: {}` for the default retry schedule.

          idempotency_key: Unique key for this submission. Retrying with the same key and body returns the
              original batch instead of creating another; a different body returns `409`.

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
                    "policies": policies,
                    "tags": tags,
                    "webhook": webhook,
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
