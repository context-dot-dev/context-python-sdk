# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["ParseHandleResponse", "KeyMetadata"]


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class ParseHandleResponse(BaseModel):
    markdown: str
    """Input bytes converted to GitHub Flavored Markdown"""

    success: Literal[True]
    """Indicates success"""

    type: Literal[
        "html",
        "xml",
        "json",
        "jsonl",
        "text",
        "csv",
        "tsv",
        "markdown",
        "yaml",
        "python",
        "java",
        "javascript",
        "php",
        "shell",
        "ruby",
        "typescript",
        "rtf",
        "srt",
        "css",
        "scss",
        "less",
        "stylus",
        "sass",
        "svg",
        "pdf",
        "docx",
        "doc",
        "xlsx",
        "xls",
        "pptx",
        "ppt",
        "jpg",
        "png",
        "gif",
        "bmp",
        "tiff",
        "webp",
        "ppm",
        "pbm",
        "pgm",
        "pnm",
    ]
    """Detected content type used for parsing"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""
