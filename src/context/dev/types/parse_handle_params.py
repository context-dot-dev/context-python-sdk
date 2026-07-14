# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["ParseHandleParams", "Pdf"]


class ParseHandleParams(TypedDict, total=False):
    client: str
    """Optional client identifier used for usage attribution."""

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
    """
    Optional file extension hint, such as pdf, docx, xlsx, pptx, html, json, csv,
    md, py, rtf, jpg, png, or txt.
    """

    include_images: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    ocr: Union[bool, Literal["true", "false"]]
    """
    When true for PDF inputs, detect and OCR images embedded in the selected pages,
    inserting recognized text at each image's position in page reading order while
    preserving the PDF text layer. pdf.start/pdf.end limit the inclusive page range.
    When false, all OCR is disabled, including the automatic scanned-PDF fallback.
    """

    pdf: Pdf
    """PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}."""

    shorten_base64_images: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    use_main_content_only: Annotated[Union[bool, Literal["true", "false"]], PropertyInfo(alias="useMainContentOnly")]
    """Extract only the main content from HTML-like inputs"""


class Pdf(TypedDict, total=False):
    """PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}."""

    end: int
    """Last 1-based PDF page to parse.

    When omitted, parsing ends at the last page. Must be greater than or equal to
    start when both are provided.
    """

    start: int
    """First 1-based PDF page to parse.

    When omitted, parsing starts at the first page.
    """
