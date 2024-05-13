# Documentación 
[volver a home](../README.md)

La aplicación es un Blog básico donde el Autor(propietario) puede cargar artículos(post), 
gestionarlos(crud) y recibir visitas. También puede mostrar un perfil prefesional y fotpgrafías
de su portafolio.

<br>
<div style="text-align:center">
<img src="./doc-img/diagrama.png" alt="diagrama Agular Grand" width="400"/>
</div>
<br>

## Instalación
Al ser un proyecto en el framework Python Django, se recomienda trabajar dentro de un entorno virtual
```
pyrhon -m virtualenv <entorno>
source <entorno>/bin/activate     # linux - macOS
<entorno>\Scripts\activate        # Windows
```
Instalar las dependencias necesarias desde el archivo requirements.tex 
```
pip install -r requirements.txt

```
Esta instrucción debe instalar los siguientes requerimientos
<table>
  <tr>
    <th>módulo</th>
    <th>versión</th>
  </tr>
  <tr>
    <td>Django</td>
    <td>5.0.2</td>
  </tr>
  <tr>
    <td>django-admin-interface</td>
    <td>0.28.6</td>
  </tr>
  <tr>
    <td>django-colorfield</td>
    <td>0.11.0</td>
  </tr>
  <tr>
    <td>ngrok</td>
    <td>1.2.0</td>
  </tr>
  <tr>
    <td>pillow</td>
    <td>10.2.0</td>
  </tr>
  <tr>
    <td>python-dotenv</td>
    <td>1.0.1</td>
  </tr>
  <tr>
    <td>python-slugify</td>
    <td>8.0.4</td>
  </tr>
  <tr>
    <td>sqlparse</td>
    <td>0.4.4</td>
  </tr>
  <tr>
    <td>text-unidecode</td>
    <td>1.3</td>
  </tr>
</table>

## Modelos y Vistas
El proyecto alberga 3 modelos -> `models.py`
> Post: Tabla contenedora de Artículos
    Acá se almacenan los artículos creados por el Administrador.
    Imagen de portada, video o podcats.
    Etiqueta a la cual pertece el artículo, fecha y autor.

> Contacto: Tabla de almacenamiento para formulario de contacto al administrador.
    Contiene los datos principales del visitante que contacta al Administrador.

> Comentario: Tabla de almacenamiento de comentarios de visitantes
    Alberga los comentarios de los visitantes que muestran sus impresiones
    acerca de los artículos contenidos en el Blog.


Cuenta con 5 vistas las cuales renderizan una plantilla html usando Jinja, a partir de una base.
```
def home(request: HttpRequest) -> HttpResponse:
    '''
    Página principal, renderiza tarjetas de artículos paginados
    de a 3 artículos por página.
    
    Parameters:
    request (HttpRequest): solicitud HTTP recibida.

    Returns:
    HttpResponse: respuesta HTTP que renderiza página principal.
    '''

    posts = Post.objects.all().order_by('-fecha')                         
    paginador = Paginator(posts, 6)                                       
    numero_pagina = request.GET.get('page')                               
    page_obj = paginador.get_page(numero_pagina)                          
 
    return render(request, 'App_Core/home.html', {"page_obj": page_obj})

```
* home: Página de bienvenida o principal del blog.
* articolos_all: Mustra todos los artículos cargados al blog
* contacto: Fromulario de contacto de visitantes al administrador
* sobre_mi: Breve perfil profesional y fotografías de portafolio
* articulo: Muestra el contenido del artículo seleccionado, así como los comentarios de los visitantes


Para acceder al Panel Administrativo se usa la dirección por defecto otorgada por Django:
`/admin`, ingresando las credenciales del superusuario creado por la instrucción:
```
python manage.py createsuperuser
```

El código posee líneas identificadas con comentarios numerados `# 🠶 01` que no son más que comentarios de 
apoyo al desarrollador. Para consultarlos visitar [Índice de Comentarios](./comentarios.md).
Estos contienen información detallada de cómo funcionan secciones y líneas de código.
    


[volver a home](../README.md)

<br>
<div align="center">
    <span style="font-size: 12px;">Creador por 🠮 Gustavo Colmenares | 
        <a href='https://gustavo9481.github.io/Portafolio/' target="_blank" class="autor__a">GUScode</a>
        © Todos los derechos reservados</span>
</div>

