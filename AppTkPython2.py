# -*- coding: utf-8 -*-
# Compatible solo con Python 2.x

import Tkinter as tk  # En Python 2 es con "T" mayúscula

def saludar():
    nombre = entrada.get()
    mensaje = "Hola, " + nombre
    etiqueta.config(text=mensaje)

ventana = tk.Tk()
ventana.title("App Python 2")

etiqueta = tk.Label(ventana, text="Ingresa tu nombre:")
etiqueta.pack()

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text="Saludar", command=saludar)
boton.pack()

ventana.mainloop()
