from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField

# ............................. App Core | urls .............................. 󰌠



etiquetas = [                                                             # 🠶 01
    ["fotografía", "fotografía"],
    ["budismo", "budismo"]
]



# --------------------------------------------------------------- model | Post 󰌠
class Post(models.Model):
    '''
    Tabla contenedora de Artículos
    '''

    etiqueta = models.CharField(max_length=20, choices=etiquetas)         # 🠶 02
    titulo = models.CharField(max_length=70)
    introduccion = models.TextField(max_length=200, null=True, blank=True)
    contenido = RichTextField()                                           # 🠶 03 
    fecha = models.DateTimeField(auto_now_add=True)
    portada = models.ImageField(
        upload_to='App_Core', null=True, blank=True)                      # 🠶 04
    video = models.URLField(max_length=500, null=True, blank=True)
    podcast = models.URLField(max_length=500, null=True, blank=True)
    autor = models.CharField(max_length=50)

    class Meta:
        verbose_name="Post"
        verbose_name_plural="Posts"



# ---------------------------------------------------------- modelo | Contacto 󰌠
class Contacto(models.Model):
    '''
    Tabla de almacenamiento para formulario de contacto al administrador
    '''

    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    asunto = models.CharField(max_length=200)
    mensaje = models.TextField()
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Contacto"
        verbose_name_plural = "Contactos"



# -------------------------------------------------------- modelo | Comentario 󰌠
class Comentario(models.Model):
    '''
    Tabla de almacenamiento de comentarios de visitantes
    '''

    nombre = models.CharField(max_length=60)
    email = models.EmailField()
    comentario = models.TextField(max_length=300)
    art_relacionado = models.CharField(                                   # 🠶 05
        max_length=70, null=True, blank=True, editable=False)               
    fecha = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "Comentario"
        verbose_name_plural = "Comentarios"
