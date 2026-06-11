# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["AIExtractProductResponse", "KeyMetadata", "Product"]


class KeyMetadata(BaseModel):
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the response status is not 200.
    """

    credits_consumed: int
    """The number of credits consumed by this request."""

    credits_remaining: int
    """The number of credits remaining for your organization after this request."""


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

    billing_frequency: Optional[Literal["monthly", "yearly", "one_time", "usage_based"]] = None
    """Billing frequency for the product"""

    category: Optional[str] = None
    """Category of the product"""

    currency: Optional[str] = None
    """Currency code for the price (e.g., USD, EUR)"""

    image_url: Optional[str] = None
    """URL to the product image"""

    price: Optional[float] = None
    """Price of the product"""

    pricing_model: Optional[Literal["per_seat", "flat", "tiered", "freemium", "custom"]] = None
    """Pricing model for the product"""

    url: Optional[str] = None
    """URL to the product page"""


class AIExtractProductResponse(BaseModel):
    is_product_page: Optional[bool] = None
    """Whether the given URL is a product detail page"""

    key_metadata: Optional[KeyMetadata] = None
    """Metadata about the API key used for the request.

    Included in every response whenever a valid API key is provided, even when the
    response status is not 200.
    """

    platform: Optional[Literal["amazon", "tiktok_shop", "etsy", "generic"]] = None
    """The detected ecommerce platform, or null if not a product page"""

    product: Optional[Product] = None
    """The extracted product data, or null if not a product page"""
