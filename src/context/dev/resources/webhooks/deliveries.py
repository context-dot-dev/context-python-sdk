# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ..._utils import path_template, required_args, maybe_transform, strip_not_given, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.webhooks import (
    delivery_list_params,
    delivery_retry_params,
    delivery_retrieve_params,
    delivery_list_attempts_params,
)
from ...types.webhooks.delivery_list_response import DeliveryListResponse
from ...types.webhooks.delivery_retry_response import DeliveryRetryResponse
from ...types.webhooks.delivery_retrieve_response import DeliveryRetrieveResponse
from ...types.webhooks.delivery_list_attempts_response import DeliveryListAttemptsResponse

__all__ = ["DeliveriesResource", "AsyncDeliveriesResource"]


class DeliveriesResource(SyncAPIResource):
    """Inspect and retry batch and monitor webhook deliveries."""

    @cached_property
    def with_raw_response(self) -> DeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return DeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return DeliveriesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        delivery_id: str,
        *,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetrieveResponse:
        """
        Retrieve a webhook delivery’s status and original payload.

        Args:
          delivery_id: Delivery ID.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            path_template("/webhooks/deliveries/{delivery_id}", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"tags": tags}, delivery_retrieve_params.DeliveryRetrieveParams),
            ),
            cast_to=DeliveryRetrieveResponse,
        )

    @overload
    def list(
        self,
        *,
        type: Literal["batch"],
        batch_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List batch and monitor webhook deliveries from the last 30 days.

        Args:
          type: Delivery source.

          batch_id: Filter by batch ID.

          created_after: Only include events created after this ISO 8601 timestamp.

          cursor: The next_cursor from the previous response.

          limit: Number of deliveries to return.

          status: Filter by delivery status.

          tags: Labels for filtering usage in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def list(
        self,
        *,
        type: Literal["monitor"],
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        run_id: str | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List batch and monitor webhook deliveries from the last 30 days.

        Args:
          type: Delivery source.

          created_after: Only include events created after this ISO 8601 timestamp.

          cursor: The next_cursor from the previous response.

          limit: Number of deliveries to return.

          monitor_id: Filter by monitor ID.

          run_id: Filter by monitor run ID.

          status: Filter by delivery status.

          tags: Labels for filtering usage in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    def list(
        self,
        *,
        type: Literal["batch"] | Literal["monitor"],
        batch_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        monitor_id: str | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        return self._post(
            "/webhooks/deliveries",
            body=maybe_transform(
                {
                    "type": type,
                    "batch_id": batch_id,
                    "created_after": created_after,
                    "cursor": cursor,
                    "limit": limit,
                    "status": status,
                    "tags": tags,
                    "monitor_id": monitor_id,
                    "run_id": run_id,
                },
                delivery_list_params.DeliveryListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryListResponse,
        )

    def list_attempts(
        self,
        delivery_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListAttemptsResponse:
        """
        List a delivery’s attempts, newest first.

        Args:
          delivery_id: Delivery ID.

          cursor: The next_cursor from the previous response.

          limit: Number of attempts to return.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return self._get(
            path_template("/webhooks/deliveries/{delivery_id}/attempts", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "tags": tags,
                    },
                    delivery_list_attempts_params.DeliveryListAttemptsParams,
                ),
            ),
            cast_to=DeliveryListAttemptsResponse,
        )

    def retry(
        self,
        delivery_id: str,
        *,
        force: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetryResponse:
        """Resend the original payload using the source’s current URL and secret.

        Available
        for 7 days after the event.

        Args:
          delivery_id: Delivery ID.

          force: Resend even if the delivery already succeeded. Defaults to false.

          tags: Labels for filtering usage in the dashboard.

          idempotency_key: Unique key to prevent duplicate retry requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return self._post(
            path_template("/webhooks/deliveries/{delivery_id}/retry", delivery_id=delivery_id),
            body=maybe_transform(
                {
                    "force": force,
                    "tags": tags,
                },
                delivery_retry_params.DeliveryRetryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRetryResponse,
        )


class AsyncDeliveriesResource(AsyncAPIResource):
    """Inspect and retry batch and monitor webhook deliveries."""

    @cached_property
    def with_raw_response(self) -> AsyncDeliveriesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncDeliveriesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncDeliveriesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        delivery_id: str,
        *,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetrieveResponse:
        """
        Retrieve a webhook delivery’s status and original payload.

        Args:
          delivery_id: Delivery ID.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            path_template("/webhooks/deliveries/{delivery_id}", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"tags": tags}, delivery_retrieve_params.DeliveryRetrieveParams),
            ),
            cast_to=DeliveryRetrieveResponse,
        )

    @overload
    async def list(
        self,
        *,
        type: Literal["batch"],
        batch_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List batch and monitor webhook deliveries from the last 30 days.

        Args:
          type: Delivery source.

          batch_id: Filter by batch ID.

          created_after: Only include events created after this ISO 8601 timestamp.

          cursor: The next_cursor from the previous response.

          limit: Number of deliveries to return.

          status: Filter by delivery status.

          tags: Labels for filtering usage in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def list(
        self,
        *,
        type: Literal["monitor"],
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        monitor_id: str | Omit = omit,
        run_id: str | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        """
        List batch and monitor webhook deliveries from the last 30 days.

        Args:
          type: Delivery source.

          created_after: Only include events created after this ISO 8601 timestamp.

          cursor: The next_cursor from the previous response.

          limit: Number of deliveries to return.

          monitor_id: Filter by monitor ID.

          run_id: Filter by monitor run ID.

          status: Filter by delivery status.

          tags: Labels for filtering usage in the dashboard.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(["type"])
    async def list(
        self,
        *,
        type: Literal["batch"] | Literal["monitor"],
        batch_id: str | Omit = omit,
        created_after: Union[str, datetime] | Omit = omit,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        status: Literal["pending", "delivering", "retrying", "delivered", "failed", "cancelled"] | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        monitor_id: str | Omit = omit,
        run_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListResponse:
        return await self._post(
            "/webhooks/deliveries",
            body=await async_maybe_transform(
                {
                    "type": type,
                    "batch_id": batch_id,
                    "created_after": created_after,
                    "cursor": cursor,
                    "limit": limit,
                    "status": status,
                    "tags": tags,
                    "monitor_id": monitor_id,
                    "run_id": run_id,
                },
                delivery_list_params.DeliveryListParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryListResponse,
        )

    async def list_attempts(
        self,
        delivery_id: str,
        *,
        cursor: str | Omit = omit,
        limit: int | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryListAttemptsResponse:
        """
        List a delivery’s attempts, newest first.

        Args:
          delivery_id: Delivery ID.

          cursor: The next_cursor from the previous response.

          limit: Number of attempts to return.

          tags: Comma-separated labels for filtering usage, e.g. `production,team-alpha`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        return await self._get(
            path_template("/webhooks/deliveries/{delivery_id}/attempts", delivery_id=delivery_id),
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "cursor": cursor,
                        "limit": limit,
                        "tags": tags,
                    },
                    delivery_list_attempts_params.DeliveryListAttemptsParams,
                ),
            ),
            cast_to=DeliveryListAttemptsResponse,
        )

    async def retry(
        self,
        delivery_id: str,
        *,
        force: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        idempotency_key: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeliveryRetryResponse:
        """Resend the original payload using the source’s current URL and secret.

        Available
        for 7 days after the event.

        Args:
          delivery_id: Delivery ID.

          force: Resend even if the delivery already succeeded. Defaults to false.

          tags: Labels for filtering usage in the dashboard.

          idempotency_key: Unique key to prevent duplicate retry requests.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not delivery_id:
            raise ValueError(f"Expected a non-empty value for `delivery_id` but received {delivery_id!r}")
        extra_headers = {**strip_not_given({"Idempotency-Key": idempotency_key}), **(extra_headers or {})}
        return await self._post(
            path_template("/webhooks/deliveries/{delivery_id}/retry", delivery_id=delivery_id),
            body=await async_maybe_transform(
                {
                    "force": force,
                    "tags": tags,
                },
                delivery_retry_params.DeliveryRetryParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeliveryRetryResponse,
        )


class DeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_raw_response_wrapper(
            deliveries.list,
        )
        self.list_attempts = to_raw_response_wrapper(
            deliveries.list_attempts,
        )
        self.retry = to_raw_response_wrapper(
            deliveries.retry,
        )


class AsyncDeliveriesResourceWithRawResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = async_to_raw_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            deliveries.list,
        )
        self.list_attempts = async_to_raw_response_wrapper(
            deliveries.list_attempts,
        )
        self.retry = async_to_raw_response_wrapper(
            deliveries.retry,
        )


class DeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: DeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            deliveries.list,
        )
        self.list_attempts = to_streamed_response_wrapper(
            deliveries.list_attempts,
        )
        self.retry = to_streamed_response_wrapper(
            deliveries.retry,
        )


class AsyncDeliveriesResourceWithStreamingResponse:
    def __init__(self, deliveries: AsyncDeliveriesResource) -> None:
        self._deliveries = deliveries

        self.retrieve = async_to_streamed_response_wrapper(
            deliveries.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            deliveries.list,
        )
        self.list_attempts = async_to_streamed_response_wrapper(
            deliveries.list_attempts,
        )
        self.retry = async_to_streamed_response_wrapper(
            deliveries.retry,
        )
