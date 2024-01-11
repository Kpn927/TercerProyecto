from django import forms

class CafeFormulario(forms.Form):
    nombre = forms.CharField()
    
class RegisFormulario(forms.Form):
    Usuario = forms.CharField(max_length= 25)
    Password = forms.CharField(max_length= 25)
    
class deliverFormulario(forms.Form):
    ubicacion = forms.CharField(max_length=25)
    telefono = forms.IntegerField()
    Nombre = forms.CharField(max_length=25)
    Correo = forms.CharField(max_length=25)