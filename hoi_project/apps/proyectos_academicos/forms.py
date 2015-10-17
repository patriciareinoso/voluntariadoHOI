# -*- coding: utf-8 -*-
from django import forms


class MonthlyForm(forms.Form):
    OPCIONES_MES = (
        ("01", "Enero"),
        ("02", "Febrero"),
        ("03", "Marzo"),
        ("04", "Abril"),
        ("05", "Mayo"),
        ("06", "Junio"),
        ("07", "Julio"),
        ("08", "Agosto"),
        ("09", "Septiembre"),
        ("10", "Octubre"),
        ("11", "Noviembre"),
        ("12", "Diciembre")
    )

    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    mes = forms.ChoiceField(label="Mes", required=True, choices=OPCIONES_MES)
    ano = forms.IntegerField(label="Año", required=True, min_value=1)


class AnualForm(forms.Form):

    _selected_action = forms.CharField(widget=forms.MultipleHiddenInput)
    ano = forms.IntegerField(label="Año", required=True, min_value=1)
