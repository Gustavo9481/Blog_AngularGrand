# Documentación 
[volver a home](../README.md)

                     <p><strong>Lenguaje de Programación Principal:</strong></p>
                    <ul><li>* Python</li></ul><br>
                    <p>Framework:</p>
                    <ul><li>* Django</li></ul><br>
                    
                    <h2 class="sub-titulo__h2">Backend</h2><br>
                    <p>Base de Datos:</p>
                    <p>SQLite (por defecto, para desarrollo)<br>
                        Posibilidad de usar PostgreSQL o MySQL para producción</p><br>

                    Modelos:

Modelo para Post: incluye campos como título, contenido, fecha de publicación, autor y estado (borrador o publicado).
Modelo para Comentarios: incluye campos como nombre del comentarista, correo electrónico, contenido del comentario, fecha de creación y referencia al post relacionado.
Modelo para Categorías y Etiquetas (opcional): permite clasificar y etiquetar posts.
Autenticación y Autorización:

Sistema de autenticación de Django para administración de usuarios.
Posibilidad de crear diferentes roles de usuario (admin, autor, lector).
Administración:

Interfaz de administración de Django para gestionar posts, comentarios, categorías y usuarios.
Frontend
Plantillas:

Uso del motor de plantillas de Django (Django Templates).
Plantillas para páginas de listado de posts, detalle de post, formulario de comentario, página de categorías, etc.
Estilos y Diseño:

HTML5 y CSS3.
Framework CSS como Bootstrap para diseño responsivo (opcional).
Funcionalidades del Blog
Publicación de Posts:

Crear, editar y eliminar posts desde la interfaz de administración.
Programar publicaciones futuras.
Comentarios:

Formulario para que los usuarios dejen comentarios en los posts.
Moderación de comentarios (aprobar o rechazar desde la administración).
Clasificación y Etiquetado:

Sistema de categorías para agrupar posts similares.
Etiquetas para una mejor indexación y búsqueda.
Búsqueda:

Funcionalidad de búsqueda para encontrar posts por título o contenido.
Paginación:

Paginación de listas de posts para mejorar la navegación.
Feeds RSS:

Generación de feeds RSS para que los usuarios se suscriban a las actualizaciones del blog.
Seguridad
Protección contra CSRF:

Uso del middleware CSRF de Django para proteger contra ataques de falsificación de solicitud entre sitios.
Validación y Saneamiento de Entradas:

Validación de datos en formularios y saneamiento para evitar inyección de código.
Autenticación:

Seguridad en el manejo de contraseñas y autenticación de usuarios.
Despliegue
Servidor de Aplicaciones:

Gunicorn o uWSGI para servir la aplicación en producción.
Servidor Web:

Nginx o Apache como servidor web frontend.
Despliegue en la Nube:

Opciones para desplegar en plataformas como Heroku, AWS, DigitalOcean, etc.
Gestión de Archivos Estáticos y Media:

Configuración para servir archivos estáticos y de medios en producción (por ejemplo, usando Amazon S3).
Desarrollo y Mantenimiento
Control de Versiones:

Uso de Git para control de versiones del código.
Entorno Virtual:

Uso de entornos virtuales (virtualenv o venv) para gestionar dependencias de Python.
Pruebas:

Tests unitarios y de integración usando el framework de pruebas de Django.
Documentación:

Documentación del proyecto y del código para facilitar el mantenimiento y la colaboración.

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

