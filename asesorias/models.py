from django.db import models
from django.contrib.auth.models import User

class Servicio(models.Model):
    MODALIDAD_CHOICES = [
        ('online', 'Online'),
        ('presencial', 'Presencial'),
        ('hibrido', 'Híbrido'),
    ]
    titulo = models.CharField(max_length=200)
    descripcion = models.TextField(blank=True, null=True)
    modalidad = models.CharField(max_length=20, choices=MODALIDAD_CHOICES, default='online')
    estado = models.BooleanField(default=True)

    def __str__(self):
        return self.titulo

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='perfil_pie')
    
    ROL_CHOICES = [
        ('admin', 'Administrador'),
        ('coordinador_pie', 'Coordinador PIE'),
        ('docente', 'Docente'),
        ('directivo', 'Directivo'),
        ('apoderado', 'Apoderado'),
        ('estudiante', 'Estudiante de Ed. Diferencial'),
    ]
    rol = models.CharField(max_length=20, choices=ROL_CHOICES)
    telefono = models.CharField(max_length=20, blank=True, null=True)
    institucion_educativa = models.CharField(max_length=200)
    
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.user.get_full_name()} - {self.institucion_educativa}"

class Reserva(models.Model):
    ESTADO_CHOICES = [
        ('pendiente', 'Pendiente'),
        ('confirmada', 'Confirmada'),
        ('realizada', 'Realizada'),
        ('cancelada', 'Cancelada'),
    ]
    usuario = models.ForeignKey(Usuario, on_delete=models.RESTRICT, related_name='reservas')
    servicio = models.ForeignKey(Servicio, on_delete=models.RESTRICT, related_name='reservas')
    
    fecha_hora = models.DateTimeField()
    estado = models.CharField(max_length=20, choices=ESTADO_CHOICES, default='pendiente')
    notas_cliente = models.TextField(blank=True, null=True)
    
    creado_en = models.DateTimeField(auto_now_add=True)
    actualizado_en = models.DateTimeField(auto_now=True)

    def __str__(self):
        # CORRECCIÓN DE CÓDIGO: Extraemos el nombre desde el modelo User nativo
        return f"Reserva: {self.servicio.titulo} para {self.usuario.user.get_full_name()}"

class Pago(models.Model):
    METODO_CHOICES = [
        ('transferencia', 'Transferencia Bancaria'),
        ('webpay', 'Webpay / Tarjeta'),
        ('efectivo', 'Efectivo'),
    ]
    ESTADO_PAGO_CHOICES = [
        ('completado', 'Completado'),
        ('rechazado', 'Rechazado'),
        ('reembolsado', 'Reembolsado'),
    ]
    reserva = models.ForeignKey(Reserva, on_delete=models.CASCADE, related_name='pagos')
    monto = models.DecimalField(max_digits=10, decimal_places=0) 
    fecha_pago = models.DateTimeField(auto_now_add=True)
    metodo_pago = models.CharField(max_length=20, choices=METODO_CHOICES)
    estado_pago = models.CharField(max_length=20, choices=ESTADO_PAGO_CHOICES, default='completado')
    id_transaccion_externo = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return f"Pago - ${self.monto} ({self.estado_pago})"

class Recurso(models.Model):
    TIPO_CHOICES = [
        ('pdf', 'PDF'),
        ('word', 'Word'),
        ('excel', 'Excel'),
        ('video', 'Video'),
    ]
    titulo = models.CharField(max_length=200)
    tipo_documento = models.CharField(max_length=10, choices=TIPO_CHOICES)
    archivo = models.FileField(upload_to='recursos/')
    es_publico = models.BooleanField(default=False)
    subido_en = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo