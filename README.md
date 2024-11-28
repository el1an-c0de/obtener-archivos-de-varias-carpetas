# Mover Archivos

Esta aplicación permite mover archivos desde una carpeta de origen a una carpeta de destino, con la opción de mantener la estructura de carpetas. La interfaz gráfica facilita la selección de carpetas y muestra los logs de la operación en tiempo real.

## Características

- Selección de carpetas de origen y destino.
- Opción para mover archivos manteniendo la estructura de carpetas.
- Interfaz gráfica intuitiva.
- Visualización de logs en tiempo real.
- Pestaña de detalles con información sobre la aplicación.
## Uso
1. Descargar el archivo ejecutable en el siguiente enlace [Releases](https://github.com/el1an-c0de/obtener-archivos-de-varias-carpetas/releases/tag/python)
2. Sigue las instrucciones en la interfaz gráfica para seleccionar las carpetas de origen y destino, y mover los archivos.
![Captura 1](https://github.com/el1an-c0de/obtener-archivos-de-varias-carpetas/blob/main/src/images/captura-1.png)
![Captura 2](https://github.com/el1an-c0de/obtener-archivos-de-varias-carpetas/blob/main/src/images/captura-2.png)
## Requisitos

- Python 3.x
- Bibliotecas de Python: `tkinter`, `os`, `shutil`

## Instalación

1. Clona el repositorio:

```sh
git clone https://github.com/tu-usuario/mover-archivos.git
cd mover-archivos
```
2. Ejecuta el script de Python:
```sh
python app.py
```
3. Sigue las instrucciones en la interfaz gráfica para seleccionar las carpetas de origen y destino, y mover los archivos.

## Crear un Archivo Ejecutable
Para crear un archivo ejecutable (.exe) que permita a los usuarios ejecutar la aplicación sin necesidad de tener Python instalado, sigue estos pasos:
1. Instala ```PyInstaller```:
```
pip install pyinstaller
```
2. Crea el archivo ejecutable:
```
pyinstaller --onefile --windowed --icon=src/images/icon.ico app.py
```
3. Verificar el archivo ejecutable:
Navega hasta el directorio ```dist``` y ejecuta ```app.exe```.

## Contribución
Si deseas contribuir a este proyecto, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu nueva característica ```(git checkout -b feature/nueva-caracteristica)```.
3. Realiza tus cambios y haz commit ```(git commit -am 'Añadir nueva característica')```.
4. Haz push a la rama ```(git push origin feature/nueva-caracteristica)```.
5. Crea un Pull Request.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.

## Contacto
- Desarrollador: Elian Ramírez
- GitHub: @el1an-c0de
- Correo Electrónico: elianRAMIER2017@hotmail.com

¡Gracias por utilizar Organizador de Archivos! Si tienes alguna pregunta, sugerencia o encuentras algún error, no dudes en contactarme.
