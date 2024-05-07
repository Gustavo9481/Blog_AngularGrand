from django.contrib import admin
from .models import Post, Contacto, Comentario

# ............................. App Core | admin ............................. 󰌠
# tablas registradas en el panel administrativo



# ---------------------------------------------------- tabla panel | PostAdmin 󰌠
class PostAdmin(admin.ModelAdmin):
    '''
    Tabla Posts: artículos del Blog
    '''

    list_display = ("etiqueta", "titulo", "autor", "fecha")               # 🠶 01
    search_fields = ("etiqueta", "autor", "fecha",)
    readonly_fields = ('fecha',)



# ------------------------------------------------ tabla panel | ContactoAdmin 󰌠
class ContactoAdmin(admin.ModelAdmin):
    '''
    Tabla Contacto: mensajes al administrador o autor del Blog
    '''

    list_display = ("nombre", "email", "asunto", "fecha")
    search_fields = ("nombre", "email", "fecha",)
    readonly_fields = ("fecha",)



# ---------------------------------------------- tabla panel | ComentarioAdmin 󰌠
class ComentarioAdmin(admin.ModelAdmin):
    '''
    Tabla Comentario: mensajes u opiniones de los lectores en los artículos
    '''

    list_display = ("nombre", "email", "comentario", "art_relacionado", "fecha")
    search_fields = ("nombre", "email", "art_relacionado", "fecha",)
    readonly_fields = ("fecha",)



admin.site.register(Post, PostAdmin)
admin.site.register(Contacto, ContactoAdmin)
admin.site.register(Comentario, ComentarioAdmin)
