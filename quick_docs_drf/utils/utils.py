"""Utility Function for Quick Docs DRF"""

from quick_docs_drf.settings import DEFAULT


def get_template_styling():
    """Base Documentation Template Styling"""
    return DEFAULT.get("TEMPLATE_STYLE")


def get_project_name():
    """Documentation Project Name"""
    return DEFAULT.get("PROJECT_NAME")


def get_project_description():
    """Documentation Project Description"""
    return DEFAULT.get("PROJECT_DESCRIPTION")


def get_project_version():
    """Documentation Project Version"""
    return DEFAULT.get("VERSION")


def get_project_author():
    """Documentation Project Author"""
    return DEFAULT.get("AUTHOR")


def get_project_author_email():
    """Documentation Project Author Email"""
    return DEFAULT.get("AUTHOR_EMAIL")


def get_project_license():
    """Documentation Project License"""
    return DEFAULT.get("LICENSE")


def get_api_url():
    """Documentation API URL"""
    return DEFAULT.get("API_URL")


def get_api_version():
    """Documentation API Version"""
    return DEFAULT.get("API_VERSION")


def get_api_prefix():
    """Documentation API Prefix"""
    return DEFAULT.get("API_PREFIX")


def get_base_url():
    """Documentation Base URL"""
    return DEFAULT.get("BASE_URL")


def get_base_router_name():
    """Documentation Base Router Name"""
    return DEFAULT.get("BASE_ROUTER_NAME")


def get_nested_router_name():
    """Documentation Nested Router Name"""
    return DEFAULT.get("NESTED_ROUTER_NAME")


def get_contribution():
    """Documentation Contribution Section"""
    return DEFAULT.get("CONTRIBUTION")


def get_contact_section():
    """Documentation Contact Section"""
    return DEFAULT.get("CONTACT_SECTION")


def get_social_section():
    """Documentation Social Section"""
    return DEFAULT.get("SOCIAL_SECTION")


def get_contact_details():
    """Documentation Contact Details"""
    return DEFAULT.get("CONTACT")


def get_social_details():
    """Documentation Social Details"""
    return DEFAULT.get("SOCIAL")


def get_api_description():
    """Documentation API Description"""
    return DEFAULT.get("API_DESCRIPTION")


def get_api_license():
    """Documentation API License"""
    return DEFAULT.get("API_LICENSE")
