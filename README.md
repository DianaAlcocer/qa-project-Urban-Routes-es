# Diana Carolina Alcocer Garcia - Grupo 27.o - Sprint 8
# Proyecto Urban Routes
## _Pruebas para comprobar la funcionalidad de Urban Routes al pedir un taxi con la tarifa comfort_

_Objetivo de las comprobaciones_
- Verificar que se puede introducir información en los campos de texto y la información introducida coincide con la enviada.
- Validar que los botones están habilitados y realizan la acción esperada.
- Comprobar que los selectores permanecen activos después de accionados.

_Especificaciones técnicas:_

- Necesitas tener instalados los siguientes paquetes y programas: 

| Type     | Program                   |
|----------|---------------------------|
| Terminal | Cywing                    |
| IDE      | PyCharm Community Edition |

>Puedes utilizar otras terminales como WSL, Git Bash o CMD.R y otros editores de código como Visual Studio Code.

| Package  | Terminal_command     |       
|----------|----------------------|       
| pytest   | pip install pytest   |       
| selenium | pip install selenium |

>Puedes utilizar la terminal o buscarlos en la pestaña _Python packages_ dentro de la aplicación PyCharm.

_Pasos a seguir para la ejecución de las pruebas:_

1. Abrir la carpeta del proyecto en un editor de código o IDE.
2. Instalar paquetes _pytest_ y _selenium_.
3. Actualizar la url del servidor en _urban_routes_url_ en el archivo _data.py_.
4. Ejecutar las pruebas mediante la herramienta 'Run':

>Se pueden ejecutar de forma individual: haciendo click en el icono de Run ubicado a la izquierda de cada prueba,
o ejecutar Run para todos los test del archivo Main.py: haciendo click en el icono de Run ubicado en la parte superior
del archivo.

>NOTE: Si deseas modificar los datos sobre la ruta, teléfono, número y código de la tarjeta de credito, mensaje al conductor, elementos adicionales como manta y numero de helados, dirigete al archivo _data.py_ 

_Descripción del proceso completo de pedir un taxi:_

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
