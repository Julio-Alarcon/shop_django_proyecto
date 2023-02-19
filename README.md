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


### Herencia HTML

El .HTML que se heredara es el:


**base.html**

El cual contiene un nav bar con accesos a otros templates, entre estas opciones tenemos la pagina de productos y las opciones para editar y ver la información del usuario y adminstrador.

Templates que heredan esta base son: **todos**
Ruta del .html: **connectorshop/templates/base.html**
Permisos: **Ninguno**


### 3 clases en models

Los modelos son:

**Category**
**Tag**
**Article**

Los models Tag y Category componen parte del model Article de forma muchos a muchos, **tag** contendra todos los textos que querramos para definir un producto, por Ej: "Nuevo", "Usado", "Tecnologico", etc.., **Category** contendra todos los tipos de productos de los que puede proceder un articulo, por Ej: "CPU", "Teclado", "Microfono", etc.., **Article** contendra todos los articulos que se registran en la tienda con sus respectivos datos como el stock, sku, precio, descripcion, tags, categoria y si se encuentra publicado para su compra.

Ruta de los models: **connectorshop/models.py**


### Formulari para insertar datos a los models
