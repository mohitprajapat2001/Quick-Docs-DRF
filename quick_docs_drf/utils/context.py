"""Generate Documentation Page Context Data"""

from enum import Enum
from quick_docs_drf.settings import DEFAULT as DRF_SETTINGS
from quick_docs_drf.utils import utils


def generate_documentation_page_context_data(self):
    """Generate Documentation Page Context Data"""
    return {
        "template_style": utils.get_template_styling(),
    }
