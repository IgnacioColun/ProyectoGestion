import tkinter as tk
from tkinter import messagebox
from generador_excel import generar_excel

def abrir_productos(usuario_actual, ventana_principal):
    ventana_principal.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Gestión de Productos")
    ventana.geometry("500x450")
    ventana.config(bg="#f8f8f8")

    tk.Label(ventana, text=f"Usuario activo: {usuario_actual['nombre']}", bg="#f8f8f8", fg="blue").pack(pady=5)
    tk.Label(ventana, text="Nombre del producto:", bg="#f8f8f8").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    tk.Label(ventana, text="Precio:", bg="#f8f8f8").pack()
    entrada_precio = tk.Entry(ventana)
    entrada_precio.pack()

    tk.Label(ventana, text="Categoría:", bg="#f8f8f8").pack()
    entrada_categoria = tk.Entry(ventana)
    entrada_categoria.pack()

    tk.Label(ventana, text="Descripción:", bg="#f8f8f8").pack()
    entrada_desc = tk.Entry(ventana, width=50)
    entrada_desc.pack()

    datos_guardados = []

    def guardar():
        if not usuario_actual["nombre"]:
            messagebox.showwarning("Aviso", "Seleccione un usuario primero")
            return
        datos = {
            "Usuario": usuario_actual["nombre"],
            "Nombre": entrada_nombre.get(),
            "Precio": entrada_precio.get(),
            "Categoría": entrada_categoria.get(),
            "Descripción": entrada_desc.get()
        }
        datos_guardados.append(datos)
        messagebox.showinfo("Guardado", "Producto añadido correctamente")
        entrada_nombre.delete(0, tk.END)
        entrada_precio.delete(0, tk.END)
        entrada_categoria.delete(0, tk.END)
        entrada_desc.delete(0, tk.END)

    def exportar_excel():
        if datos_guardados:
            for datos in datos_guardados:
                generar_excel("productos", datos)
            messagebox.showinfo("Éxito", "Datos exportados a Excel")
        else:
            messagebox.showwarning("Aviso", "No hay productos para exportar")

    def volver():
        ventana.destroy()
        ventana_principal.deiconify()

    tk.Button(ventana, text="Guardar producto", command=guardar).pack(pady=10)
    tk.Button(ventana, text="Exportar a Excel", command=exportar_excel).pack(pady=10)
    tk.Button(ventana, text="Volver al menú", command=volver).pack(pady=10)
