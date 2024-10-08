from django.views.generic import TemplateView
from typing import Any
from django.conf import settings
from django.utils.module_loading import import_string


class DocumentationView(TemplateView):
    template_name = "documentation.html"

    def get_context_data(self, **kwargs) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        router = import_string("quick_docs.urls.router")
        for _ in router.urls:
            # print(_.__dict__["pattern"])
            print(_.__dict__["callback"].__dict__.get("cls").__dict__)
        return context


documentation_view = DocumentationView.as_view()
