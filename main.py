import tkinter as tk
from contabilidad import abrir_contabilidad
from productos import abrir_productos
from stock import abrir_stock

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestión")
    ventana.geometry("400x300")
    ventana.config(bg="f1f1f1")
    
    etiqueta = tk.Label(ventana, text="Seleccione una sección", front=("Console", 14), bg="#f1f1f1")
    etiqueta.pack(pady=20)
    
    boton_contabilidad = tk.Button(ventana, text="Contabilidad", width=20, command=abrir_contabilidad)
    boton_contabilidad.pack(pady=10)

    boton_productos = tk.Button(ventana, text="Productos", width=20, command=abrir_productos)
    boton_productos.pack(pady=10)

    boton_stock = tk.Button(ventana, text="Stock", width=20, command=abrir_stock)
    boton_stock.pack(pady=10)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()