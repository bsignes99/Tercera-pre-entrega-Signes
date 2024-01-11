from django import forms

class formularioHeroes(forms.Form):
    nombre = forms.CharField()
    habilidad = forms.CharField()
    raza = forms.CharField()
    vehiculo = forms.CharField()

class formularioVillano(forms.Form):
    nombre = forms.CharField()
    raza = forms.CharField()
    vehiculo = forms.CharField()

class formularioVehiculo(forms.Form):
    modelo= forms.CharField(max_length= 40)
    propietario = forms.CharField(max_length= 40)