from django.shortcuts import render
from models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum, Avg
from forms import *

# Create your views here.
@login_required(login_url='/accounts/login/')
def consultar(request):
    if request.method=='POST':
        mensaje = None
        form = InformeForm(request.POST)
        if form.is_valid():
            request.session['fecha_inicio'] = form.cleaned_data['fecha_inicio']
            request.session['fecha_final'] = form.cleaned_data['fecha_final'] 
            mensaje = "Explore los resultos en el menu superior"
            centinela = 1
    else:
        form = InformeForm()
        centinela = 0
        mensaje = "hubo errores" 
    return render(request, "index.html", locals())

@login_required(login_url='/accounts/login/')
def index_view(request, template="datos.html"):

    fecha1=request.session['fecha_inicio']
    fecha2=request.session['fecha_final']
    
    presupuesto1 = Presupuesto.objects.filter(tablero__fecha__range=(fecha1,fecha2)).aggregate(
        presupuesto_aprobado=Sum('presupuesto_aprobado'), 
        ingreso_acumulado=Sum('ingreso_acumulado'))

    
    ingresos = Ingreso.objects.filter(tablero__fecha__range=(fecha1,fecha2))
    ingreso_dicc = {}
    for obj in Organismos.objects.filter(id__in=[1,2,4,5,6,7,8,10,11]):
        acumulado = Ingreso.objects.filter(tablero__fecha__range=(fecha1,fecha2), donante=obj).aggregate(
                                        ingresOrgnanismo=Sum('ingreso'))
        ingreso_dicc[obj] = acumulado

    servicios = Servicios.objects.filter(tablero__fecha__range=(fecha1,fecha2))
    acumulado_servicio = Servicios.objects.filter(tablero__fecha__range=(fecha1,fecha2)).aggregate(
                        total=Sum('monto'), promedio=Avg('monto'))

    gastos = Gastos.objects.filter(tablero__fecha__range=(fecha1,fecha2))
    gasto_acumulado = Gastos.objects.filter(tablero__fecha__range=(fecha1,fecha2)).aggregate(
                        total=Sum('monto'), promedio=Avg('monto'))

    disponibilidad = Disponibilidades.objects.filter(tablero__fecha__range=(fecha1,fecha2))

    return render(request, template, locals())
