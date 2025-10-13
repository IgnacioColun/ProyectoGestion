import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

ARCHIVO_DATOS = "datos.json"


def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return {"usuarios": []}
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if not isinstance(datos, dict) or "usuarios" not in datos:
            raise ValueError
    except Exception:
        datos = {"usuarios": []}
        guardar_datos(datos)
    return datos


def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def abrir_usuarios(usuario_actual=None, raiz=None):
    ventana = tk.Toplevel()
    ventana.title("Gestión de Usuarios")
    ventana.geometry("600x480")
    ventana.configure(bg="#f7f7f7")

    tk.Label(ventana, text="Gestión de Usuarios", font=("Arial", 16, "bold"), bg="#f7f7f7").pack(pady=10)

    frame = tk.Frame(ventana, bg="#f7f7f7")
    frame.pack(fill="both", expand=True, padx=15, pady=10)

    tk.Label(frame, text="Nombre de usuario:", bg="#f7f7f7").grid(row=0, column=0, sticky="w", pady=5)
    entrada_nombre = ttk.Entry(frame, width=35)
    entrada_nombre.grid(row=0, column=1, pady=5, padx=5)

    columnas = ("ID", "Nombre", "Creado en")
    lista = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    for col in columnas:
        lista.heading(col, text=col)
        lista.column(col, anchor="center", width=180)
    lista.grid(row=2, column=0, columnspan=3, pady=15, sticky="nsew")

    scroll = ttk.Scrollbar(frame, orient="vertical", command=lista.yview)
    lista.configure(yscroll=scroll.set)
    scroll.grid(row=2, column=3, sticky="ns")

    frame.grid_rowconfigure(2, weight=1)
    frame.grid_columnconfigure(1, weight=1)

    def refrescar_lista():
        lista.delete(*lista.get_children())
        datos = cargar_datos()
        for u in datos["usuarios"]:
            if isinstance(u, dict):
                lista.insert("", "end", values=(u.get("id"), u.get("nombre"), u.get("creado_en")))

    def agregar_usuario():
        nombre = entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Debe ingresar un nombre de usuario.")
            return
        datos = cargar_datos()
        if any(u["nombre"].lower() == nombre.lower() for u in datos["usuarios"]):
            messagebox.showerror("Error", "Ese usuario ya existe.")
            return
        nuevo = {
            "id": len(datos["usuarios"]) + 1,
            "nombre": nombre,
            "creado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        datos["usuarios"].append(nuevo)
        guardar_datos(datos)
        entrada_nombre.delete(0, tk.END)
        refrescar_lista()
        messagebox.showinfo("Éxito", f"Usuario '{nombre}' agregado correctamente.")

    def eliminar_usuario():
        seleccion = lista.selection()
        if not seleccion:
            messagebox.showwarning("Aviso", "Seleccione un usuario para eliminar.")
            return
        item = lista.item(seleccion)
        nombre = item["values"][1]
        if not messagebox.askyesno("Confirmar", f"¿Eliminar usuario '{nombre}'?"):
            return
        datos = cargar_datos()
        datos["usuarios"] = [u for u in datos["usuarios"] if u["nombre"] != nombre]
        guardar_datos(datos)
        refrescar_lista()
        messagebox.showinfo("Eliminado", f"Usuario '{nombre}' eliminado correctamente.")

    def volver_menu():
        ventana.destroy()

    boton_frame = tk.Frame(ventana, bg="#f7f7f7")
    boton_frame.pack(pady=10)
    ttk.Button(boton_frame, text="Agregar", command=agregar_usuario).grid(row=0, column=0, padx=5)
    ttk.Button(boton_frame, text="Eliminar", command=eliminar_usuario).grid(row=0, column=1, padx=5)
    ttk.Button(boton_frame, text="Volver al menú", command=volver_menu).grid(row=0, column=2, padx=5)

    refrescar_lista()


if __name__ == "__main__":
    root = tk.Tk()
    abrir_usuarios()
    root.mainloop()
