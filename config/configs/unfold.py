from django.conf.urls.static import static
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

UNFOLD = {
    "SITE_TITLE": "Custom suffix in <title> tag",
    "SITE_HEADER": "Custom suffix in <h1> tag",
    "SITE_URL": "/",
    # "SITE_ICON": lambda request: static("icon.svg"),  # both modes, optimise for 32px height
    # "SITE_ICON": {
    #     "light": lambda request: static("icon-light.svg"),  # light mode
    #     "dark": lambda request: static("icon-dark.svg"),  # dark mode
    # },
    # # "SITE_LOGO": lambda request: static("logo.svg"),  # both modes, optimise for 32px height
    # "SITE_LOGO": {
    #     "light": lambda request: static("logo-light.svg"),  # light mode
    #     "dark": lambda request: static("logo-dark.svg"),  # dark mode
    # },
    "SITE_SYMBOL": "speed",  # symbol from icon set
    # "SITE_FAVICONS": [
    #     {
    #         "rel": "icon",
    #         "sizes": "32x32",
    #         "type": "image/svg+xml",
    #         "href": lambda request: static("favicon.svg"),
    #     },
    # ],
    "SHOW_HISTORY": True, # show/hide "History" button, default: True
    "SHOW_VIEW_ON_SITE": True, # show/hide "View on site" button, default: True
    # "ENVIRONMENT": "sample_app.environment_callback",
    # "DASHBOARD_CALLBACK": "sample_app.dashboard_callback",
    "THEME": "dark", # Force theme: "dark" or "light". Will disable theme switcher
    "LOGIN": {
        "image": lambda request: static("sample/login-bg.jpg"),
        "redirect_after": lambda request: reverse_lazy("admin:authentication_user_changelist"),
    },
    # "STYLES": [
    #     lambda request: static("css/style.css"),
    # ],
    # "SCRIPTS": [
    #     lambda request: static("js/script.js"),
    # ],
    "COLORS": {
        "font": {
            "subtle-light": "107 114 128",
            "subtle-dark": "156 163 175",
            "default-light": "75 85 99",
            "default-dark": "209 213 219",
            "important-light": "17 24 39",
            "important-dark": "243 244 246",
        },
        "primary": {
            "50": "250 245 255",
            "100": "243 232 255",
            "200": "233 213 255",
            "300": "216 180 254",
            "400": "192 132 252",
            "500": "168 85 247",
            "600": "147 51 234",
            "700": "126 34 206",
            "800": "107 33 168",
            "900": "88 28 135",
            "950": "59 7 100",
        },
    },
    # "EXTENSIONS": {
    #     "modeltranslation": {
    #         "flags": {
    #             "en": "🇬🇧",
    #             "fr": "🇫🇷",
    #             "nl": "🇧🇪",
    #         },
    #     },
    # },
     "SIDEBAR": {
        "show_search": True,  # Disable search in applications and models names
        "show_all_applications": True,  # Disable dropdown with all applications and models
        "navigation": [
            {
                "title": _("User"),
                "icon": "person",
                "collapsible": True,
                "items": [
                    {
                        "title": _("User Address"),
                        "icon": "home",
                        "link": reverse_lazy("admin:authentication_useraddress_changelist"),
                    },
                    {
                        "title": _("User"),
                        "icon": "person",
                        "link": reverse_lazy("admin:authentication_user_changelist"),
                    },
                ],
            },
            {
                "title": _("Restaurants"),
                "icon": "restaurant",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Restaurants"),
                        "icon": "coffee",
                        "link": reverse_lazy("admin:orders_restaurant_changelist"),
                    },
                    {
                        "title": _("Orders"),
                        "icon": "archive",
                        "link": reverse_lazy("admin:orders_order_changelist"),
                    },
                    {
                        "title": _("Deliveries"),
                        "icon": "local_shipping",
                        "link": reverse_lazy("admin:orders_delivery_changelist"),
                    },
                ],
            },
            {
                "title": _("Products"),
                "icon": "fastfood",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Products"),
                        "icon": "local_pizza",
                        "link": reverse_lazy("admin:product_product_changelist"),
                    },
                    {
                        "title": _("Toppings"),
                        "icon": "emoji_food_beverage",
                        "link": reverse_lazy("admin:product_topping_changelist"),
                    },
                    {
                        "title": _("Categories"),
                        "icon": "category",
                        "link": reverse_lazy("admin:product_category_changelist"),
                    },
                    {
                        "title": _("Sizes"),
                        "icon": "straighten",
                        "link": reverse_lazy("admin:product_size_changelist"),
                    },
                    {
                        "title": _("Tags"),
                        "icon": "tag",
                        "link": reverse_lazy("admin:product_tag_changelist"),
                    },
                    {
                        "title": _("Статьи"),
                        "icon": "article",
                        "link": reverse_lazy("admin:product_article_changelist"),
                    },
                ],
            },
            {
                "title": _("Pages"),
                "icon": "description",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Main Page"),
                        "icon": "insert_drive_file",
                        "link": reverse_lazy("admin:pages_mainpage_changelist"),
                    },
                    {
                        "title": _("Static Pages"),
                        "icon": "note_alt",
                        "link": reverse_lazy("admin:pages_staticpage_changelist"),
                    },
                    {
                        "title": _("Banners"),
                        "icon": "view_carousel",
                        "link": reverse_lazy("admin:pages_banner_changelist"),
                    },
                    {
                        "title": _("Stories"),
                        "link": reverse_lazy("admin:pages_stories_changelist"),
                    },
                    {
                        "title": _("Contacts"),
                        "icon": "contact_phone",
                        "link": reverse_lazy("admin:pages_contacts_changelist"),
                    },
                ],
            },
            {
                "title": _("Settings"),
                "icon": "settings",
                "collapsible": True,
                "items": [
                    {
                        "title": _("Telegram"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:orders_telegrambottoken_changelist"),
                    },
                    {
                        "title": _("WhatsApp"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:orders_whatsappchat_changelist"),
                    },
                    {
                        "title": _("Cashback"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:orders_percentcashback_changelist"),
                    },
                    {
                        "title": _("Distance Pricing"),
                        "icon": "settings",
                        "link": reverse_lazy("admin:orders_distancepricing_changelist"),
                    },
                ],
            },
        ],
    },
    # "TABS": [
    #     {
    #         "models": [
    #             "app_label.model_name_in_lowercase",
    #         ],
    #         "items": [
    #             {
    #                 "title": _("Your custom title"),
    #                 "link": reverse_lazy("admin:app_label_model_name_changelist"),
    #                 "permission": "sample_app.permission_callback",
    #             },
    #         ],
    #     },
    # ],
}
