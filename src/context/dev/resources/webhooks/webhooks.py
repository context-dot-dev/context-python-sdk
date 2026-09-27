# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .deliveries import (
    DeliveriesResource,
    AsyncDeliveriesResource,
    DeliveriesResourceWithRawResponse,
    AsyncDeliveriesResourceWithRawResponse,
    DeliveriesResourceWithStreamingResponse,
    AsyncDeliveriesResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["WebhooksResource", "AsyncWebhooksResource"]


class WebhooksResource(SyncAPIResource):
    @cached_property
    def deliveries(self) -> DeliveriesResource:
        """Inspect and retry batch and monitor webhook deliveries."""
        return DeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> WebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return WebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> WebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return WebhooksResourceWithStreamingResponse(self)


class AsyncWebhooksResource(AsyncAPIResource):
    @cached_property
    def deliveries(self) -> AsyncDeliveriesResource:
        """Inspect and retry batch and monitor webhook deliveries."""
        return AsyncDeliveriesResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncWebhooksResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncWebhooksResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncWebhooksResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncWebhooksResourceWithStreamingResponse(self)


class WebhooksResourceWithRawResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithRawResponse:
        """Inspect and retry batch and monitor webhook deliveries."""
        return DeliveriesResourceWithRawResponse(self._webhooks.deliveries)


class AsyncWebhooksResourceWithRawResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithRawResponse:
        """Inspect and retry batch and monitor webhook deliveries."""
        return AsyncDeliveriesResourceWithRawResponse(self._webhooks.deliveries)


class WebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: WebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def deliveries(self) -> DeliveriesResourceWithStreamingResponse:
        """Inspect and retry batch and monitor webhook deliveries."""
        return DeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)


class AsyncWebhooksResourceWithStreamingResponse:
    def __init__(self, webhooks: AsyncWebhooksResource) -> None:
        self._webhooks = webhooks

    @cached_property
    def deliveries(self) -> AsyncDeliveriesResourceWithStreamingResponse:
        """Inspect and retry batch and monitor webhook deliveries."""
        return AsyncDeliveriesResourceWithStreamingResponse(self._webhooks.deliveries)
