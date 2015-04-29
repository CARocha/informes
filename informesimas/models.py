# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.utils.encoding import python_2_unicode_compatible
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
@python_2_unicode_compatible
class Organismos(models.Model):
	nombre = models.CharField(max_length=250)

	def __str__(self):
		return self.nombre

	class Meta:
		verbose_name='Organismo'
		verbose_name_plural='Organismos'

@python_2_unicode_compatible
class Tablero(models.Model):
	fecha = models.DateField()
	usuario = models.ForeignKey(User)

	def __str__(self):
		return u'%s' % (str(self.fecha))

class Presupuesto(models.Model):
	tablero = models.ForeignKey(Tablero)
	presupuesto_aprobado = models.FloatField()
	ingreso_acumulado = models.FloatField()

	porcentaje = models.FloatField(editable=False, null=True, blank=True)

	def save(self, *args, **kwargs):
		
		self.porcentaje = (self.ingreso_acumulado / self.presupuesto_aprobado) * 100
		 
		super(Presupuesto, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Presupuesto vs ingreso'
		verbose_name_plural = 'Presupuestos vs ingresos'


class Ingreso(models.Model):
	tablero = models.ForeignKey(Tablero)
	donante = models.ForeignKey(Organismos)
	ingreso = models.FloatField()

	total = models.FloatField(editable=False, null=True, blank=True)

	# def save(self, *args, **kwargs):
		
	# 	self.total += self.ingreso
		
	# 	super(Ingreso, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Ingreso por tipo de donante/proyecto'
		verbose_name_plural = 'Ingreso por tipo de donante/proyecto'

class Servicios(models.Model):
	tablero = models.ForeignKey(Tablero)
	organizacion = models.ForeignKey(Organismos)
	monto = models.FloatField()

	total = models.FloatField(editable=False, null=True, blank=True)

	class Meta:
		verbose_name = 'Servicios de consultorias'
		verbose_name_plural = 'Servicios de consultorias'

class Admon(models.Model):
	tablero = models.ForeignKey(Tablero)
	organismo = models.ForeignKey(Organismos)
	monto = models.FloatField()

	total = models.FloatField(editable=False, null=True, blank=True)

	class Meta:
		verbose_name = 'Proyecto en admon'
		verbose_name_plural = 'Proyectos en admon'

CHOICE_MESES = (
					(1,'Enero'),
					(2,'Febrero'),
					(3,'Marzo'),
					(4,'Abril'),
					(5,'Mayo'),
					(6,'Junio'),
					(7,'Julio'),
					(8,'Agosto'),
					(9,'Septiembre'),
					(10,'Octubre'),
					(11,'Noviembre'),
					(12,'Diciembre'),
				)

class Gastos(models.Model):
	tablero = models.ForeignKey(Tablero)
	mes = models.IntegerField(choices=CHOICE_MESES)
	monto = models.FloatField()

	total = models.FloatField(editable=False, null=True, blank=True)

	class Meta:
		verbose_name = 'Gasto mensual'
		verbose_name_plural = 'Gastos mensuales'


class GastoFuncionamiento(models.Model):
	tablero = models.ForeignKey(Tablero)
	aporte = models.CharField(max_length=250)
	monto = models.FloatField()

	total = models.FloatField(editable=False, null=True, blank=True)
	porcentaje = models.FloatField(editable=False, null=True, blank=True)

	class Meta:
		verbose_name = 'Gasto de funcionamiento de SIMAS'
		verbose_name_plural = 'Gasto de funcionamiento de SIMAS'

class GastoIngreso(models.Model):
	tablero = models.ForeignKey(Tablero)
	ingreso = models.FloatField()
	gasto = models.FloatField()

	class Meta:
		verbose_name = 'Gasto vs ingreso'
		verbose_name_plural = 'Gasto vs ingreso'

class Disponibilidades(models.Model):
	tablero = models.ForeignKey(Tablero)
	disponible = models.CharField(max_length=250)
	monto = models.FloatField()

	class Meta:
		verbose_name = 'Disponibilidad en la cuenta de efectivo'
		verbose_name_plural = 'Disponibilidad en la cuenta de efectivo'