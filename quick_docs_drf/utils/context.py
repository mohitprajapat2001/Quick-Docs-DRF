"""Generate Documentation Page Context Data"""

from quick_docs_drf.utils import utils
from quick_docs_drf.utils.context_menu import get_contexts


def generate_documentation_page_context_data(self):
    """Generate Documentation Page Context Data"""
    menu_context, viewset_context = get_contexts()
    return {
        "template_style": utils.get_template_styling(),
        "project_name": utils.get_project_name(),
        "project_description": utils.get_project_description(),
        "project_version": utils.get_project_version(),
        "project_author": utils.get_project_author(),
        "project_author_email": utils.get_project_author_email(),
        "project_license": utils.get_project_license(),
        "api_url": utils.get_api_url(),
        "api_version": utils.get_api_version(),
        "api_prefix": utils.get_api_prefix(),
        "base_url": utils.get_base_url(),
        "base_router_name": utils.get_base_router_name(),
        "nested_router_name": utils.get_nested_router_name(),
        "contribution": utils.get_contribution(),
        "contact_section": utils.get_contact_section(),
        "social_section": utils.get_social_section(),
        "contact_details": utils.get_contact_details(),
        "social_details": utils.get_social_details(),
        "api_description": utils.get_api_description(),
        "api_license": utils.get_api_license(),
        "menu_context": menu_context,
        "viewset_context": viewset_context,
    }
