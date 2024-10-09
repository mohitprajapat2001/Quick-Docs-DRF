# Create Context Menu Data
from quick_docs_drf.settings import DEFAULT
from django.core.exceptions import ImproperlyConfigured
from django.utils.module_loading import import_string

APP_NAME = set()
MENU_CONTEXT = []
VIEWSETS_CONTEXT = None


def context_menu():
    """generate context menu data"""
    base_router = DEFAULT.get("BASE_ROUTER_NAME")
    if base_router is None:
        raise ImproperlyConfigured("BASE_ROUTER_NAME not found in settings.py")
    base_router = import_string(base_router)
    for url in base_router.urls:
        try:
            if url.name not in APP_NAME:
                APP_NAME.add(url.name)
                print(url.name)
                MENU_CONTEXT.append(
                    {
                        "model": url.callback.cls.queryset.model.__name__,
                        "app_name": url.name,
                        "app_actions": [
                            action for action in url.callback.actions.values()
                        ],
                    }
                )
        except AttributeError:
            MENU_CONTEXT.append(
                {
                    "name": url.callback.view_class.__name__,
                    "app_name": url.name,
                    "docs": url.callback.view_class.__doc__,
                }
            )


def viewset_context():
    """generate viewset context data"""
    global VIEWSETS_CONTEXT
    VIEWSETS_CONTEXT = []

    viewsets = DEFAULT.get("VIEWSET_LISTS")
    if viewsets is None:
        raise ImproperlyConfigured("VIEWSET_LISTS not found in settings.py")
    for viewset in viewsets:
        viewset = import_string(viewset)
        VIEWSETS_CONTEXT.append(
            {
                "name": viewset.queryset.model.__name__,
                "serializer_class": viewset.serializer_class.__name__,
                "fields": viewset.serializer_class.Meta.fields,
                "permission_classes": [
                    permission.__name__ for permission in viewset.permission_classes
                ],
                "pagination_class": viewset.pagination_class.__name__,
                "authentication_classes": [
                    authentication.__name__
                    for authentication in viewset.authentication_classes
                ],
                "lookup_field": viewset.lookup_field,
                "throttle_classes": viewset.throttle_classes,
                "renderer_classes": [
                    renderer.__name__ for renderer in viewset.renderer_classes
                ],
            }
        )


def get_contexts():
    """get menu and viewset"""
    context_menu()
    viewset_context()
    return MENU_CONTEXT, VIEWSETS_CONTEXT
