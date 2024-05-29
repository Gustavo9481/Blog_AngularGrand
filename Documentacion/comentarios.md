# Índice de Comentarios
[volver a home](../README.md)

### 🖿 Proyecto Blog

`settings.py` 
* 🠶 01 - carga de variables de entorno (dotenv)
* 🠶 02 - Agregar la secret_key al .gitignore y llevarla a variable de entorno .env.
* 🠶 03 - Asignación de nombre al sitio web.
* 🠶 04 - Variable para ejecución asíncrona.
* 🠶 05 - Requests atómicos para la base de datos, impide la duplicación de datos y consultas rápidas.
* 🠶 06 - Configuraciónde zona horaria.

---

### 🖿 App Core

`views.py` 
Funciones de vistas de aplicación
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



`services.py`
obtención de data - patrón **Service Layer**
* 🠶 01 - solicitud a BD de los artículos ordenados por fecha (reciente -> antiguo).
    * métodos para obtener datos de las tablas Post y Comentarios:
        * objects.get(@): unico registro con el filtro @
        * objects.filter(@): filtro de registros @
        * objects.all(): trae todos los registros



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


[volver a home](../README.md)
<br>
<div align="center">
    <span style="font-size: 12px;">Creador por 🠮 Gustavo Colmenares | 
        <a href='https://gustavo9481.github.io/Portafolio/' target="_blank" class="autor__a">GUScode</a>
        © Todos los derechos reservados</span>
</div>

