# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import (
    BatchListResponse,
    BatchCancelResponse,
    BatchSubmitResponse,
    BatchRetrieveResponse,
    BatchGetResultsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBatch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ContextDev) -> None:
        batch = client.batch.retrieve(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve_with_all_params(self, client: ContextDev) -> None:
        batch = client.batch.retrieve(
            batch_id="batch_9f2c8a",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ContextDev) -> None:
        response = client.batch.with_raw_response.retrieve(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ContextDev) -> None:
        with client.batch.with_streaming_response.retrieve(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batch.with_raw_response.retrieve(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ContextDev) -> None:
        batch = client.batch.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ContextDev) -> None:
        batch = client.batch.list(
            cursor="cursor",
            limit=1,
            status="queued",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ContextDev) -> None:
        response = client.batch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ContextDev) -> None:
        with client.batch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel(self, client: ContextDev) -> None:
        batch = client.batch.cancel(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_cancel_with_all_params(self, client: ContextDev) -> None:
        batch = client.batch.cancel(
            batch_id="batch_9f2c8a",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_cancel(self, client: ContextDev) -> None:
        response = client.batch.with_raw_response.cancel(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_cancel(self, client: ContextDev) -> None:
        with client.batch.with_streaming_response.cancel(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_cancel(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batch.with_raw_response.cancel(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results(self, client: ContextDev) -> None:
        batch = client.batch.get_results(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get_results_with_all_params(self, client: ContextDev) -> None:
        batch = client.batch.get_results(
            batch_id="batch_9f2c8a",
            cursor="cursor",
            limit=1,
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get_results(self, client: ContextDev) -> None:
        response = client.batch.with_raw_response.get_results(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get_results(self, client: ContextDev) -> None:
        with client.batch.with_streaming_response.get_results(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get_results(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            client.batch.with_raw_response.get_results(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: ContextDev) -> None:
        batch = client.batch.submit(
            identifiers={},
        )
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: ContextDev) -> None:
        batch = client.batch.submit(
            identifiers={"linkedin_url": "https://www.linkedin.com/in/yahia-bakour/"},
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: ContextDev) -> None:
        response = client.batch.with_raw_response.submit(
            identifiers={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = response.parse()
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: ContextDev) -> None:
        with client.batch.with_streaming_response.submit(
            identifiers={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = response.parse()
            assert_matches_type(BatchSubmitResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBatch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.retrieve(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.retrieve(
            batch_id="batch_9f2c8a",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextDev) -> None:
        response = await async_client.batch.with_raw_response.retrieve(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextDev) -> None:
        async with async_client.batch.with_streaming_response.retrieve(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchRetrieveResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batch.with_raw_response.retrieve(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.list()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.list(
            cursor="cursor",
            limit=1,
            status="queued",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextDev) -> None:
        response = await async_client.batch.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchListResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextDev) -> None:
        async with async_client.batch.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchListResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.cancel(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_cancel_with_all_params(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.cancel(
            batch_id="batch_9f2c8a",
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_cancel(self, async_client: AsyncContextDev) -> None:
        response = await async_client.batch.with_raw_response.cancel(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchCancelResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_cancel(self, async_client: AsyncContextDev) -> None:
        async with async_client.batch.with_streaming_response.cancel(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchCancelResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_cancel(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batch.with_raw_response.cancel(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.get_results(
            batch_id="batch_9f2c8a",
        )
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get_results_with_all_params(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.get_results(
            batch_id="batch_9f2c8a",
            cursor="cursor",
            limit=1,
            tags=["production", "team-alpha"],
        )
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get_results(self, async_client: AsyncContextDev) -> None:
        response = await async_client.batch.with_raw_response.get_results(
            batch_id="batch_9f2c8a",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get_results(self, async_client: AsyncContextDev) -> None:
        async with async_client.batch.with_streaming_response.get_results(
            batch_id="batch_9f2c8a",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchGetResultsResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get_results(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `batch_id` but received ''"):
            await async_client.batch.with_raw_response.get_results(
                batch_id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.submit(
            identifiers={},
        )
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncContextDev) -> None:
        batch = await async_client.batch.submit(
            identifiers={"linkedin_url": "https://www.linkedin.com/in/yahia-bakour/"},
            tags=["production", "team-alpha"],
            timeout_ms=1000,
        )
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncContextDev) -> None:
        response = await async_client.batch.with_raw_response.submit(
            identifiers={},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        batch = await response.parse()
        assert_matches_type(BatchSubmitResponse, batch, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncContextDev) -> None:
        async with async_client.batch.with_streaming_response.submit(
            identifiers={},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            batch = await response.parse()
            assert_matches_type(BatchSubmitResponse, batch, path=["response"])

        assert cast(Any, response.is_closed) is True
