# Compatible solo con Python 3.x

import tkinter as tk  # En Python 3 es todo en minúsculas
from typing import Optional

def saludar() -> None:
    nombre = entrada.get()
    etiqueta.config(text=f"👋 ¡Hola, {nombre}!")

ventana = tk.Tk()
ventana.title("App Python 3")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()
