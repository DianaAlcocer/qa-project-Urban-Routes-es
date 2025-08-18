# Proyecto Urban Routes - Sp_8

### _Pruebas automatizadas para comprobar la funcionalidad de Urban Routes al pedir un taxi con la tarifa comfort_

### Descripción

- Se verificó que se pudiera introducir información en los campos de texto y la información introducida coincidiera con la enviada.
- Se validó que los botones estuvieran habilitados y realizaran la acción esperada.
- Se comprobó que los selectores permanecieran activos después de accionados.

### Contenido

data.py

main.py

### Proceso completo de pedir un taxi:

1. Configurar la dirección
2. Seleccionar la tarifa Comfort
3. Rellenar el número de teléfono
4. Agregar una tarjeta de crédito
5. Escribir un mensaje para el conductor
6. Pedir una manta y pañuelos
7. Pedir 2 helados
8. Aparición del modal para buscar un conductor o taxi, con cuenta regresiva
9. Aparición del modal con información sobre el conductor o viaje

>El paso 8 y 9 se encuentran en proceso de desarrollo, debido a que la ventana para buscar un conductor
> solo aparece por una fracción de segundo, y por consiguiente, la ventana de información sobre el viaje no se despliega.


### Configuración

#### Requisitos

- Variables de entorno:
  - URL_SERVICE (URL del servidor de Urban Routes)
- Un editor de código:
  - *Pycharm*
- Paquetes:
  - _pytest_
  - _selenium_

>Puedes utilizar la terminal o buscarlos en la pestaña _Python packages_ dentro de la aplicación PyCharm.

#### Instrucciones

1. Clonar o descargar la carpeta del proyecto
2. Abrirla en un editor de código o IDE como Pycharm
3. Instalar paquetes _pytest_ y _requests_ desde terminal o en python packages
4. Actualizar la url del servidor en _urban_routes_url_ en el archivo _data.py_.
5. Ejecutar las pruebas mediante la herramienta 'Run':

>Se pueden ejecutar de forma individual: haciendo clic en el icono de Run ubicado a la izquierda de cada prueba,
o ejecutar Run para todos los test del archivo Main.py: haciendo clic en el icono de Run ubicado en la parte superior
del archivo.

>NOTE: Si deseas modificar los datos sobre la ruta, teléfono, número y código de la tarjeta de credito, mensaje al conductor, elementos adicionales como manta y número de helados, dirígete al archivo _data.py_
