import tkinter as tk
from tkinter import messagebox
from generador_excel import generar_excel

def abrir_stock(usuario_actual, ventana_principal):
    ventana_principal.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Gestión de Stock")
    ventana.geometry("500x450")
    ventana.config(bg="#f8f8f8")

    tk.Label(ventana, text=f"Usuario activo: {usuario_actual['nombre']}", bg="#f8f8f8", fg="blue").pack(pady=5)
    tk.Label(ventana, text="Producto:", bg="#f8f8f8").pack()
    entrada_producto = tk.Entry(ventana)
    entrada_producto.pack()

    tk.Label(ventana, text="Cantidad disponible:", bg="#f8f8f8").pack()
    entrada_cantidad = tk.Entry(ventana)
    entrada_cantidad.pack()

    tk.Label(ventana, text="Ubicación en bodega:", bg="#f8f8f8").pack()
    entrada_ubicacion = tk.Entry(ventana)
    entrada_ubicacion.pack()

    datos_guardados = []

    def guardar():
        if not usuario_actual["nombre"]:
            messagebox.showwarning("Aviso", "Seleccione un usuario primero")
            return
        datos = {
            "Usuario": usuario_actual["nombre"],
            "Producto": entrada_producto.get(),
            "Cantidad": entrada_cantidad.get(),
            "Ubicación": entrada_ubicacion.get()
        }
        datos_guardados.append(datos)
        messagebox.showinfo("Guardado", "Registro añadido correctamente")
        entrada_producto.delete(0, tk.END)
        entrada_cantidad.delete(0, tk.END)
        entrada_ubicacion.delete(0, tk.END)

    def exportar_excel():
        if datos_guardados:
            for datos in datos_guardados:
                generar_excel("stock", datos)
            messagebox.showinfo("Éxito", "Datos exportados a Excel")
        else:
            messagebox.showwarning("Aviso", "No hay datos para exportar")

    def volver():
        ventana.destroy()
        ventana_principal.deiconify()

    tk.Button(ventana, text="Guardar datos", command=guardar).pack(pady=10)
    tk.Button(ventana, text="Exportar a Excel", command=exportar_excel).pack(pady=10)
    tk.Button(ventana, text="Volver al menú", command=volver).pack(pady=10)
