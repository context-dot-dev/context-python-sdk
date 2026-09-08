# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev._utils import parse_datetime
from context.dev.types.webhooks import (
    DeliveryListResponse,
    DeliveryRetryResponse,
    DeliveryRetrieveResponse,
    DeliveryListAttemptsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDeliveries:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ContextDev) -> None:
        response = client.webhooks.deliveries.with_raw_response.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ContextDev) -> None:
        with client.webhooks.deliveries.with_streaming_response.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.retrieve(
                delivery_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_overload_1(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list(
            type="batch",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params_overload_1(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list(
            type="batch",
            batch_id="batch_id",
            created_after=parse_datetime("2026-09-01T00:00:00Z"),
            cursor="whd_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            status="pending",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_overload_1(self, client: ContextDev) -> None:
        response = client.webhooks.deliveries.with_raw_response.list(
            type="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_overload_1(self, client: ContextDev) -> None:
        with client.webhooks.deliveries.with_streaming_response.list(
            type="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_overload_2(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list(
            type="monitor",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params_overload_2(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list(
            type="monitor",
            created_after=parse_datetime("2026-09-01T00:00:00Z"),
            cursor="whd_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            monitor_id="monitor_id",
            run_id="run_id",
            status="pending",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_overload_2(self, client: ContextDev) -> None:
        response = client.webhooks.deliveries.with_raw_response.list(
            type="monitor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_overload_2(self, client: ContextDev) -> None:
        with client.webhooks.deliveries.with_streaming_response.list(
            type="monitor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attempts(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_attempts_with_all_params(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            cursor="wha_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list_attempts(self, client: ContextDev) -> None:
        response = client.webhooks.deliveries.with_raw_response.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list_attempts(self, client: ContextDev) -> None:
        with client.webhooks.deliveries.with_streaming_response.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_list_attempts(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.list_attempts(
                delivery_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retry_with_all_params(self, client: ContextDev) -> None:
        delivery = client.webhooks.deliveries.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            force=True,
            tags=["production", "team-alpha"],
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retry(self, client: ContextDev) -> None:
        response = client.webhooks.deliveries.with_raw_response.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = response.parse()
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retry(self, client: ContextDev) -> None:
        with client.webhooks.deliveries.with_streaming_response.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = response.parse()
            assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retry(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            client.webhooks.deliveries.with_raw_response.retry(
                delivery_id="",
            )


class TestAsyncDeliveries:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextDev) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextDev) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.retrieve(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryRetrieveResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.retrieve(
                delivery_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_overload_1(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            type="batch",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params_overload_1(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            type="batch",
            batch_id="batch_id",
            created_after=parse_datetime("2026-09-01T00:00:00Z"),
            cursor="whd_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            status="pending",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_overload_1(self, async_client: AsyncContextDev) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list(
            type="batch",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_overload_1(self, async_client: AsyncContextDev) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list(
            type="batch",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_overload_2(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            type="monitor",
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params_overload_2(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list(
            type="monitor",
            created_after=parse_datetime("2026-09-01T00:00:00Z"),
            cursor="whd_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            monitor_id="monitor_id",
            run_id="run_id",
            status="pending",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_overload_2(self, async_client: AsyncContextDev) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list(
            type="monitor",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_overload_2(self, async_client: AsyncContextDev) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list(
            type="monitor",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attempts(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_attempts_with_all_params(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            cursor="wha_210b9798eb53baa4e69d31c1071cf03d",
            limit=1,
            tags=["production", "team-alpha"],
        )
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list_attempts(self, async_client: AsyncContextDev) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list_attempts(self, async_client: AsyncContextDev) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.list_attempts(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryListAttemptsResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_list_attempts(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.list_attempts(
                delivery_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retry_with_all_params(self, async_client: AsyncContextDev) -> None:
        delivery = await async_client.webhooks.deliveries.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
            force=True,
            tags=["production", "team-alpha"],
            idempotency_key="Idempotency-Key",
        )
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retry(self, async_client: AsyncContextDev) -> None:
        response = await async_client.webhooks.deliveries.with_raw_response.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        delivery = await response.parse()
        assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retry(self, async_client: AsyncContextDev) -> None:
        async with async_client.webhooks.deliveries.with_streaming_response.retry(
            delivery_id="whd_210b9798eb53baa4e69d31c1071cf03d",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            delivery = await response.parse()
            assert_matches_type(DeliveryRetryResponse, delivery, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retry(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `delivery_id` but received ''"):
            await async_client.webhooks.deliveries.with_raw_response.retry(
                delivery_id="",
            )
