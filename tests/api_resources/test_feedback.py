# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from context.dev import ContextDev, AsyncContextDev
from tests.utils import assert_matches_type
from context.dev.types import FeedbackSubmitResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFeedback:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit(self, client: ContextDev) -> None:
        feedback = client.feedback.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: ContextDev) -> None:
        feedback = client.feedback.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
            request_id="3f1c2a6e-8b4d-4c1e-9f0a-2d7b5e6c8a91",
            tags=["production", "team-alpha"],
            url="https://stripe.com/pricing",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: ContextDev) -> None:
        response = client.feedback.with_raw_response.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = response.parse()
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: ContextDev) -> None:
        with client.feedback.with_streaming_response.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = response.parse()
            assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFeedback:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncContextDev) -> None:
        feedback = await async_client.feedback.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncContextDev) -> None:
        feedback = await async_client.feedback.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
            request_id="3f1c2a6e-8b4d-4c1e-9f0a-2d7b5e6c8a91",
            tags=["production", "team-alpha"],
            url="https://stripe.com/pricing",
        )
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncContextDev) -> None:
        response = await async_client.feedback.with_raw_response.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        feedback = await response.parse()
        assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncContextDev) -> None:
        async with async_client.feedback.with_streaming_response.submit(
            category="bug",
            note="Markdown drops the plan comparison table; expected all 4 rows.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            feedback = await response.parse()
            assert_matches_type(FeedbackSubmitResponse, feedback, path=["response"])

        assert cast(Any, response.is_closed) is True
