import tkinter as tk
from tkinter import ttk, messagebox
import json
import os
from datetime import datetime

ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        return {"usuarios": []}
    with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
        return json.load(f)


def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)


def abrir_usuarios(usuario_actual=None, raiz=None):
    ventana = tk.Toplevel()
    ventana.title("Gestión de Usuarios")
    ventana.geometry("500x400")
    ventana.resizable(False, False)

    ttk.Label(ventana, text="Gestión de Usuarios", font=("Arial", 14, "bold")).pack(pady=10)

    frame = ttk.Frame(ventana)
    frame.pack(fill="both", expand=True, padx=10, pady=10)

    ttk.Label(frame, text="Nombre de usuario:").pack(anchor="w")
    entrada_nombre = ttk.Entry(frame, width=40)
    entrada_nombre.pack(pady=5)

    def agregar_usuario():
        nombre = entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Debe ingresar un nombre de usuario.")
            return

        datos = cargar_datos()

        for u in datos["usuarios"]:
            if u["nombre"].lower() == nombre.lower():
                messagebox.showerror("Error", "Ese nombre de usuario ya existe.")
                return

        nuevo_usuario = {
            "id": len(datos["usuarios"]) + 1,
            "nombre": nombre,
            "creado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }
        datos["usuarios"].append(nuevo_usuario)
        guardar_datos(datos)
        refrescar_lista()
        entrada_nombre.delete(0, tk.END)

    ttk.Button(frame, text="Agregar Usuario", command=agregar_usuario).pack(pady=5)

    columnas = ("ID", "Nombre", "Creado en")
    lista = ttk.Treeview(frame, columns=columnas, show="headings", height=10)
    for col in columnas:
        lista.heading(col, text=col)
        lista.column(col, width=150)
    lista.pack(pady=10, fill="x")

    def refrescar_lista():
        lista.delete(*lista.get_children())
        datos = cargar_datos()
        for u in datos["usuarios"]:
            lista.insert("", "end", values=(u["id"], u["nombre"], u["creado_en"]))

    refrescar_lista()

    def eliminar_usuario():
        seleccionado = lista.selection()
        if not seleccionado:
            messagebox.showwarning("Aviso", "Seleccione un usuario para eliminar.")
            return

        item = lista.item(seleccionado)
        nombre = item["values"][1]

        datos = cargar_datos()
        datos["usuarios"] = [u for u in datos["usuarios"] if u["nombre"] != nombre]
        guardar_datos(datos)
        refrescar_lista()
        messagebox.showinfo("Eliminado", f"Usuario '{nombre}' eliminado correctamente.")

    ttk.Button(frame, text="Eliminar Usuario Seleccionado", command=eliminar_usuario).pack(pady=5)
    ttk.Button(frame, text="Cerrar", command=ventana.destroy).pack(pady=10)

if __name__ == "__main__":
    root = tk.Tk()
    abrir_usuarios()
    root.mainloop()
