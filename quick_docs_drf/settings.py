"""Default Settings for Quick Docs DRF"""

from django.conf import settings


def quick_docs_drf_configuration(key):
    """
    Get Configuration Settings from Project Settings File else None

    :param key: str
    """
    try:
        configuration = settings.QUICK_DOCS_DRF
        return configuration.get(key, None)
    except AttributeError as err:
        raise AttributeError("QUICK_DOCS_DRF not found in settings.py")


DEFAULT = {
    "PROJECT_NAME": quick_docs_drf_configuration("PROJECT_NAME"),
    "PROJECT_DESCRIPTION": quick_docs_drf_configuration("PROJECT_DESCRIPTION") or None,
    "VERSION": quick_docs_drf_configuration("VERSION") or 1.0,
    "AUTHOR": quick_docs_drf_configuration("AUTHOR") or None,
    "AUTHOR_EMAIL": quick_docs_drf_configuration("AUTHOR_EMAIL") or None,
    "LICENSE": quick_docs_drf_configuration("LICENSE") or "MIT",
    "API_URL": quick_docs_drf_configuration("API_URL") or "/api/",
    "API_VERSION": quick_docs_drf_configuration("API_VERSION") or "v1",
    "API_PREFIX": quick_docs_drf_configuration("API_PREFIX") or "api",
    "BASE_URL": quick_docs_drf_configuration("BASE_URL") or None,
    "BASE_ROUTER_NAME": quick_docs_drf_configuration("BASE_ROUTER_NAME") or "router",
    "NESTED_ROUTER_NAME": quick_docs_drf_configuration("NESTED_ROUTER_NAME") or None,
    "CONTRIBUTION": True,
    "TEMPLATE_STYLE": quick_docs_drf_configuration("TEMPLATE_STYLE") or "bootstrap5",
    "CONTACT_SECTION": False,
    "SOCIAL_SECTION": False,
    "CONTACT": {
        "name": quick_docs_drf_configuration("CONTACT_NAME") or None,
        "email": quick_docs_drf_configuration("CONTACT_EMAIL") or None,
        "url": quick_docs_drf_configuration("CONTACT_URL") or None,
    },
    "SOCIAL": {
        "github": quick_docs_drf_configuration("SOCIAL_GITHUB") or None,
        "twitter": quick_docs_drf_configuration("SOCIAL_TWITTER") or None,
        "linkedin": quick_docs_drf_configuration("SOCIAL_LINKEDIN") or None,
        "facebook": quick_docs_drf_configuration("SOCIAL_FACEBOOK") or None,
        "instagram": quick_docs_drf_configuration("SOCIAL_INSTAGRAM") or None,
        "youtube": quick_docs_drf_configuration("SOCIAL_YOUTUBE") or None,
        "medium": quick_docs_drf_configuration("SOCIAL_MEDIUM") or None,
    },
}
