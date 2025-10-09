import tkinter as tk
from tkinter import ttk, messagebox
from datos import cargar_datos, agregar_asiento_diccion
from generador_excel import exportar_lista_a_excel

def abrir_contabilidad(usuario_actual, ventana_principal):
    ventana_principal.withdraw()
    ventana = tk.Toplevel()
    ventana.title("Contabilidad")
    ventana.geometry("760x520")
    ventana.config(bg="#f3f4f6")

    marco = ttk.Frame(ventana, padding=12)
    marco.pack(fill="both", expand=True)

    cab = ttk.Frame(marco)
    cab.pack(fill="x")
    ttk.Label(cab, text=f"Usuario activo: {usuario_actual.get('nombre','')}", font=("Arial",11)).pack(side="left")
    ttk.Button(cab, text="Volver al menú", command=lambda: volver()).pack(side="right")

    controles = ttk.Frame(marco)
    controles.pack(fill="x", pady=(8,8))
    ttk.Label(controles, text="Tipo (Ingreso/Gasto)").grid(row=0, column=0, padx=4, sticky="w")
    tipo_cb = ttk.Combobox(controles, values=["Ingreso","Gasto"], state="readonly", width=18); tipo_cb.current(0); tipo_cb.grid(row=0, column=1, padx=4)
    ttk.Label(controles, text="Monto").grid(row=0, column=2, padx=4, sticky="w")
    entrada_monto = ttk.Entry(controles, width=18); entrada_monto.grid(row=0, column=3, padx=4)
    ttk.Label(controles, text="Descripción").grid(row=1, column=0, padx=4, sticky="w")
    entrada_desc = ttk.Entry(controles, width=60); entrada_desc.grid(row=1, column=1, columnspan=3, padx=4, pady=6)

    tabla = ttk.Treeview(marco, columns=("id","tipo","monto","descripcion","usuario","creado_en"), show="headings", height=14)
    tabla.heading("id", text="ID")
    tabla.heading("tipo", text="Tipo")
    tabla.heading("monto", text="Monto")
    tabla.heading("descripcion", text="Descripción")
    tabla.heading("usuario", text="Usuario")
    tabla.heading("creado_en", text="Fecha")
    tabla.column("id", width=50, anchor="center")
    tabla.column("tipo", width=90, anchor="center")
    tabla.column("monto", width=100, anchor="center")
    tabla.column("descripcion", width=240)
    tabla.column("usuario", width=120)
    tabla.column("creado_en", width=140)
    tabla.pack(fill="both", expand=True, pady=(8,6))

    botones = ttk.Frame(marco)
    botones.pack(fill="x", pady=(6,0))
    ttk.Button(botones, text="Agregar", command=lambda: agregar()).pack(side="left", padx=6)
    ttk.Button(botones, text="Exportar a Excel", command=lambda: exportar()).pack(side="right", padx=6)

    def refrescar():
        for r in tabla.get_children(): tabla.delete(r)
        for a in cargar_datos()["contabilidad"]:
            tabla.insert("", "end", values=(a["id"], a["tipo"], a["monto"], a["descripcion"], a.get("usuario",""), a["creado_en"]))

    def agregar():
        tipo = tipo_cb.get()
        try:
            monto = float(entrada_monto.get())
        except:
            messagebox.showwarning("Aviso", "Monto inválido")
            return
        descripcion = entrada_desc.get()
        if not usuario_actual.get("nombre"):
            messagebox.showwarning("Aviso", "Seleccione un usuario")
            return
        agregar_asiento_diccion(cargar_datos(), tipo, monto, descripcion, usuario_actual.get("nombre"))
        entrada_monto.delete(0, "end"); entrada_desc.delete(0, "end")
        refrescar()

    def exportar():
        lista = cargar_datos()["contabilidad"]
        if not lista:
            messagebox.showwarning("Aviso", "No hay registros")
            return
        ruta = exportar_lista_a_excel(lista, "contabilidad", hoja_nombre="contabilidad", metadata={"Generado_por": usuario_actual.get("nombre","")})
        messagebox.showinfo("Exportado", f"Exportado a:\n{ruta}")

    def volver():
        ventana.destroy()
        ventana_principal.deiconify()

    refrescar()
