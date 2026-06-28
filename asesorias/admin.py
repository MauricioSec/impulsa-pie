from django.contrib import admin
from .models import Servicio, Usuario, Reserva, Pago, Recurso

# Registramos los modelos para que sean visibles en el panel de control
admin.site.register(Servicio)
admin.site.register(Usuario)
admin.site.register(Reserva)
admin.site.register(Pago)
admin.site.register(Recurso)