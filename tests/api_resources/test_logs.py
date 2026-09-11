# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import LogListResponse, LogRetrieveResponse
from context.dev._utils import parse_datetime

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestLogs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ContextDev) -> None:
        log = client.logs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ContextDev) -> None:
        response = client.logs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ContextDev) -> None:
        with client.logs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.logs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ContextDev) -> None:
        log = client.logs.list()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ContextDev) -> None:
        log = client.logs.list(
            error_code="WEBSITE_ACCESS_ERROR",
            errors_only=True,
            from_=parse_datetime("2026-09-10T00:00:00Z"),
            key_id="x",
            limit=1,
            page=1,
            path="/brand/retrieve",
            search="acme.com",
            status_code=500,
            tags="nightly-import,team-alpha",
            to=parse_datetime("2026-09-11T00:00:00Z"),
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ContextDev) -> None:
        response = client.logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = response.parse()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ContextDev) -> None:
        with client.logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = response.parse()
            assert_matches_type(LogListResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncLogs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncContextDev) -> None:
        log = await async_client.logs.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncContextDev) -> None:
        response = await async_client.logs.with_raw_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogRetrieveResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncContextDev) -> None:
        async with async_client.logs.with_streaming_response.retrieve(
            "182bd5e5-6e1a-4fe4-a799-aa6d9a6ab26e",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogRetrieveResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncContextDev) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.logs.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncContextDev) -> None:
        log = await async_client.logs.list()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncContextDev) -> None:
        log = await async_client.logs.list(
            error_code="WEBSITE_ACCESS_ERROR",
            errors_only=True,
            from_=parse_datetime("2026-09-10T00:00:00Z"),
            key_id="x",
            limit=1,
            page=1,
            path="/brand/retrieve",
            search="acme.com",
            status_code=500,
            tags="nightly-import,team-alpha",
            to=parse_datetime("2026-09-11T00:00:00Z"),
        )
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncContextDev) -> None:
        response = await async_client.logs.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        log = await response.parse()
        assert_matches_type(LogListResponse, log, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncContextDev) -> None:
        async with async_client.logs.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            log = await response.parse()
            assert_matches_type(LogListResponse, log, path=["response"])

        assert cast(Any, response.is_closed) is True
