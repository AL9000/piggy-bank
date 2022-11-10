from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path

urlpatterns = [
    path("", include("savings.urls")),
]

if settings.DEBUG:
    urlpatterns += [
        path("api-auth/", include("rest_framework.urls")),
    ] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
