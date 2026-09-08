# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing_extensions import Literal

import httpx

from ..types import parse_handle_params
from .._files import read_file_content, async_read_file_content
from .._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    BinaryTypes,
    FileContent,
    SequenceNotStr,
    AsyncBinaryTypes,
    omit,
    not_given,
)
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.parse_handle_response import ParseHandleResponse

__all__ = ["ParseResource", "AsyncParseResource"]


class ParseResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return ParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return ParseResourceWithStreamingResponse(self)

    def handle(
        self,
        body: FileContent | BinaryTypes,
        *,
        client: str | Omit = omit,
        extension: Literal[
            "txt",
            "text",
            "md",
            "markdown",
            "html",
            "htm",
            "xhtml",
            "xml",
            "rss",
            "atom",
            "csv",
            "tsv",
            "yaml",
            "yml",
            "py",
            "java",
            "js",
            "jsx",
            "mjs",
            "cjs",
            "json",
            "jsonl",
            "ndjson",
            "php",
            "sh",
            "bash",
            "zsh",
            "fish",
            "rb",
            "ts",
            "tsx",
            "rtf",
            "srt",
            "css",
            "scss",
            "less",
            "styl",
            "sass",
            "svg",
            "pdf",
            "docx",
            "doc",
            "xlsx",
            "xlsm",
            "xlsb",
            "xltx",
            "xltm",
            "xls",
            "pptx",
            "pptm",
            "ppsx",
            "ppsm",
            "potx",
            "potm",
            "ppt",
            "pps",
            "pot",
            "jpg",
            "jpeg",
            "jpe",
            "png",
            "gif",
            "bmp",
            "tiff",
            "tif",
            "webp",
            "ppm",
            "pbm",
            "pgm",
            "pnm",
        ]
        | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf: parse_handle_params.Pdf | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseHandleResponse:
        """
        Converts raw text, source code, web/data, PDF, Microsoft Office, and image bytes
        into LLM-usable Markdown.

        Args:
          client: Optional client identifier used for usage attribution.

          extension: Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
              md, py, rtf, jpg, png, or txt.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: When true for PDF inputs, OCR the selected pages that have no usable text layer
              (scans), replacing each recovered page's text with the OCR result while pages
              with a real text layer keep it. pdf.start/pdf.end limit the inclusive page
              range. Billed at 1 credit per page OCR actually recovered, on top of the base
              request cost. When false, no OCR runs.

          pdf: PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          use_main_content_only: Extract only the main content from HTML-like inputs

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return self._post(
            "/parse",
            content=read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "client": client,
                        "extension": extension,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf": pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "use_main_content_only": use_main_content_only,
                        "zdr": zdr,
                    },
                    parse_handle_params.ParseHandleParams,
                ),
            ),
            cast_to=ParseHandleResponse,
        )


class AsyncParseResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncParseResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#accessing-raw-response-data-eg-headers
        """
        return AsyncParseResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncParseResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/context-dot-dev/context-python-sdk#with_streaming_response
        """
        return AsyncParseResourceWithStreamingResponse(self)

    async def handle(
        self,
        body: FileContent | AsyncBinaryTypes,
        *,
        client: str | Omit = omit,
        extension: Literal[
            "txt",
            "text",
            "md",
            "markdown",
            "html",
            "htm",
            "xhtml",
            "xml",
            "rss",
            "atom",
            "csv",
            "tsv",
            "yaml",
            "yml",
            "py",
            "java",
            "js",
            "jsx",
            "mjs",
            "cjs",
            "json",
            "jsonl",
            "ndjson",
            "php",
            "sh",
            "bash",
            "zsh",
            "fish",
            "rb",
            "ts",
            "tsx",
            "rtf",
            "srt",
            "css",
            "scss",
            "less",
            "styl",
            "sass",
            "svg",
            "pdf",
            "docx",
            "doc",
            "xlsx",
            "xlsm",
            "xlsb",
            "xltx",
            "xltm",
            "xls",
            "pptx",
            "pptm",
            "ppsx",
            "ppsm",
            "potx",
            "potm",
            "ppt",
            "pps",
            "pot",
            "jpg",
            "jpeg",
            "jpe",
            "png",
            "gif",
            "bmp",
            "tiff",
            "tif",
            "webp",
            "ppm",
            "pbm",
            "pgm",
            "pnm",
        ]
        | Omit = omit,
        include_images: bool | Omit = omit,
        include_links: bool | Omit = omit,
        ocr: bool | Omit = omit,
        pdf: parse_handle_params.Pdf | Omit = omit,
        shorten_base64_images: bool | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        use_main_content_only: bool | Omit = omit,
        zdr: Literal["enabled", "disabled"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ParseHandleResponse:
        """
        Converts raw text, source code, web/data, PDF, Microsoft Office, and image bytes
        into LLM-usable Markdown.

        Args:
          client: Optional client identifier used for usage attribution.

          extension: Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
              md, py, rtf, jpg, png, or txt.

          include_images: Include image references in Markdown output

          include_links: Preserve hyperlinks in Markdown output

          ocr: When true for PDF inputs, OCR the selected pages that have no usable text layer
              (scans), replacing each recovered page's text with the OCR result while pages
              with a real text layer keep it. pdf.start/pdf.end limit the inclusive page
              range. Billed at 1 credit per page OCR actually recovered, on top of the base
              request cost. When false, no OCR runs.

          pdf: PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}.

          shorten_base64_images: Shorten base64-encoded image data in the Markdown output

          tags: Comma-separated tags for tracking request usage. Up to 20 tags, each 1-50
              characters.

          use_main_content_only: Extract only the main content from HTML-like inputs

          zdr: Set to enabled to bypass shared caches and omit request and response content
              from retained usage logs. Requires zero data retention to be enabled for your
              organization (contact support@context.dev), otherwise the request fails with
              ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Content-Type": "application/octet-stream", **(extra_headers or {})}
        return await self._post(
            "/parse",
            content=await async_read_file_content(body) if isinstance(body, os.PathLike) else body,
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "client": client,
                        "extension": extension,
                        "include_images": include_images,
                        "include_links": include_links,
                        "ocr": ocr,
                        "pdf": pdf,
                        "shorten_base64_images": shorten_base64_images,
                        "tags": tags,
                        "use_main_content_only": use_main_content_only,
                        "zdr": zdr,
                    },
                    parse_handle_params.ParseHandleParams,
                ),
            ),
            cast_to=ParseHandleResponse,
        )


class ParseResourceWithRawResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.handle = to_raw_response_wrapper(
            parse.handle,
        )


class AsyncParseResourceWithRawResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.handle = async_to_raw_response_wrapper(
            parse.handle,
        )


class ParseResourceWithStreamingResponse:
    def __init__(self, parse: ParseResource) -> None:
        self._parse = parse

        self.handle = to_streamed_response_wrapper(
            parse.handle,
        )


class AsyncParseResourceWithStreamingResponse:
    def __init__(self, parse: AsyncParseResource) -> None:
        self._parse = parse

        self.handle = async_to_streamed_response_wrapper(
            parse.handle,
        )
