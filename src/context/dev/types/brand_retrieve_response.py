# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "BrandRetrieveResponse",
    "Brand",
    "BrandAddress",
    "BrandBackdrop",
    "BrandBackdropColor",
    "BrandBackdropResolution",
    "BrandColor",
    "BrandEmployees",
    "BrandIndustries",
    "BrandIndustriesEic",
    "BrandLinks",
    "BrandLogo",
    "BrandLogoColor",
    "BrandLogoResolution",
    "BrandSocial",
    "BrandStock",
    "CacheMetadata",
    "KeyMetadata",
]


class BrandAddress(BaseModel):
    """Physical address of the brand. Omitted when unknown."""

    city: Optional[str] = None
    """City."""

    country: Optional[str] = None
    """Country name."""

    country_code: Optional[str] = None
    """Country code, such as `US`."""

    postal_code: Optional[str] = None
    """Postal or ZIP code."""

    state_code: Optional[str] = None
    """State or province code."""

    state_province: Optional[str] = None
    """State or province name."""

    street: Optional[str] = None
    """Street address."""


class BrandBackdropColor(BaseModel):
    hex: Optional[str] = None
    """Hex color code, such as `#635BFF`."""

    name: Optional[str] = None
    """Human-readable color name."""


class BrandBackdropResolution(BaseModel):
    """Size of the backdrop image."""

    aspect_ratio: Optional[float] = None
    """Aspect ratio, as width divided by height."""

    height: Optional[int] = None
    """Height, in pixels."""

    width: Optional[int] = None
    """Width, in pixels."""


class BrandBackdrop(BaseModel):
    colors: Optional[List[BrandBackdropColor]] = None
    """Colors in the backdrop image."""

    resolution: Optional[BrandBackdropResolution] = None
    """Size of the backdrop image."""

    url: Optional[str] = None
    """URL of the backdrop image."""


class BrandColor(BaseModel):
    hex: Optional[str] = None
    """Hex color code, such as `#635BFF`."""

    name: Optional[str] = None
    """Human-readable color name."""

    source: Optional[Literal["site", "logo"]] = None
    """
    `site` colors come from the website's own theme (rendered page colors, web app
    manifest, `theme-color` meta tag); `logo` colors come from logo pixels.
    """


class BrandEmployees(BaseModel):
    """Employee headcount. Omitted when unknown."""

    exact: Optional[int] = None
    """Exact employee count, when known."""

    range: Optional[
        Literal[
            "1 to 10", "11 to 50", "51 to 200", "201 to 500", "501 to 1000", "1001 to 5000", "5001 to 10000", "10001+"
        ]
    ] = None
    """Headcount range, such as `11 to 50`."""


class BrandIndustriesEic(BaseModel):
    industry: Literal[
        "Aerospace & Defense",
        "Technology",
        "Finance",
        "Healthcare",
        "Retail & E-commerce",
        "Entertainment",
        "Education",
        "Government & Nonprofit",
        "Industrial & Energy",
        "Automotive & Transportation",
        "Lifestyle & Leisure",
        "Luxury & Fashion",
        "News & Media",
        "Sports",
        "Real Estate & PropTech",
        "Legal & Compliance",
        "Telecommunications",
        "Agriculture & Food",
        "Professional Services & Agencies",
        "Chemicals & Materials",
        "Logistics & Supply Chain",
        "Hospitality & Tourism",
        "Construction & Built Environment",
        "Consumer Packaged Goods (CPG)",
    ]
    """Top-level industry in the Easy Industry Classification (EIC)."""

    subindustry: Literal[
        "Defense Systems & Military Hardware",
        "Aerospace Manufacturing",
        "Avionics & Navigation Technology",
        "Subsea & Naval Defense Systems",
        "Space & Satellite Technology",
        "Defense IT & Systems Integration",
        "Software (B2B)",
        "Software (B2C)",
        "Cloud Infrastructure & DevOps",
        "Cybersecurity",
        "Artificial Intelligence & Machine Learning",
        "Data Infrastructure & Analytics",
        "Hardware & Semiconductors",
        "Fintech Infrastructure",
        "eCommerce & Marketplace Platforms",
        "Developer Tools & APIs",
        "Web3 & Blockchain",
        "XR & Spatial Computing",
        "Banking & Lending",
        "Investment Management & WealthTech",
        "Insurance & InsurTech",
        "Payments & Money Movement",
        "Accounting, Tax & Financial Planning Tools",
        "Capital Markets & Trading Platforms",
        "Financial Infrastructure & APIs",
        "Credit Scoring & Risk Management",
        "Cryptocurrency & Digital Assets",
        "BNPL & Alternative Financing",
        "Healthcare Providers & Services",
        "Pharmaceuticals & Drug Development",
        "Medical Devices & Diagnostics",
        "Biotechnology & Genomics",
        "Digital Health & Telemedicine",
        "Health Insurance & Benefits Tech",
        "Clinical Trials & Research Platforms",
        "Mental Health & Wellness",
        "Healthcare IT & EHR Systems",
        "Consumer Health & Wellness Products",
        "Online Marketplaces",
        "Direct-to-Consumer (DTC) Brands",
        "Retail Tech & Point-of-Sale Systems",
        "Omnichannel & In-Store Retail",
        "E-commerce Enablement & Infrastructure",
        "Subscription & Membership Commerce",
        "Social Commerce & Influencer Platforms",
        "Fashion & Apparel Retail",
        "Food, Beverage & Grocery E-commerce",
        "Streaming Platforms (Video, Music, Audio)",
        "Gaming & Interactive Entertainment",
        "Creator Economy & Influencer Platforms",
        "Film, TV & Production Studios",
        "Events, Venues & Live Entertainment",
        "Virtual Worlds & Metaverse Experiences",
        "K-12 Education Platforms & Tools",
        "Higher Education & University Tech",
        "Online Learning & MOOCs",
        "Test Prep & Certification",
        "Corporate Training & Upskilling",
        "Tutoring & Supplemental Learning",
        "Education Management Systems (LMS/SIS)",
        "Language Learning",
        "Creator-Led & Cohort-Based Courses",
        "Special Education & Accessibility Tools",
        "Government Technology & Digital Services",
        "Civic Engagement & Policy Platforms",
        "International Development & Humanitarian Aid",
        "Philanthropy & Grantmaking",
        "Nonprofit Operations & Fundraising Tools",
        "Public Health & Social Services",
        "Education & Youth Development Programs",
        "Environmental & Climate Action Organizations",
        "Legal Aid & Social Justice Advocacy",
        "Municipal & Infrastructure Services",
        "Manufacturing & Industrial Automation",
        "Energy Production (Oil, Gas, Nuclear)",
        "Renewable Energy & Cleantech",
        "Utilities & Grid Infrastructure",
        "Industrial IoT & Monitoring Systems",
        "Construction & Heavy Equipment",
        "Mining & Natural Resources",
        "Environmental Engineering & Sustainability",
        "Energy Storage & Battery Technology",
        "Automotive OEMs & Vehicle Manufacturing",
        "Electric Vehicles (EVs) & Charging Infrastructure",
        "Mobility-as-a-Service (MaaS)",
        "Fleet Management",
        "Public Transit & Urban Mobility",
        "Autonomous Vehicles & ADAS",
        "Aftermarket Parts & Services",
        "Telematics & Vehicle Connectivity",
        "Aviation & Aerospace Transport",
        "Maritime Shipping",
        "Fitness & Wellness",
        "Beauty & Personal Care",
        "Home & Living",
        "Dating & Relationships",
        "Hobbies, Crafts & DIY",
        "Outdoor & Recreational Gear",
        "Events, Experiences & Ticketing Platforms",
        "Designer & Luxury Apparel",
        "Accessories, Jewelry & Watches",
        "Footwear & Leather Goods",
        "Beauty, Fragrance & Skincare",
        "Fashion Marketplaces & Retail Platforms",
        "Sustainable & Ethical Fashion",
        "Resale, Vintage & Circular Fashion",
        "Fashion Tech & Virtual Try-Ons",
        "Streetwear & Emerging Luxury",
        "Couture & Made-to-Measure",
        "News Publishing & Journalism",
        "Advertising, Adtech & Media Buying",
        "Digital Media & Content Platforms",
        "Broadcasting (TV & Radio)",
        "Podcasting & Audio Media",
        "News Aggregators & Curation Tools",
        "Independent & Creator-Led Media",
        "Newsletters & Substack-Style Platforms",
        "Political & Investigative Media",
        "Trade & Niche Publications",
        "Media Monitoring & Analytics",
        "Professional Teams & Leagues",
        "Sports Media & Broadcasting",
        "Sports Betting & Fantasy Sports",
        "Fitness & Athletic Training Platforms",
        "Sportswear & Equipment",
        "Esports & Competitive Gaming",
        "Sports Venues & Event Management",
        "Athlete Management & Talent Agencies",
        "Sports Tech & Performance Analytics",
        "Youth, Amateur & Collegiate Sports",
        "Real Estate Marketplaces",
        "Property Management Software",
        "Rental Platforms",
        "Mortgage & Lending Tech",
        "Real Estate Investment Platforms",
        "Law Firms & Legal Services",
        "Legal Tech & Automation",
        "Regulatory Compliance",
        "E-Discovery & Litigation Tools",
        "Contract Management",
        "Governance, Risk & Compliance (GRC)",
        "IP & Trademark Management",
        "Legal Research & Intelligence",
        "Compliance Training & Certification",
        "Whistleblower & Ethics Reporting",
        "Mobile & Wireless Networks (3G/4G/5G)",
        "Broadband & Fiber Internet",
        "Satellite & Space-Based Communications",
        "Network Equipment & Infrastructure",
        "Telecom Billing & OSS/BSS Systems",
        "VoIP & Unified Communications",
        "Internet Service Providers (ISPs)",
        "Edge Computing & Network Virtualization",
        "IoT Connectivity Platforms",
        "Precision Agriculture & AgTech",
        "Crop & Livestock Production",
        "Food & Beverage Manufacturing & Processing",
        "Food Distribution",
        "Restaurants & Food Service",
        "Agricultural Inputs & Equipment",
        "Sustainable & Regenerative Agriculture",
        "Seafood & Aquaculture",
        "Management Consulting",
        "Marketing & Advertising Agencies",
        "Design, Branding & Creative Studios",
        "IT Services & Managed Services",
        "Staffing, Recruiting & Talent",
        "Accounting & Tax Firms",
        "Public Relations & Communications",
        "Business Process Outsourcing (BPO)",
        "Professional Training & Coaching",
        "Specialty Chemicals",
        "Commodity & Petrochemicals",
        "Polymers, Plastics & Rubber",
        "Coatings, Adhesives & Sealants",
        "Industrial Gases",
        "Advanced Materials & Composites",
        "Battery Materials & Energy Storage",
        "Electronic Materials & Semiconductor Chemicals",
        "Agrochemicals & Fertilizers",
        "Freight & Transportation Tech",
        "Last-Mile Delivery",
        "Warehouse Automation",
        "Supply Chain Visibility Platforms",
        "Logistics Marketplaces",
        "Shipping & Freight Forwarding",
        "Cold Chain Logistics",
        "Reverse Logistics & Returns",
        "Cross-Border Trade Tech",
        "Transportation Management Systems (TMS)",
        "Hotels & Accommodation",
        "Vacation Rentals & Short-Term Stays",
        "Restaurant Tech & Management",
        "Travel Booking Platforms",
        "Tourism Experiences & Activities",
        "Cruise Lines & Marine Tourism",
        "Hospitality Management Systems",
        "Event & Venue Management",
        "Corporate Travel Management",
        "Travel Insurance & Protection",
        "Construction Management Software",
        "BIM/CAD & Design Tools",
        "Construction Marketplaces",
        "Equipment Rental & Management",
        "Building Materials & Procurement",
        "Construction Workforce Management",
        "Project Estimation & Bidding",
        "Modular & Prefab Construction",
        "Construction Safety & Compliance",
        "Smart Building Technology",
        "Food & Beverage CPG",
        "Home & Personal Care CPG",
        "CPG Analytics & Insights",
        "Direct-to-Consumer CPG Brands",
        "CPG Supply Chain & Distribution",
        "Private Label Manufacturing",
        "CPG Retail Intelligence",
        "Sustainable CPG & Packaging",
        "Beauty & Cosmetics CPG",
        "Health & Wellness CPG",
    ]
    """Subindustry in the Easy Industry Classification (EIC)."""


class BrandIndustries(BaseModel):
    """Industry classification of the brand."""

    eic: Optional[List[BrandIndustriesEic]] = None
    """
    Industry and subindustry pairs from Context.dev's Easy Industry Classification
    (EIC).
    """


class BrandLinks(BaseModel):
    """Key pages on the brand's website."""

    blog: Optional[str] = None
    """URL of the blog or newsroom. `null` when not found."""

    careers: Optional[str] = None
    """URL of the careers page. `null` when not found."""

    contact: Optional[str] = None
    """URL of the contact page. `null` when not found."""

    pricing: Optional[str] = None
    """URL of the pricing page. `null` when not found."""

    privacy: Optional[str] = None
    """URL of the privacy policy. `null` when not found."""

    terms: Optional[str] = None
    """URL of the terms of service. `null` when not found."""


class BrandLogoColor(BaseModel):
    hex: Optional[str] = None
    """Hex color code, such as `#635BFF`."""

    name: Optional[str] = None
    """Human-readable color name."""


class BrandLogoResolution(BaseModel):
    """Size of the logo image."""

    aspect_ratio: Optional[float] = None
    """Aspect ratio, as width divided by height."""

    height: Optional[int] = None
    """Height, in pixels."""

    width: Optional[int] = None
    """Width, in pixels."""


class BrandLogo(BaseModel):
    colors: Optional[List[BrandLogoColor]] = None
    """Colors in the logo."""

    mode: Optional[Literal["light", "dark", "has_opaque_background"]] = None
    """
    `light` works best in light mode, `dark` works best in dark mode, and
    `has_opaque_background` works in either because the image has its own
    background.
    """

    resolution: Optional[BrandLogoResolution] = None
    """Size of the logo image."""

    type: Optional[Literal["icon", "logo"]] = None
    """Whether the image is an `icon` or a full `logo`, based on its dimensions."""

    url: Optional[str] = None
    """URL of the hosted logo image."""


class BrandSocial(BaseModel):
    type: Optional[
        Literal[
            "x",
            "facebook",
            "instagram",
            "linkedin",
            "youtube",
            "pinterest",
            "tiktok",
            "dribbble",
            "github",
            "behance",
            "snapchat",
            "whatsapp",
            "telegram",
            "line",
            "discord",
            "twitch",
            "vimeo",
            "imdb",
            "tumblr",
            "flickr",
            "giphy",
            "medium",
            "spotify",
            "soundcloud",
            "tripadvisor",
            "yelp",
            "producthunt",
            "reddit",
            "crunchbase",
            "appstore",
            "playstore",
        ]
    ] = None
    """Social platform."""

    url: Optional[str] = None
    """URL of the brand's profile on that platform."""


class BrandStock(BaseModel):
    """Stock listing. Omitted when the company is not publicly traded."""

    exchange: Optional[str] = None
    """Exchange the stock trades on."""

    ticker: Optional[str] = None
    """Stock ticker symbol."""


class Brand(BaseModel):
    """The brand's identity, visual assets, and company details."""

    address: Optional[BrandAddress] = None
    """Physical address of the brand. Omitted when unknown."""

    backdrops: Optional[List[BrandBackdrop]] = None
    """Backdrop images for the brand, such as social profile banners."""

    colors: Optional[List[BrandColor]] = None
    """Brand colors from the website and logos."""

    description: Optional[str] = None
    """Short description of the brand."""

    domain: Optional[str] = None
    """Domain of the brand."""

    email: Optional[str] = None
    """Contact email address for the company."""

    employees: Optional[BrandEmployees] = None
    """Employee headcount. Omitted when unknown."""

    industries: Optional[BrandIndustries] = None
    """Industry classification of the brand."""

    is_nsfw: Optional[bool] = None
    """Whether the brand's content is not safe for work (NSFW)."""

    links: Optional[BrandLinks] = None
    """Key pages on the brand's website."""

    logos: Optional[List[BrandLogo]] = None
    """Brand logos, most relevant first.

    An SVG is listed ahead of a raster logo of the same shape.
    """

    phone: Optional[str] = None
    """Contact phone number for the company."""

    primary_language: Optional[
        Literal[
            "afrikaans",
            "albanian",
            "amharic",
            "arabic",
            "armenian",
            "assamese",
            "aymara",
            "azeri",
            "basque",
            "belarusian",
            "bengali",
            "bosnian",
            "bulgarian",
            "burmese",
            "cantonese",
            "catalan",
            "cebuano",
            "chinese",
            "corsican",
            "croatian",
            "czech",
            "danish",
            "dutch",
            "english",
            "esperanto",
            "estonian",
            "farsi",
            "fijian",
            "finnish",
            "french",
            "galician",
            "georgian",
            "german",
            "greek",
            "guarani",
            "gujarati",
            "haitian-creole",
            "hausa",
            "hawaiian",
            "hebrew",
            "hindi",
            "hmong",
            "hungarian",
            "icelandic",
            "igbo",
            "indonesian",
            "irish",
            "italian",
            "japanese",
            "javanese",
            "kannada",
            "kazakh",
            "khmer",
            "kinyarwanda",
            "korean",
            "kurdish",
            "kyrgyz",
            "lao",
            "latin",
            "latvian",
            "lingala",
            "lithuanian",
            "luxembourgish",
            "macedonian",
            "malagasy",
            "malay",
            "malayalam",
            "maltese",
            "maori",
            "marathi",
            "mongolian",
            "nepali",
            "norwegian",
            "odia",
            "oromo",
            "pashto",
            "pidgin",
            "polish",
            "portuguese",
            "punjabi",
            "quechua",
            "romanian",
            "russian",
            "samoan",
            "scottish-gaelic",
            "serbian",
            "sesotho",
            "shona",
            "sindhi",
            "sinhala",
            "slovak",
            "slovene",
            "somali",
            "spanish",
            "sundanese",
            "swahili",
            "swedish",
            "tagalog",
            "tajik",
            "tamil",
            "tatar",
            "telugu",
            "thai",
            "tibetan",
            "tigrinya",
            "tongan",
            "tswana",
            "turkish",
            "turkmen",
            "ukrainian",
            "urdu",
            "uyghur",
            "uzbek",
            "vietnamese",
            "welsh",
            "wolof",
            "xhosa",
            "yiddish",
            "yoruba",
            "zulu",
        ]
    ] = None
    """Lowercase language name, such as `english`."""

    slogan: Optional[str] = None
    """Brand slogan or tagline."""

    socials: Optional[List[BrandSocial]] = None
    """Social media profiles of the brand."""

    stock: Optional[BrandStock] = None
    """Stock listing. Omitted when the company is not publicly traded."""

    title: Optional[str] = None
    """Brand name."""


class CacheMetadata(BaseModel):
    """Cache status of this response."""

    age_ms: int
    """Age of the cached data, in milliseconds. `0` for `miss` and `zdr`."""

    status: Literal["hit", "miss", "zdr"]
    """
    `hit` when served from cache, `miss` when fetched fresh, `zdr` when zero data
    retention bypassed the cache.
    """


class KeyMetadata(BaseModel):
    """Credits this request used and your remaining balance."""

    credits_consumed: int
    """Credits charged for this request."""

    credits_remaining: int
    """Credits your organization has left after this request."""


class BrandRetrieveResponse(BaseModel):
    brand: Brand
    """The brand's identity, visual assets, and company details."""

    cache_metadata: CacheMetadata
    """Cache status of this response."""

    code: int
    """HTTP status code. Always `200` on success."""

    request_id: str
    """Unique ID of this request, also in `X-Request-Id`.

    Include it when contacting support.
    """

    status: str
    """Always `ok` on success."""

    key_metadata: Optional[KeyMetadata] = None
    """Credits this request used and your remaining balance."""

    partial: Optional[bool] = None
    """`true` when the `timeoutOpts` deadline ended processing early.

    The response holds the data completed so far; unfinished fields are omitted.
    """
