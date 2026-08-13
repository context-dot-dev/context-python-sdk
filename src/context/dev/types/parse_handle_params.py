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
    """
    When true for PDF inputs, OCR the selected pages that have no usable text layer
    (scans), replacing each recovered page's text with the OCR result while pages
    with a real text layer keep it. pdf.start/pdf.end limit the inclusive page
    range. Billed at 1 credit per page OCR actually recovered, on top of the base
    request cost. When false, no OCR runs.
    """

    pdf: Pdf
    """PDF page-range options as a JSON object, e.g. {"start": 2, "end": 5}."""

    shorten_base64_images: Annotated[bool, PropertyInfo(alias="shortenBase64Images")]
    """Shorten base64-encoded image data in the Markdown output"""

    tags: SequenceNotStr[str]
    """Optional comma-separated caller-defined tags for tracking this request.

    Tags are recorded on the request's usage log and can be used to filter usage on
    the dashboard usage page. Up to 20 tags, each 1-50 characters.
    """

    use_main_content_only: Annotated[bool, PropertyInfo(alias="useMainContentOnly")]
    """Extract only the main content from HTML-like inputs"""

    zdr: Literal["enabled", "disabled"]
    """
    Set to enabled to bypass shared caches and omit request and response content
    from retained usage logs. Requires zero data retention to be enabled for your
    organization (contact support@context.dev), otherwise the request fails with
    ZDR_NOT_ENABLED. Successful ZDR responses include X-Context-ZDR: true.
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
