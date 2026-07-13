# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import ParseHandleResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestParse:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_handle(self, client: ContextDev) -> None:
        parse = client.parse.handle(
            body=b"Example data",
        )
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_handle_with_all_params(self, client: ContextDev) -> None:
        parse = client.parse.handle(
            body=b"Example data",
            extension="txt",
            include_images=True,
            include_links=True,
            ocr=True,
            pdf={
                "end": 1,
                "start": 1,
            },
            shorten_base64_images=True,
            tags=["production", "team-alpha"],
            use_main_content_only=True,
        )
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_handle(self, client: ContextDev) -> None:
        response = client.parse.with_raw_response.handle(
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = response.parse()
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_handle(self, client: ContextDev) -> None:
        with client.parse.with_streaming_response.handle(
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = response.parse()
            assert_matches_type(ParseHandleResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncParse:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_handle(self, async_client: AsyncContextDev) -> None:
        parse = await async_client.parse.handle(
            body=b"Example data",
        )
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_handle_with_all_params(self, async_client: AsyncContextDev) -> None:
        parse = await async_client.parse.handle(
            body=b"Example data",
            extension="txt",
            include_images=True,
            include_links=True,
            ocr=True,
            pdf={
                "end": 1,
                "start": 1,
            },
            shorten_base64_images=True,
            tags=["production", "team-alpha"],
            use_main_content_only=True,
        )
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_handle(self, async_client: AsyncContextDev) -> None:
        response = await async_client.parse.with_raw_response.handle(
            body=b"Example data",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        parse = await response.parse()
        assert_matches_type(ParseHandleResponse, parse, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_handle(self, async_client: AsyncContextDev) -> None:
        async with async_client.parse.with_streaming_response.handle(
            body=b"Example data",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            parse = await response.parse()
            assert_matches_type(ParseHandleResponse, parse, path=["response"])

        assert cast(Any, response.is_closed) is True
