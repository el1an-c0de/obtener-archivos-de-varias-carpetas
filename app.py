import os
import shutil
import tkinter as tk
from tkinter import filedialog, messagebox, ttk, scrolledtext

def mover_archivos(origen, destino, mover_con_carpetas, log_text):
    """
    Mueve todos los archivos desde la carpeta de origen y sus subcarpetas
    a la carpeta de destino.

    :param origen: Ruta de la carpeta de origen.
    :param destino: Ruta de la carpeta de destino.
    :param mover_con_carpetas: Booleano que indica si se deben mover los archivos con sus carpetas.
    :param log_text: Widget de texto para mostrar los logs.
    """
    # Verificar si la carpeta de destino existe, si no, crearla
    if not os.path.exists(destino):
        os.makedirs(destino)
        log_text.insert(tk.END, f"Carpeta de destino creada: {destino}\n")

    # Recorrer todas las carpetas y subcarpetas
    for carpeta_actual, subcarpetas, archivos in os.walk(origen):
        for archivo in archivos:
            ruta_archivo = os.path.join(carpeta_actual, archivo)
            if mover_con_carpetas:
                # Mantener la estructura de carpetas
                rel_path = os.path.relpath(carpeta_actual, origen)
                ruta_destino = os.path.join(destino, rel_path, archivo)
                os.makedirs(os.path.dirname(ruta_destino), exist_ok=True)
            else:
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
                log_text.insert(tk.END, f"Movido: {ruta_archivo} --> {ruta_destino}\n")
            except Exception as e:
                log_text.insert(tk.END, f"Error al mover {ruta_archivo}: {e}\n")

    log_text.insert(tk.END, "Todos los archivos han sido movidos exitosamente.\n")

def seleccionar_carpeta_origen():
    carpeta_origen.set(filedialog.askdirectory())

def seleccionar_carpeta_destino():
    carpeta_destino.set(filedialog.askdirectory())

def iniciar_movimiento():
    origen = carpeta_origen.get()
    destino = carpeta_destino.get()
    mover_con_carpetas = var_mover_con_carpetas.get()

    if not origen or not destino:
        messagebox.showerror("Error", "Por favor, selecciona ambas carpetas de origen y destino.")
        return

    mover_archivos(origen, destino, mover_con_carpetas, log_text)
    messagebox.showinfo("Éxito", "Todos los archivos han sido movidos exitosamente.")

# Crear la ventana principal
root = tk.Tk()
root.title("Mover Archivos")

# Crear el notebook para las pestañas
notebook = ttk.Notebook(root)
notebook.pack(expand=1, fill="both")

# Crear la pestaña principal
tab_principal = ttk.Frame(notebook)
notebook.add(tab_principal, text="Principal")

# Variables para las rutas de las carpetas
carpeta_origen = tk.StringVar()
carpeta_destino = tk.StringVar()
var_mover_con_carpetas = tk.BooleanVar()

# Crear widgets en la pestaña principal
tk.Label(tab_principal, text="Carpeta de origen:").grid(row=0, column=0, padx=10, pady=10)
tk.Entry(tab_principal, textvariable=carpeta_origen, width=50).grid(row=0, column=1, padx=10, pady=10)
tk.Button(tab_principal, text="Seleccionar", command=seleccionar_carpeta_origen).grid(row=0, column=2, padx=10, pady=10)

tk.Label(tab_principal, text="Carpeta de destino:").grid(row=1, column=0, padx=10, pady=10)
tk.Entry(tab_principal, textvariable=carpeta_destino, width=50).grid(row=1, column=1, padx=10, pady=10)
tk.Button(tab_principal, text="Seleccionar", command=seleccionar_carpeta_destino).grid(row=1, column=2, padx=10, pady=10)

tk.Checkbutton(tab_principal, text="Mover archivos con carpetas", variable=var_mover_con_carpetas).grid(row=2, column=0, columnspan=3, padx=10, pady=10)

tk.Button(tab_principal, text="Iniciar Movimiento", command=iniciar_movimiento).grid(row=3, column=0, columnspan=3, padx=10, pady=10)

# Crear la sección de logs
log_text = scrolledtext.ScrolledText(tab_principal, wrap=tk.WORD, width=70, height=10)
log_text.grid(row=4, column=0, columnspan=3, padx=10, pady=10)

# Crear la pestaña de detalles
tab_detalles = ttk.Frame(notebook)
notebook.add(tab_detalles, text="Detalles")

# Agregar contenido a la pestaña de detalles
detalles_texto = """
Esta aplicación permite mover archivos desde una carpeta de origen a una carpeta de destino.
Puedes elegir si deseas mover los archivos manteniendo la estructura de carpetas o no.

Instrucciones:
1. Selecciona la carpeta de origen.
2. Selecciona la carpeta de destino.
3. Marca la opción 'Mover archivos con carpetas' si deseas mantener la estructura de carpetas.
4. Haz clic en 'Iniciar Movimiento' para comenzar el proceso.

Desarrollado por el1an-c0de
"""
tk.Label(tab_detalles, text=detalles_texto, justify=tk.LEFT).pack(padx=10, pady=10)

# Iniciar el bucle principal de la aplicación
root.mainloop()
