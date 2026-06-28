from django.urls import path
from . import views

urlpatterns = [
    path('', views.inicio, name='inicio'), 
    path('servicio/<int:servicio_id>/', views.detalle_servicio, name='detalle_servicio'),
    path('servicio/<int:servicio_id>/agendar/', views.agendar_reserva, name='agendar_reserva'),
    # NUEVA RUTA
    path('registro/', views.registro, name='registro'),
]