from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Inyectamos las rutas nativas de login/logout de Django
    path('cuentas/', include('django.contrib.auth.urls')), 
    path('', include('asesorias.urls')), 
]