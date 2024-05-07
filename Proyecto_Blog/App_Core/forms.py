from django import forms
from .models import Contacto, Comentario

# ........................... modelo | Comentario ............................ 󰌠



# -------------------------------------------------------- form | ContactoFrom 󰌠
class ContactoForm(forms.ModelForm):
    '''
    Definición de campos para formulario Contacto en el panel Admin
    '''

    class Meta:
        model = Contacto
        fields = "__all__"



# ------------------------------------------------------ form | ComentarioForm 󰌠
class ComentarioForm(forms.ModelForm):
    '''
    Definición de campos para formulario Comentario en el panel Admin.
    '''

    class Meta:
        model = Comentario
        fields = "__all__"
