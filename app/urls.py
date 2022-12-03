from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view

schema_view = get_schema_view(
    info=openapi.Info(title="Tournament Table API", default_version="1.0.0"),
    public=True,
)

urlpatterns = [
    path("api/", schema_view.with_ui("swagger", cache_timeout=0), name="swagger-ui"),
]

urlpatterns += [
    # URL'ы приложения
]
