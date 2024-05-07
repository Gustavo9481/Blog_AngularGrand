from typing import Dict
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ComentarioForm, ContactoForm
from .models import Comentario, Post

# ............................. App Core | views ............................. 󰌠
# consulta de comentarios: Proyecto_Blog/comentarios.md


# --------------------------------------------------------------- vista | home 󰌠
def home(request: HttpRequest) -> HttpResponse:
    '''
    Página principal, renderiza tarjetas de artículos paginados
    de a 3 artículos por página.
    
    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza página principal.
    '''

    posts = Post.objects.all().order_by('-fecha')                         # 🠶 01
    paginador = Paginator(posts, 6)                                       # 🠶 02
    numero_pagina = request.GET.get('page')                               # 🠶 03
    page_obj = paginador.get_page(numero_pagina)                          # 🠶 04
 
    return render(request, 'App_Core/home.html', {"page_obj": page_obj})



# ------------------------------------------------------ vista | articulos_all 󰌠
def articulos_all(request: HttpRequest) -> HttpResponse:
    '''
    Página de artículos, renderiza tarjetas con todos los articulos publicados
    paginados de a 9 por cada página.

    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza las tarjetas de los artículos
    con la paginación correspondiente.
    '''

    posts = Post.objects.all().order_by('-fecha')                         # 🠶 01
    paginador = Paginator(posts, 9)                                       # 🠶 02
    numero_pagina = request.GET.get('page')                               # 🠶 03
    page_obj = paginador.get_page(numero_pagina)                          # 🠶 04

    return render(request, 'App_Core/articulos_all.html', {"page_obj": page_obj})



# ----------------------------------------------------------- vista | contacto 󰌠
def contacto(request: HttpRequest) -> HttpResponse:
    '''
    Página de Formulario de contacto al administrador.

    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza el formulario de contacto 
    con el administrador.
    '''

    data: Dict = {"form": ContactoForm()}                                         
    if request.method == "POST":                                          # 🠶 05
        formulario = ContactoForm(data = request.POST)
        if formulario.is_valid():
            formulario.save()
            data["mensaje"] = "Su mensaje ha sido enviado!"
        else:
            data["form"] = formulario

    return render(request, 'App_Core/contacto.html', data)



# ----------------------------------------------------------- vista | sobre_mi 󰌠
def sobre_mi(request: HttpRequest) -> HttpResponse:
    '''
    Página Sobre Mí - Breve reseña del perfil Profesional AngularGrand.

    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza la información sobre 
    el perfil profesional del Administrador.
    '''
    
    return render(request, 'App_Core/sobre_mi.html')



# ---------------------------------------------------------- vista | mis_fotos 󰌠
def mis_fotos(request: HttpRequest) -> HttpResponse:
    '''
    Página Mis Fotos - Galería de fotos, muestra del trabajo del admin.

    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza la galería de fotos.
    '''
    
    return render(request, 'App_Core/mis_fotos.html')



# ----------------------------------------------------------- vista | artículo 󰌠
def articulo(request: HttpRequest, titulo: str) -> HttpResponse:
    '''
    Vista de artículo individual y comentarios relacionados.
    Video y podcast relacionados al tema

    Parameters:
    request (HttpRequest): solicitud HTTP recibida
    titulo (string): titulo de post seleccionado de tarjeta o menú lateral

    Returns:
    HttpResponse: respuesta HTTP que renderiza la información del artículo.
    '''

    posts_list = Post.objects.all().order_by('-fecha')                    # 🠶 01
    post_art = Post.objects.get(titulo = titulo)                          # 🠶 06
    comentarios = Comentario.objects.filter(art_relacionado = titulo)     # 🠶 07
    
    data: Dict = {
        "post": post_art, 
        "form": ComentarioForm(), 
        "comentarios": comentarios, 
        "posts_list": posts_list
    }

    if request.method == "POST":                                          # 🠶 05
        formulario = ComentarioForm(data = request.POST)
        if formulario.is_valid():
            formulario.instance.art_relacionado = post_art.titulo         # 🠶 08
            formulario.save()
            data["mensaje"] = "Su comentario ha sido enviado!"
        else:
            data["form"] = formulario

    return render(request, 'App_Core/articulo.html', data)


# help(home)                                                              # 🠶 09
