from quick_docs_drf.field_types import _field_types
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string
from quick_docs_drf.settings import DEFAULT


class QuickDocsViewsets:
    """
    Generate Quick Docs Menu Context
    """

    def __init__(self) -> None:
        self.context: list = []

    def get_context_viewsets(self):
        """
        Generate Quick Docs Viewset Context
        """
        # Get Base Router from Default Setting
        viewsets = DEFAULT.get("VIEWSET_LISTS")
        if viewsets is None:
            raise ImproperlyConfigured("VIEWSET_LISTS not found in settings.py")

        for viewset in viewsets:
            viewset = import_string(viewset)
            self.context.append(
                {
                    "name": viewset.__name__,
                    "docs": viewset.__doc__,
                    "serializer_class": viewset.serializer_class.__name__,
                    "fields": viewset.serializer_class.Meta.fields,
                    "permission_classes": [
                        permission.__name__ for permission in viewset.permission_classes
                    ],
                    "pagination_class": (
                        viewset.pagination_class.__name__
                        if viewset.pagination_class
                        else None
                    ),
                    "authentication_classes": [
                        authentication.__name__
                        for authentication in viewset.authentication_classes
                    ],
                    "lookup_field": viewset.lookup_field,
                    "throttle_classes": [
                        throttle.__name__ for throttle in viewset.throttle_classes
                    ],
                    "renderer_classes": [
                        renderer.__name__ for renderer in viewset.renderer_classes
                    ],
                }
            )
        return self.context
