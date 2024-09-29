from django.contrib import admin # type: ignore
from django.urls import path, include  # type: ignore # Importa include para usarlo

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include('myapp.urls')),  # Incluye las URLs de tu aplicación
]
