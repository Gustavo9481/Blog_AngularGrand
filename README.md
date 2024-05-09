# Angular Grand - Documentación
Proyecto Blog | Python - Django
![Diagrama de Uso](Blog_Angulargrand.png)

Contenido:

* Publicación de nuevo Post (Artículo)
    * Carga de Videos en artículos desde Youtube
    * Carga de audios para podcast desde Google Drivre
* Índice de Comentarios del código
---
---
## Publicación de nuevo Post (Artículo)
Para la publicaciṕn de un nuevo artículo, el Administrador(propietario) debe ingresar con sus
credenciales de administrador a la dirección `http://angulargrand/admin/`, la cual lo dirigirá
al Panel de Adminitración.
En el meú de la izquierda se encontrarán las opciones:
* Comentarios  -> listado general de Comentarios de los visitantes en los artículos
* Contactos    -> Listado de visitantes y mensajes enviados al Administrador
* Post         -> Lista General de Artículos publicados por el Administrador
La sección para agregar nuevos Post(artículo) cuenta con el editor de texto enriquecido (ckeditor) que permite visualizar el texto
tal cual será publicado, permitiendo dar estilos al texto, ingresar iconos, emoticonos, tablas,
líneas, etc.

Todas los registros son modificables por el Administrador, estos podrán ser:
* Creados, agregar nuevos registros.
* Leídos, revisión del contenido de los registros.
* Modificados, cambiar contenido de los registros.
* Eliminados, borrar registros

### Carga de Videos en artículos desde Youtube
Los videos pueden ser directamente incrustados desde youtube usando el siguiente procedimiento:
1- Ubicar el video deseado en youtube.com y debajo en las opciones del video presionar *Compartir* 
2- En el submenú de *Compartir*, seleccionaremos el ícono **<>** que nos dará el código html para 
embeber el frame con el video.
3 - De dicho código tomaremos sólo el siguiente fragmento *https://www.youtube.com/embed/xxxxxxxxxx?si=xxxxxxxxxxx*
Para todos los videos el código aquí identificado con xxxxxxxxxxx es distinto.
4- Este fragmente es el que debemos ingresar en el campo video del panel de Administración del Blog
para agregar un video al artículo.
5- Despues de ingresado todo el contenido del Post(articulo), presionamos *Guardar* abajo a la derecha.
6- Podremos verificar que los cambios se han realizado y el Post se carga correctamente, visitando el 
sitio y la dirección correspondiente al artículo. Si se necesitan hacer modificaciones, podremos dirigirnos
nuevamente al Panel de Administración -> Sección Post -> seleccionar de la lista el post que se quiere modificar.


### Carga de audios para podcast desde Google Drivre
En los artículos se pueden cargar audios(podcast) que profundicen más el tema o den una mejor experiencia
y entendimiento al visitante. Para cargar audios almacenados en Drive debemos seguir el siguiente
procedimiento:
1- Previamente, al audio debe estar almacenado en una cuenta Google Drive de la cual d¿se tenga acceso
y permiso de editor, una cuenta propia preferiblemente.Este audio debe ser en formato **mp3** y previamente 
editado como desee el Administrador.
2- Ubicando el archivo, abrirlo. Drive mostrará una vista previa y reproducirá el audio, acá solicitaremos
abrir el archivo en una nueva pestaña ingresando el el menú de tres puntos **󰇙** arriba a la derecha.
3- El audio abrirá en una nueva pestaña y desde aquí es que copiaremos la dirección url que será parecida
a la siguiente: https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/view, las x representan el id 
único del archivo, este varía de archivo en archivo.
4- Cambiaremos la última palabra **view** por **preview** quedando así:
**https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/preview**.
5- Este será el link que se podrá ingresar en el Panel de Administración en la sección de nuevo Post.
6- Despues de ingresado todo el contenido del Post(articulo), presionamos *Guardar* abajo a la derecha.
7- Podremos verificar que los cambios se han realizado y el Post se carga correctamente, visitando el 
sitio y la dirección correspondiente al artículo. Si se necesitan hacer modificaciones, podremos dirigirnos
nuevamente al Panel de Administración -> Sección Post -> seleccionar de la lista el post que se quiere modificar.

---
---
## Índice de Comentarios


### Proyecto Blog

`settings.py` 
* 🠶 01 - carga de variables de entorno (dotenv)
* 🠶 02 - Agregar la secret_key al .gitignore y llevarla a variable de entorno .env.
* 🠶 03 - Asignación de nombre al sitio web.
* 🠶 04 - Variable para ejecución asíncrona.
* 🠶 05 - Requests atómicos para la base de datos, impide la duplicación de datos y consultas rápidas.
* 🠶 06 - Configuraciónde zona horaria.

---

### App Core

`views.py` 
Funciones de vistas de aplicación
* 🠶 01 - solicitud a BD de los artículos ordenados por fecha (reciente -> antiguo).
    * métodos para obtener datos de las tablas Post y Comentarios:
        * objects.get(@): unico registro con el filtro @
        * objects.filter(@): filtro de registros @
        * objects.all(): trae todos los registros
* 🠶 02 - paginación de los artículos stx: Paginador(<01>, <n° de paǵinas>).
* 🠶 03 - obtención de la página actual del total de los artículos.
* 🠶 04 - aplicación del paginador.
* 🠶 05 - Verificación del método POST: 
    * true > se ingresa como data al formulario request.POST, la información ingresada por el cliente, salvando el formulario y agregando la key mensaje al objeto data para que sea mostrado al usuario.
    * false > se reasigna a data[form] el formulario para ser recargado
* 🠶 06 - seleccionar de BD artículo por título.
* 🠶 07 - seleccionar de BD comentarios relacionados al artículo filtrado 06
* 🠶 08 - Incrustar valor dinámico a un input de formulario, .instance.art_relacionado toma el valor del título del post mostrado para que se almacene cono post relacionado en tabla Comentario.
* 🠶 09 - help(): permite corroborar el tipo de datos que usa una función como parámetros y valores retornados.



`urls.py`
urls registradas de App Core
* 🠶 01 - Agrega el path o la ruta de la carpeta MEDIA mientras el DEBUG está activo, permitiendo el renderizado de las imágenes que se cargan en las tablas a través de los formularios.



`models.py`
modelos de tablas Post - Contacto - Comentarios
* 🠶 01 - opciones de etiqueta para los artículos.
* 🠶 02 - campo de modelo con opciones a elegir.
* 🠶 03 - implementación de editor de texto enriquecido para contenido de artículos.
* 🠶 04 - Carga de imagenes a las tablas, las propiedades blank y null hacen opcionales las respuestas en los formularios.
* 🠶 05 - propiedad editable -> permite un campo oculto en el formulario html.



`admin.py`
registros en el panel de administración.
* 🠶 01 - personalización del aspecto de las tablas en el panel administrativo:
    * list_display -> campos a mostrar en el panel
    * search_fields -> campos donde buscar
    * readonly_fields -> campos que tendran una respuesta automática

---

### Static - CSS | templates html

`styles.css`
Estilos generales, fuentes, variables globales, reset css, paleta de colores
* 🠶 01 - personalización de texto seleccionado en la página, mozilla y chrome
* 🠶 02 - Eliminar la barra de desplazamiento ::webkit scroll-bar.

`base`
* 🠶 01 - Link para insertar CSS custom.

`articulo.html`
* 🠶 01 - tag |safe => mantiene el formato del editor enriquecido para que se muestre tal cual se edita.

`articulos_all`
* 🠶 01 - Valor dinámico para el parámetro de una url, tomando el valor de un registro, esto permite una única plantilla html y url para todos los artículos existentes y que el visitante clickee.

