# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Admon',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField()),
                ('total', models.FloatField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Proyecto en admon',
                'verbose_name_plural': 'Proyectos en admon',
            },
        ),
        migrations.CreateModel(
            name='Disponibilidades',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('disponible', models.CharField(max_length=250)),
                ('monto', models.FloatField()),
            ],
            options={
                'verbose_name': 'Disponibilidad en la cuenta de efectivo',
                'verbose_name_plural': 'Disponibilidad en la cuenta de efectivo',
            },
        ),
        migrations.CreateModel(
            name='GastoFuncionamiento',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('aporte', models.CharField(max_length=250)),
                ('monto', models.FloatField()),
                ('total', models.FloatField(null=True, editable=False, blank=True)),
                ('porcentaje', models.FloatField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Gasto de funcionamiento de SIMAS',
                'verbose_name_plural': 'Gasto de funcionamiento de SIMAS',
            },
        ),
        migrations.CreateModel(
            name='GastoIngreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingreso', models.FloatField()),
                ('gasto', models.FloatField()),
            ],
            options={
                'verbose_name': 'Gasto vs ingreso',
                'verbose_name_plural': 'Gasto vs ingreso',
            },
        ),
        migrations.CreateModel(
            name='Gastos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('mes', models.IntegerField(choices=[(1, 'Enero'), (2, 'Febrero'), (3, 'Marzo'), (4, 'Abril'), (5, 'Mayo'), (6, 'Junio'), (7, 'Julio'), (8, 'Agosto'), (9, 'Septiembre'), (10, 'Octubre'), (11, 'Noviembre'), (12, 'Diciembre')])),
                ('monto', models.FloatField()),
                ('total', models.FloatField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Gasto mensual',
                'verbose_name_plural': 'Gastos mensuales',
            },
        ),
        migrations.CreateModel(
            name='Ingreso',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('ingreso', models.FloatField()),
                ('total', models.FloatField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Ingreso por tipo de donante/proyecto',
                'verbose_name_plural': 'Ingreso por tipo de donante/proyecto',
            },
        ),
        migrations.CreateModel(
            name='Organismos',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=250)),
            ],
            options={
                'verbose_name': 'Organismo',
                'verbose_name_plural': 'Organismos',
            },
        ),
        migrations.CreateModel(
            name='Presupuesto',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('presupuesto_aprobado', models.FloatField()),
                ('ingreso_acumulado', models.FloatField()),
                ('porcentaje', models.FloatField(null=True, editable=False, blank=True)),
            ],
            options={
                'verbose_name': 'Presupuesto vs ingreso',
                'verbose_name_plural': 'Presupuestos vs ingresos',
            },
        ),
        migrations.CreateModel(
            name='Servicios',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('monto', models.FloatField()),
                ('total', models.FloatField(null=True, editable=False, blank=True)),
                ('organizacion', models.ForeignKey(to='informesimas.Organismos')),
            ],
            options={
                'verbose_name': 'Servicios de consultorias',
                'verbose_name_plural': 'Servicios de consultorias',
            },
        ),
        migrations.CreateModel(
            name='Tablero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('fecha', models.DateField()),
                ('usuario', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='servicios',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='presupuesto',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='donante',
            field=models.ForeignKey(to='informesimas.Organismos'),
        ),
        migrations.AddField(
            model_name='ingreso',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='gastos',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='gastoingreso',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='gastofuncionamiento',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='disponibilidades',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
        migrations.AddField(
            model_name='admon',
            name='organismo',
            field=models.ForeignKey(to='informesimas.Organismos'),
        ),
        migrations.AddField(
            model_name='admon',
            name='tablero',
            field=models.ForeignKey(to='informesimas.Tablero'),
        ),
    ]
