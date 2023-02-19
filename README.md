# Bienvenidos a mi proyecto CONNECTOR SHOP

## Introdución

Soy Julio Andrés Alarcón Caballero, estudiante de Python Comisión 34665, este es mi proyecto llamado Connector Shop, el cual consiste en la tercera entrega en CoderHouse


## Descripción

En este proyecto se cumplen los siguientes puntos
- Desarrollar una WEB en Django con patrón MVT
- Herencia HTML
- 3 clases en models
- Un formulario para insertar datos a todas las clases en models
- Un formulario para buscar en la BD
- Readme que indique el orden en el que se prueban las cosas y donde se encuentran las funcionalidades


## Herencia HTML

El .HTML que se heredara es el:

**base.html**

El cual contiene un nav bar con accesos a otros templates, entre estas opciones tenemos la pagina de productos y las opciones para editar y ver la información del usuario y adminstrador.

-Templates que heredan esta base son: **todos**

-Ruta del .html: **connectorshop/templates/base.html**

-Permisos: **Ninguno**


## 3 Clases en models

Los modelos son:

-**Category**
-**Tag**
-**Article**

Los models Tag y Category componen parte del model Article de forma muchos a muchos, **Tag** contendra todos los textos que querramos para definir un producto, por Ej: "Nuevo", "Usado", "Tecnologico", etc.., **Category** contendra todos los tipos de productos de los que puede proceder un articulo, por Ej: "CPU", "Teclado", "Microfono", etc.., **Article** contendra todos los articulos que se registran en la tienda con sus respectivos datos como el stock, sku, precio, descripcion, tags, categoria y si se encuentra publicado para su compra.

-Ruta de los models: **connectorshop/models.py**

## Formulario para insertar datos a los models

Los formularios son:

-**TagForm**
-**CategoryForm**
-**ArticleForm**

Los siguientes formularios cumplen con los diferentes fields que contiene cada uno de estos models y les da un formato al input correspondiente

-Templates que ocupan el formulario **TagForm**: **tag_edit.html** y **tag_new**
-Templates que ocupan el formulario **CategoryForm**: **category_edit.html** y **category_new**
-Templates que ocupan el formulario **ArticleForm**: **article_edit.html** y **article_new**
-Ruta templates: **connectorshop/templates/tags/**, **connectorshop/templates/categories/**, **connectorshop/templates/articles/**
-Ruta de los forms: **connectorshop/forms.py**
-Permisos: **@superuser_required**

## Formulario para buscar en la BD

El formulario es:

-**ArticleSearchForm**

El siguiente formulario ayuda a buscar entre los distintos tipos de productos que se encuentran a la venta

-Template que ocupa el formulario: **products.html**
-Ruta del template: **connectorshop/templates/products.html**
-Permisos: **@login_required**

## Readme que indique el orden en el cual se prueban las cosas

- url: "/" Registro de cuenta o inicio de sesion
**@login_required**
- url: "/home" Visualización de la información del usuario
- url: "/user_edit" Formulario que te permitira editar la información del usuario
- url: "/products" Lista en el cual te encontraras todos los productos
- url: "/logout" Cerrar sesion
**@superuser_required**
- url: "/article/list" Lista de articulos en formato texto, con posibilidad de crear uno nuevo, ver los detalles, editar la información y eliminar
- url: "/article/new" Formulario para crear un nuevo articulo
- url: "/article/<int:pk>/edit" Formulario que permite editar la informacion de un articulo
- url: "/article/<int:pk>/delete" Eliminar el articulo
- url: "/tag/list" Lista de tags en formato texto, con posibilidad de crear uno nuevo, ver los detalles, editar la información y eliminar
- url: "/tag/new" Formulario para crear un nuevo tag
- url: "/tag/<int:pk>/edit" Formulario que permite editar la informacion de un tag
- url: "/tag/<int:pk>/delete" Eliminar el tag
- url: "/category/list" Lista de categorias en formato texto, con posibilidad de crear una nueva, ver los detalles, editar la información y eliminar
- url: "/category/new" Formulario para crear una nueva categoria
- url: "/category/<int:pk>/edit" Formulario que permite editar la informacion de una categoria
- url: "/category/<int:pk>/delete" Eliminar la categoria
