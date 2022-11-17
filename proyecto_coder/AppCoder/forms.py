from django import forms


class EventoFormulario(forms.Form):

    nombre= forms.CharField(max_length=30)
    integrantes= forms.IntegerField()
    tema= forms.CharField(max_length=30)
    fechaini=forms.DateField()
    fechafin=forms.DateField()

class PaginaFormulario(forms.Form):  

    nombre= forms.CharField(max_length=30)
    tema= forms.CharField(max_length=30)
    integrantes= forms.IntegerField()

class SeguidorFormulario(forms.Form):  

    nombre= forms.CharField(max_length=30)
    apellido= forms.CharField(max_length=30)
    email= forms.EmailField()