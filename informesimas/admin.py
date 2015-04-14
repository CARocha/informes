from django.contrib import admin
from .models import *

class PresupuestoInline(admin.TabularInline):
	model = Presupuesto
	extra = 1
	max_num = 1

class IngresoInline(admin.TabularInline):
	model = Ingreso
	extra = 1

class ServiciosInline(admin.TabularInline):
	model = Servicios
	extra = 1

class AdmonInline(admin.TabularInline):
	model = Admon
	extra = 1

class GastosInline(admin.TabularInline):
	model = Gastos
	extra = 1
	max_num = 12

class GastoFuncionamientoInline(admin.TabularInline):
	model = GastoFuncionamiento
	extra = 1

class GastoIngresoInline(admin.TabularInline):
	model = GastoIngreso
	extra = 1
	max_num = 1

class DisponibilidadesInline(admin.TabularInline):
	model = Disponibilidades
	extra = 1

class TableroAdmin(admin.ModelAdmin):
	inlines = [PresupuestoInline,IngresoInline,ServiciosInline,
				AdmonInline,GastosInline,GastoFuncionamientoInline,
				GastoIngresoInline,DisponibilidadesInline,]

# Register your models here.
admin.site.register(Organismos)
admin.site.register(Tablero, TableroAdmin)