# Angular Grand - Documentación
Gustavo Colmenares [GUScode] | ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white) [código del proyecto](https://github.com/Gustavo9481/Blog_AngularGrand)<br>
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![SQLite](https://img.shields.io/badge/sqlite-%2307405e.svg?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/html5-%23E34F26.svg?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/css3-%231572B6.svg?style=for-the-badge&logo=css3&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)


<div style="text-align:center">
<img src="Proyecto_Blog/App_Core/static/App_Core/img/AG-logo.svg" alt="Logo Agular Grand" width="300" hight="300"/>
</div>

## Contenido:

* Publicación de nuevo Post (Artículo)
    * [Carga de Videos en artículos desde Youtube](## Carga de Videos en artículos desde Youtube)
    * [Carga de audios para podcast desde Google Drivre](## Carga de audios para podcast desde Google Drivre)
* [Índice de Comentarios del código](./comentarios.md)



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
* 1- Ubicar el video deseado en youtube.com y debajo en las opciones del video presionar *Compartir* 
* 2- En el submenú de *Compartir*, seleccionaremos el ícono **<>** que nos dará el código html para 
embeber el frame con el video.
* 3 - De dicho código tomaremos sólo el siguiente fragmento *https://www.youtube.com/embed/xxxxxxxxxx?si=xxxxxxxxxxx*
Para todos los videos el código aquí identificado con xxxxxxxxxxx es distinto.
* 4- Este fragmente es el que debemos ingresar en el campo video del panel de Administración del Blog
para agregar un video al artículo.
* 5- Despues de ingresado todo el contenido del Post(articulo), presionamos *Guardar* abajo a la derecha.
* 6- Podremos verificar que los cambios se han realizado y el Post se carga correctamente, visitando el 
sitio y la dirección correspondiente al artículo. Si se necesitan hacer modificaciones, podremos dirigirnos
nuevamente al Panel de Administración -> Sección Post -> seleccionar de la lista el post que se quiere modificar.


### Carga de audios para podcast desde Google Drivre
En los artículos se pueden cargar audios(podcast) que profundicen más el tema o den una mejor experiencia
y entendimiento al visitante. Para cargar audios almacenados en Drive debemos seguir el siguiente
procedimiento:
* 1- Previamente, al audio debe estar almacenado en una cuenta Google Drive de la cual d¿se tenga acceso
y permiso de editor, una cuenta propia preferiblemente.Este audio debe ser en formato **mp3** y previamente 
editado como desee el Administrador.
* 2- Ubicando el archivo, abrirlo. Drive mostrará una vista previa y reproducirá el audio, acá solicitaremos
abrir el archivo en una nueva pestaña ingresando el el menú de tres puntos **󰇙** arriba a la derecha.
* 3- El audio abrirá en una nueva pestaña y desde aquí es que copiaremos la dirección url que será parecida
a la siguiente: https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/view, las x representan el id 
único del archivo, este varía de archivo en archivo.
* 4- Cambiaremos la última palabra **view** por **preview** quedando así:
**https://drive.google.com/file/d/xxxxxxxxxxxxxxxxxxxxxxxxxxxxx/preview**.
* 5- Este será el link que se podrá ingresar en el Panel de Administración en la sección de nuevo Post.
* 6- Despues de ingresado todo el contenido del Post(articulo), presionamos *Guardar* abajo a la derecha.
* 7- Podremos verificar que los cambios se han realizado y el Post se carga correctamente, visitando el 
sitio y la dirección correspondiente al artículo. Si se necesitan hacer modificaciones, podremos dirigirnos
nuevamente al Panel de Administración -> Sección Post -> seleccionar de la lista el post que se quiere modificar.


