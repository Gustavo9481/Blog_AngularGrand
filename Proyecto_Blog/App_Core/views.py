from typing import Dict
from django.core.paginator import Paginator
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
from .forms import ComentarioForm, ContactoForm
from .services import Post_Service, Comentario_Service  
from django.contrib.auth.decorators import login_required

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

    posts = Post_Service.post_order_by_date() 
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

    posts = Post_Service.post_order_by_date()
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
    
    posts_list = Post_Service.post_order_by_date()
    post_art = Post_Service.post_filter_by_title(titulo)
    comentarios = Comentario_Service.comment_filter_by_art_title(titulo)
    
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



# ---------------------------------------------------------------- vista | admin
@login_required
def administrador(request: HttpRequest) -> HttpResponse:
    '''
    Acceso al Panel Administrativo, credenciales necesarias.

    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza el Panel Administrativo Django.
    '''
    
    return redirect("/admin/")

# help(home)                                                              # 🠶 09
