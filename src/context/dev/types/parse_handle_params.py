# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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

    include_images: Annotated[bool, PropertyInfo(alias="includeImages")]
    """Include image references in Markdown output"""

    include_links: Annotated[bool, PropertyInfo(alias="includeLinks")]
    """Preserve hyperlinks in Markdown output"""

    ocr: bool
    """Read text from images and scanned PDF pages. PDF page ranges still apply."""

    pdf: Pdf
    """PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    tags: SequenceNotStr[str]
    """Comma-separated labels for filtering usage, e.g. `production,team-alpha`."""

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Extract only the main content from HTML-like inputs"""

    zdr: Literal["enabled", "disabled"]
    """`enabled` turns on zero data retention.

    Returns 403 `ZDR_NOT_ENABLED` unless your organization has ZDR.
    """


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
