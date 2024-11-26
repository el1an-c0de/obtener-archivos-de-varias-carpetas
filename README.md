# Mover Archivos

Este script en Python permite mover todos los archivos desde una carpeta de origen y sus subcarpetas a una carpeta de destino. Si la carpeta de destino no existe, el script la creará automáticamente. Además, maneja posibles conflictos de nombres de archivos en la carpeta de destino.

## Funcionalidades

- **Mover Archivos**: Mueve todos los archivos desde la carpeta de origen y sus subcarpetas a la carpeta de destino.
- **Crear Carpeta de Destino**: Si la carpeta de destino no existe, la crea automáticamente.
- **Manejo de Conflictos de Nombres**: Si un archivo con el mismo nombre ya existe en la carpeta de destino, el script renombra el archivo para evitar sobrescribirlo.

## Requisitos

- Python 3.x
- Módulos estándar de Python: `os`, `shutil`

## Uso

1. Descargar el archivo: `app.py`.
2. Ejecuta el script desde la línea de comandos:

```sh
python app.py
```
3. Introduce las rutas de la carpeta de origen y la carpeta de destino cuando se te solicite.

## Ejemplo CMD
```sh
Introduce la ruta de la carpeta de origen: C:/Users/user/Downloads
Introduce la ruta de la carpeta de destino: C:/Users/user/Downloads/Carpeta-archivos
Movido: C:/Users/user/Downloads/test.jpg --> C:/Users/user/Downloads/Carpeta-archivos/test.jpg
```

## Notas
- Asegúrate de tener permisos de lectura y escritura en las carpetas de origen y destino.
- El script maneja conflictos de nombres de archivos añadiendo un sufijo numérico al nombre del archivo.

## Licencia
Este proyecto está bajo la Licencia MIT. Consulta el archivo LICENSE para más detalles.