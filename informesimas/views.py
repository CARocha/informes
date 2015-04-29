from django.shortcuts import render
from models import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
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

    form = InformeForm()
    fecha1=request.session['fecha_inicio']
    fecha2=request.session['fecha_final']
    
    presupuesto1 = Presupuesto.objects.filter(tablero__fecha__range=(fecha1,fecha2)).aggregate(
        presupuesto_aprobado=Sum('presupuesto_aprobado'), 
        ingreso_acumulado=Sum('ingreso_acumulado'))

    
    ingresos = Ingreso.objects.filter(tablero__fecha__range=(fecha1,fecha2))
    servicios = Servicios.objects.filter(tablero__fecha__range=(fecha1,fecha2))
    gastos = Gastos.objects.filter(tablero__fecha__range=(fecha1,fecha2))

    return render(request, template, locals())
