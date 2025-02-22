
from django.contrib import admin
from django.urls import path, include
from .views import home  # ✅ Importa la función home

urlpatterns = [
    path('', home, name='home'),  # ✅ Ruta principal de la API
    path('admin/', admin.site.urls),
    path('api/v1/', include('core.urls')),
    path('api/v1/auth/', include('users.urls')),  # Si implementas autenticación
]
