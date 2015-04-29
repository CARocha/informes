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

    list_display = ['fecha','usuario']

    #def person_name(self, obj):
    #    for presu in obj.presupuesto_set.all():

    #    return obj.presupuesto_set.porcentaje

    #person_name.short_description = ("porcentajes")
    
    #def get_inline_instances(self, request, obj=None):
    #    for inline in self.inlines:
    #        print inline(self.model, self.admin_site)
    #    return [inline(self.model, self.admin_site) for inline in self.inlines]

    #def save_formset(self, request, form, formset, change):
    #    instances = formset.save(commit=False)
        
    #    for instance in instances:
    #        instance.save()
    #    formset.save_m2m()
    
    #def save_related(self, request, form, formsets, change):
    #    print formsets
        # now we have what we need here... :)
    #    return formsets

    #def save_model(self, request, obj, form, change):
        #print dir(obj)
        # do something with obj.related_set.all()
        # OPS! it's empty!

# Register your models here.
admin.site.register(Organismos)
admin.site.register(Tablero, TableroAdmin)