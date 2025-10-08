import tkinter as tk
from tkinter import messagebox

def abrir_gestion_usuarios(usuario_actual, ventana_principal):
    ventana_principal.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Gestión de Usuarios")
    ventana.geometry("400x350")
    ventana.config(bg="#f8f8f8")

    lista_usuarios = []

    tk.Label(ventana, text="Nombre del usuario:", bg="#f8f8f8").pack()
    entrada_nombre = tk.Entry(ventana)
    entrada_nombre.pack()

    lista = tk.Listbox(ventana, width=30)
    lista.pack(pady=10)

    def agregar_usuario():
        nombre = entrada_nombre.get().strip()
        if nombre:
            lista_usuarios.append(nombre)
            lista.insert(tk.END, nombre)
            entrada_nombre.delete(0, tk.END)
        else:
            messagebox.showwarning("Atención", "Ingrese un nombre válido")

    def seleccionar_usuario():
        seleccion = lista.curselection()
        if seleccion:
            usuario_actual["nombre"] = lista_usuarios[seleccion[0]]
            messagebox.showinfo("Usuario activo", f"Usuario seleccionado: {usuario_actual['nombre']}")
        else:
            messagebox.showwarning("Aviso", "Seleccione un usuario de la lista")

    def volver():
        ventana.destroy()
        ventana_principal.deiconify()

    tk.Button(ventana, text="Agregar usuario", command=agregar_usuario).pack(pady=5)
    tk.Button(ventana, text="Seleccionar usuario", command=seleccionar_usuario).pack(pady=5)
    tk.Button(ventana, text="Volver al menú", command=volver).pack(pady=15)
