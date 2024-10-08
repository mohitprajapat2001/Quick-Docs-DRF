"""Utility Function for Quick Docs DRF"""

from quick_docs_drf.settings import DEFAULT


def get_template_styling():
    """Base Documentation Template Styling"""
    return DEFAULT.get("TEMPLATE_STYLE")
