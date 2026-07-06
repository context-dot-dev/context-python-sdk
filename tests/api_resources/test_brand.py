# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    BrandRetrieveResponse,
    BrandRetrieveSimplifiedResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBrand:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overload_1(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
            type="by_domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params_overload_1(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            domain="domain",
            type="by_domain",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overload_1(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            domain="domain",
            type="by_domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overload_1(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            domain="domain",
            type="by_domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overload_2(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            name="xxx",
            type="by_name",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params_overload_2(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            name="xxx",
            type="by_name",
            country_gl="country_gl",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overload_2(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            name="xxx",
            type="by_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overload_2(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            name="xxx",
            type="by_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overload_3(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            email="dev@stainless.com",
            type="by_email",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params_overload_3(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            email="dev@stainless.com",
            type="by_email",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overload_3(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            email="dev@stainless.com",
            type="by_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overload_3(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            email="dev@stainless.com",
            type="by_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overload_4(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            ticker="ticker",
            type="by_ticker",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params_overload_4(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            ticker="ticker",
            type="by_ticker",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            ticker_exchange="ticker_exchange",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overload_4(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            ticker="ticker",
            type="by_ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overload_4(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            ticker="ticker",
            type="by_ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_overload_5(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params_overload_5(self, client: ContextDev) -> None:
        brand = client.brand.retrieve(
            transaction_info="xxx",
            type="by_transaction",
            city="city",
            country_gl="country_gl",
            force_language="afrikaans",
            high_confidence_only=True,
            max_speed=True,
            mcc=0,
            phone=0,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_overload_5(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_overload_5(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_simplified(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_simplified(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_simplified_with_all_params(self, client: ContextDev) -> None:
        brand = client.brand.retrieve_simplified(
            domain="domain",
            max_age_ms=86400000,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve_simplified(self, client: ContextDev) -> None:
        response = client.brand.with_raw_response.retrieve_simplified(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = response.parse()
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_simplified(self, client: ContextDev) -> None:
        with client.brand.with_streaming_response.retrieve_simplified(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = response.parse()
            assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBrand:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overload_1(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
            type="by_domain",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params_overload_1(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            domain="domain",
            type="by_domain",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overload_1(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            domain="domain",
            type="by_domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overload_1(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            domain="domain",
            type="by_domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overload_2(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            name="xxx",
            type="by_name",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params_overload_2(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            name="xxx",
            type="by_name",
            country_gl="country_gl",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overload_2(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            name="xxx",
            type="by_name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overload_2(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            name="xxx",
            type="by_name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overload_3(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            email="dev@stainless.com",
            type="by_email",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params_overload_3(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            email="dev@stainless.com",
            type="by_email",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overload_3(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            email="dev@stainless.com",
            type="by_email",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overload_3(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            email="dev@stainless.com",
            type="by_email",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overload_4(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            ticker="ticker",
            type="by_ticker",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params_overload_4(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            ticker="ticker",
            type="by_ticker",
            force_language="afrikaans",
            max_age_ms=0,
            max_speed=True,
            ticker_exchange="ticker_exchange",
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overload_4(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            ticker="ticker",
            type="by_ticker",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overload_4(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            ticker="ticker",
            type="by_ticker",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_overload_5(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params_overload_5(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve(
            transaction_info="xxx",
            type="by_transaction",
            city="city",
            country_gl="country_gl",
            force_language="afrikaans",
            high_confidence_only=True,
            max_speed=True,
            mcc=0,
            phone=0,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_overload_5(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_overload_5(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve(
            transaction_info="xxx",
            type="by_transaction",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_simplified(
            domain="domain",
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_simplified_with_all_params(self, async_client: AsyncContextDev) -> None:
        brand = await async_client.brand.retrieve_simplified(
            domain="domain",
            max_age_ms=86400000,
            timeout_ms=1000,
        )
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        response = await async_client.brand.with_raw_response.retrieve_simplified(
            domain="domain",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        brand = await response.parse()
        assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_simplified(self, async_client: AsyncContextDev) -> None:
        async with async_client.brand.with_streaming_response.retrieve_simplified(
            domain="domain",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            brand = await response.parse()
            assert_matches_type(BrandRetrieveSimplifiedResponse, brand, path=["response"])

        assert cast(Any, response.is_closed) is True
