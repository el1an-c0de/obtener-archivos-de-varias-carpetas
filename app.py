import os
import shutil

def mover_archivos(origen, destino):
    """
    Mueve todos los archivos desde la carpeta de origen y sus subcarpetas
    a la carpeta de destino.
    
    :param origen: Ruta de la carpeta de origen.
    :param destino: Ruta de la carpeta de destino.
    """
    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(destino):
        os.makedirs(destino)
        print(f"Carpeta de destino creada: {destino}")
    
    # Recorrer todas las carpetas y subcarpetas
    for carpeta_actual, subcarpetas, archivos in os.walk(origen):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_actual, archivo)
            # Definir la ruta de destino
            ruta_destino = os.path.join(destino, archivo)
            
            # Manejar posibles conflictos de nombres
            contador = 1
            nombre, extension = os.path.splitext(archivo)
            while os.path.exists(ruta_destino):
                nuevo_nombre = f"{nombre}_{contador}{extension}"
                ruta_destino = os.path.join(destino, nuevo_nombre)
                contador += 1
            
            try:
                shutil.move(ruta_archivo, ruta_destino)
                print(f"Movido: {ruta_archivo} --> {ruta_destino}")
            except Exception as e:
                print(f"Error al mover {ruta_archivo}: {e}")

    print("Todos los archivos han sido movidos exitosamente.")

if __name__ == "__main__":
    # Solicitar al usuario las rutas de origen y destino
    carpeta_origen = input("Introduce la ruta de la carpeta de origen: ").strip('"')
    carpeta_destino = input("Introduce la ruta de la carpeta de destino: ").strip('"')
    
    mover_archivos(carpeta_origen, carpeta_destino)
