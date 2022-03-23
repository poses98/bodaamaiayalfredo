from django import forms

from .models import Confirmacion


class ConfirmacionForm(forms.ModelForm):

    class Meta:
        model = Confirmacion
        fields = ('asistiras', 'name', 'surname', 'acompanantes', 'nombres_acompanantes',
                  'bus_ida', 'bus_vuelta', 'nombre_cancion', 'nombre_grupo', 'food_restrictions', 'food_restrictions_especificaciones')


class WebPasswordForm(forms.Form):
    password = forms.CharField()
