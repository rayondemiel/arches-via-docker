from django.urls import include, re_path
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", include("arches.urls")),
    path("", include("arches_for_science.urls")),
    path("reports/", include("arches_templating.urls")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
