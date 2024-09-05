from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from accounts.views import *

urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path("", note_all),
    path("note_edit/<int:id>/", note_edit),
    path("", include("pages.urls")),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns = [
        path("__debug__/", include(debug_toolbar.urls)),
    ] + urlpatterns
