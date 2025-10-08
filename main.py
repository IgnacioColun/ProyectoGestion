import tkinter as tk
from usuarios import abrir_gestion_usuarios
from contabilidad import abrir_contabilidad
from productos import abrir_productos
from stock import abrir_stock

usuario_actual = {"nombre": ""}

def iniciar_interfaz():
    ventana = tk.Tk()
    ventana.title("Sistema de Gestion")
    ventana.geometry("450x350")
    ventana.config(bg="#f1f1f1")

    tk.Label(ventana, text="Sistema de Gestion", font=("Arial", 16, "bold"), bg="#f1f1f1").pack(pady=10)

    def abrir_usuarios():
        abrir_gestion_usuarios(usuario_actual, ventana)

    def abrir_conta():
        abrir_contabilidad(usuario_actual, ventana)

    def abrir_prod():
        abrir_productos(usuario_actual, ventana)

    def abrir_stock_ventana():
        abrir_stock(usuario_actual, ventana)

    tk.Button(ventana, text="Gestionar Usuarios", width=25, command=abrir_usuarios).pack(pady=8)
    tk.Button(ventana, text="Contabilidad", width=25, command=abrir_conta).pack(pady=8)
    tk.Button(ventana, text="Productos", width=25, command=abrir_prod).pack(pady=8)
    tk.Button(ventana, text="Stock", width=25, command=abrir_stock_ventana).pack(pady=8)

    ventana.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()