from django.shortcuts import render
from models import *
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='/accounts/login/')
def index_view(request, template="index.html"):
	
	presupuesto = Presupuesto.objects.all()
	ingresos = Ingreso.objects.all()
	servicios = Servicios.objects.all()
	gastos = Gastos.objects.all()

	return render(request, template, locals())
