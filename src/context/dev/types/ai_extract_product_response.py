# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AIExtractProductResponse", "CacheMetadata", "KeyMetadata", "Product", "ProductVariant"]


class CacheMetadata(BaseModel):
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing to the output was a hit; age_ms is the oldest contributing hit.
    """

    age_ms: int
    """Age of the cached data in milliseconds. Zero for miss and zdr responses."""

    status: Literal["hit", "miss", "zdr"]
    """
    Whether the response was served from cache, required fresh work, or honored
    zero-data-retention cache bypass.
    """


class KeyMetadata(BaseModel):
    """Credit usage, included whenever a valid API key is provided."""

    credits_consumed: int
    """Credits used by this request."""

    credits_remaining: int
    """Credits remaining for your organization."""


class ProductVariant(BaseModel):
    attributes: Dict[str, str]
    """
    Explicit variant attributes such as color, size, material, pattern and
    properties declared by page.
    """

    images: List[str]
    """Original source image URLs explicitly attached to this variant."""

    sku: Optional[str] = None

    url: Optional[str] = None
    """Variant or offer URL when provided by the source. May be shared by variants."""


class Product(BaseModel):
    """The extracted product data, or null if not a product page"""

    description: str
    """Description of the product"""

    features: List[str]
    """List of product features"""

    images: List[str]
    """URLs to product images on the page (up to 7)"""

    name: str
    """Name of the product"""

    sku: Optional[str] = None
    """Stock Keeping Unit (product identifier). Null if no identifier is found."""

    tags: List[str]
    """Tags associated with the product"""

    target_audience: List[str]
    """Target audience for the product (array of strings)"""

    availability: Optional[
        Literal[
            "in_stock", "out_of_stock", "limited_availability", "preorder", "backorder", "made_to_order", "discontinued"
        ]
    ] = None
    """Normalized stock or ordering availability"""

    billing_frequency: Optional[Literal["monthly", "yearly", "one_time", "usage_based"]] = None
    """Billing frequency for the product"""

    category: Optional[str] = None
    """Category of the product"""

    currency: Optional[str] = None
    """Currency code for the price (e.g., USD, EUR)"""

    dimensions: Optional[List[str]] = None
    """
    Dimension statements shown for the product, preserving labels, values, and units
    """

    image_url: Optional[str] = None
    """URL to the product image"""

    price: Optional[float] = None
    """Price of the product"""

    pricing_model: Optional[Literal["per_seat", "flat", "tiered", "freemium", "custom"]] = None
    """Pricing model for the product"""

    regular_price: Optional[float] = None
    """Original or regular price before a displayed discount"""

    url: Optional[str] = None
    """URL to the product page"""

    variants: Optional[List[ProductVariant]] = None
    """
    Product variations, such as different colors or sizes, with their attributes and
    images. Empty if none are found. May not include every variation offered by the
    store.
    """


class AIExtractProductResponse(BaseModel):
    cache_metadata: CacheMetadata
    """Cache outcome for this response.

    Composite responses are hits only when every cache-controlled fetch contributing
    to the output was a hit; age_ms is the oldest contributing hit.
    """

    request_id: str
    """Unique id of this API call, also sent in the X-Request-Id response header.

    Quote it when contacting support about a failed request.
    """

    is_product_page: Optional[bool] = None
    """Whether the given URL is a product detail page"""

    key_metadata: Optional[KeyMetadata] = None
    """Credit usage, included whenever a valid API key is provided."""

    partial: Optional[bool] = None
    """
    True when the timeout ended processing and this response contains only usable
    results completed so far. Unfinished results are omitted.
    """

    platform: Optional[Literal["amazon", "tiktok_shop", "etsy", "generic"]] = None
    """The detected ecommerce platform, or null if not a product page"""

    product: Optional[Product] = None
    """The extracted product data, or null if not a product page"""
