from django.contrib import admin
from django.urls import path, include
from quick_docs_drf.urls import quick_docs_urls
from rest_framework.routers import DefaultRouter
from quick_docs.views import BlogViewSet, UserViewSet
from drf_spectacular.views import (
    SpectacularAPIView,
    SpectacularRedocView,
    SpectacularSwaggerView,
)

router = DefaultRouter()
router.register("blog", BlogViewSet, basename="blog")
router.register("users", UserViewSet, basename="user")
urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    # Optional UI:
    path(
        "api/schema/swagger-ui/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path(
        "api/schema/redoc/",
        SpectacularRedocView.as_view(url_name="schema"),
        name="redoc",
    ),
] + quick_docs_urls
