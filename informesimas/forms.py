 # -*- coding: UTF-8 -*-

from django import forms

#date_inputformats=['%d.%m.%Y','%d/%m/%Y','%Y-%m-%d']

class InformeForm(forms.Form):
    fecha_inicio = forms.DateField()
    fecha_final = forms.DateField()