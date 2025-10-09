import tkinter as tk
from tkinter import ttk, messagebox, simpledialog
from datos import cargar_datos, agregar_producto_diccion, actualizar_producto_diccion, eliminar_producto_diccion
from generador_excel import exportar_lista_a_excel

def abrir_productos(usuario_actual, ventana_principal):
    ventana_principal.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Inventario")
    ventana.geometry("820x520")
    ventana.config(bg="#f3f4f6")

    datos = cargar_datos()

    marco = ttk.Frame(ventana, padding=12)
    marco.pack(fill="both", expand=True)

    cab = ttk.Frame(marco)
    cab.pack(fill="x")
    ttk.Label(cab, text=f"Usuario activo: {usuario_actual.get('nombre','')}", font=("Arial", 11)).pack(side="left")
    ttk.Button(cab, text="Volver al menú", command=lambda: volver()).pack(side="right")

    controles = ttk.Frame(marco)
    controles.pack(fill="x", pady=(8,8))
    ttk.Label(controles, text="Nombre").grid(row=0, column=0, padx=4, pady=2, sticky="w")
    entrada_nombre = ttk.Entry(controles, width=30); entrada_nombre.grid(row=0, column=1, padx=4)
    ttk.Label(controles, text="Cantidad").grid(row=0, column=2, padx=4, sticky="w")
    entrada_cantidad = ttk.Entry(controles, width=12); entrada_cantidad.grid(row=0, column=3, padx=4)
    ttk.Label(controles, text="Precio").grid(row=0, column=4, padx=4, sticky="w")
    entrada_precio = ttk.Entry(controles, width=12); entrada_precio.grid(row=0, column=5, padx=4)
    ttk.Label(controles, text="Categoría").grid(row=1, column=0, padx=4, pady=6, sticky="w")
    entrada_categoria = ttk.Entry(controles, width=30); entrada_categoria.grid(row=1, column=1, padx=4)
    ttk.Label(controles, text="Descripción").grid(row=1, column=2, padx=4, sticky="w")
    entrada_desc = ttk.Entry(controles, width=40); entrada_desc.grid(row=1, column=3, columnspan=3, padx=4)

    tabla = ttk.Treeview(marco, columns=("id","nombre","cantidad","precio","categoria"), show="headings", height=14)
    tabla.heading("id", text="ID")
    tabla.heading("nombre", text="Nombre")
    tabla.heading("cantidad", text="Cantidad")
    tabla.heading("precio", text="Precio")
    tabla.heading("categoria", text="Categoría")
    tabla.column("id", width=50, anchor="center")
    tabla.column("nombre", width=280)
    tabla.column("cantidad", width=90, anchor="center")
    tabla.column("precio", width=90, anchor="center")
    tabla.column("categoria", width=120)
    tabla.pack(fill="both", expand=True, pady=(10,6))

    botones = ttk.Frame(marco)
    botones.pack(fill="x", pady=(6,0))
    ttk.Button(botones, text="Agregar", command=lambda: agregar()).pack(side="left", padx=4)
    ttk.Button(botones, text="Editar", command=lambda: editar()).pack(side="left", padx=4)
    ttk.Button(botones, text="Eliminar", command=lambda: eliminar()).pack(side="left", padx=4)
    ttk.Button(botones, text="Exportar todos a Excel", command=lambda: exportar_todos()).pack(side="right", padx=4)

    def refrescar():
        for r in tabla.get_children(): tabla.delete(r)
        for p in cargar_datos()["productos"]:
            tabla.insert("", "end", values=(p["id"], p["nombre"], p["cantidad"], p["precio"], p.get("categoria","")))

    def agregar():
        nombre = entrada_nombre.get().strip()
        if not nombre:
            messagebox.showwarning("Aviso", "Ingrese nombre")
            return
        try:
            cantidad = float(entrada_cantidad.get() or 0)
            precio = float(entrada_precio.get() or 0)
        except:
            messagebox.showwarning("Aviso", "Cantidad/Precio inválido")
            return
        agregar_producto_diccion(cargar_datos(), nombre, cantidad, precio, entrada_categoria.get(), entrada_desc.get())
        entrada_nombre.delete(0, "end"); entrada_cantidad.delete(0, "end"); entrada_precio.delete(0, "end")
        entrada_categoria.delete(0, "end"); entrada_desc.delete(0, "end")
        refrescar()

    def editar():
        sel = tabla.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Seleccione un producto")
            return
        vals = tabla.item(sel[0])["values"]
        prod_id = vals[0]
        p = next((x for x in cargar_datos()["productos"] if x["id"] == prod_id), None)
        if not p:
            messagebox.showwarning("Aviso", "Producto no encontrado")
            return
        nuevo_nombre = simpledialog.askstring("Editar", "Nombre:", initialvalue=p["nombre"], parent=ventana)
        if nuevo_nombre is None: return
        try:
            nueva_cant = float(simpledialog.askstring("Editar", "Cantidad:", initialvalue=str(p["cantidad"]), parent=ventana) or p["cantidad"])
            nuevo_prec = float(simpledialog.askstring("Editar", "Precio:", initialvalue=str(p["precio"]), parent=ventana) or p["precio"])
        except:
            messagebox.showwarning("Aviso", "Cantidad/Precio inválido")
            return
        nueva_cat = simpledialog.askstring("Editar", "Categoría:", initialvalue=p.get("categoria",""), parent=ventana) or ""
        nueva_desc = simpledialog.askstring("Editar", "Descripción:", initialvalue=p.get("descripcion",""), parent=ventana) or ""
        actualizar_producto_diccion(cargar_datos(), prod_id, nuevo_nombre, nueva_cant, nuevo_prec, nueva_cat, nueva_desc)
        refrescar()

    def eliminar():
        sel = tabla.selection()
        if not sel:
            messagebox.showwarning("Aviso", "Seleccione un producto")
            return
        vals = tabla.item(sel[0])["values"]
        prod_id = vals[0]
        if messagebox.askyesno("Confirmar", "Eliminar producto?"):
            eliminar_producto_diccion(cargar_datos(), prod_id)
            refrescar()

    def exportar_todos():
        productos = cargar_datos()["productos"]
        if not productos:
            messagebox.showwarning("Aviso", "No hay productos")
            return
        productos_sin_usuario = []
        for p in productos:
            copia = {k: v for k, v in p.items() if k != "usuario"}
            productos_sin_usuario.append(copia)
        ruta = exportar_lista_a_excel(productos_sin_usuario, "productos_export", hoja_nombre="productos", metadata={"Generado_por": usuario_actual.get("nombre","")})
        messagebox.showinfo("Exportado", f"Exportado a:\n{ruta}")

    def volver():
        ventana.destroy()
        ventana_principal.deiconify()

    refrescar()
