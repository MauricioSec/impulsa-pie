from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from django.contrib import messages
from .models import Servicio, Reserva, Usuario
from .forms import RegistroForm

def inicio(request):
    """Renderiza el catálogo dinámico de servicios."""
    servicios_activos = Servicio.objects.filter(estado=True)
    contexto = {
        'servicios_lista': servicios_activos
    }
    return render(request, 'asesorias/inicio.html', contexto)

def detalle_servicio(request, servicio_id):
    """Muestra la información extendida de un servicio específico."""
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    contexto = {'servicio': servicio}
    return render(request, 'asesorias/detalle.html', contexto)

def agendar_reserva(request, servicio_id):
    """Procesa la inserción de una nueva reserva vinculada al perfil activo."""
    if request.method != 'POST' or not request.user.is_authenticated:
        return redirect('inicio')
    
    servicio = get_object_or_404(Servicio, pk=servicio_id)
    notas = request.POST.get('notas_cliente', '')
    
    if hasattr(request.user, 'perfil_pie'):
        Reserva.objects.create(
            usuario=request.user.perfil_pie, 
            servicio=servicio,
            fecha_hora=timezone.now(), 
            estado='pendiente',
            notas_cliente=notas
        )
        messages.success(request, "Su solicitud de asesoría ha sido registrada exitosamente. Nos pondremos en contacto a la brevedad.")
        
    return redirect('inicio')

def registro(request):
    """Maneja el auto-registro de clientes en la plataforma pública."""
    if request.method == 'POST':
        form = RegistroForm(request.POST)
        if form.is_valid():
            # 1. Persistencia del objeto User (Tabla auth_user)
            user = form.save()
            
            # 2. Extracción y normalización de nombres para los campos nativos de Django
            nombre_completo = form.cleaned_data.get('nombre_completo')
            partes = nombre_completo.split(' ', 1)
            user.first_name = partes[0]
            user.last_name = partes[1] if len(partes) > 1 else ''
            user.email = form.cleaned_data.get('email')
            user.save()

            # 3. Creación del perfil satélite (Tabla asesorias_usuario) con la relación Uno a Uno
            Usuario.objects.create(
                user=user,
                rol=form.cleaned_data.get('rol'),
                telefono=form.cleaned_data.get('telefono'),
                institucion_educativa=form.cleaned_data.get('institucion_educativa')
            )
            
            messages.success(request, "Su cuenta ha sido creada exitosamente. Ya puede iniciar sesión.")
            return redirect('login')
    else:
        form = RegistroForm()
        
    return render(request, 'registration/registro.html', {'form': form})