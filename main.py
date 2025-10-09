import tkinter as tk
from tkinter import ttk
from usuarios import abrir_usuarios
from inventario import abrir_productos
from contabilidad import abrir_contabilidad
from datos import cargar_datos
from datetime import datetime

usuario_actual = {"nombre": ""}

def iniciar_interfaz():
    raiz = tk.Tk()
    raiz.title("Sistema Empresarial - Gestión Interna")
    raiz.geometry("900x600")
    raiz.config(bg="#eef2f6")

    marco = ttk.Frame(raiz, padding=18)
    marco.pack(fill="both", expand=True)

    titulo = ttk.Label(marco, text="Sistema Empresarial", font=("Arial", 18, "bold"))
    titulo.pack(pady=(4,12))

    resumen = ttk.Frame(marco)
    resumen.pack(fill="x", pady=(6,12))

    lbl_usuarios = ttk.Label(resumen, text="Usuarios: 0", font=("Arial", 12))
    lbl_productos = ttk.Label(resumen, text="Productos: 0", font=("Arial", 12))
    lbl_ingresos = ttk.Label(resumen, text="Total contabilidad: $0.00", font=("Arial", 12))

    lbl_usuarios.pack(side="left", padx=12)
    lbl_productos.pack(side="left", padx=12)
    lbl_ingresos.pack(side="left", padx=12)

    botones = ttk.Frame(marco)
    botones.pack(pady=18)
    ttk.Button(botones, text="Gestionar usuarios", width=22, command=lambda: abrir_usuarios(usuario_actual, raiz)).grid(row=0, column=0, padx=6, pady=6)
    ttk.Button(botones, text="Inventario", width=22, command=lambda: abrir_productos(usuario_actual, raiz)).grid(row=0, column=1, padx=6, pady=6)
    ttk.Button(botones, text="Contabilidad", width=22, command=lambda: abrir_contabilidad(usuario_actual, raiz)).grid(row=0, column=2, padx=6, pady=6)
    ttk.Button(botones, text="Refrescar resumen", width=22, command=lambda: refrescar()).grid(row=1, column=1, padx=6, pady=12)
    ttk.Button(botones, text="Salir", width=22, command=raiz.destroy).grid(row=2, column=1, padx=6, pady=6)

    def refrescar():
        datos = cargar_datos()
        lbl_usuarios.config(text=f"Usuarios: {len(datos.get('usuarios',[]))}")
        lbl_productos.config(text=f"Productos: {len(datos.get('productos',[]))}")
        total = sum([x.get("monto",0) if x.get("tipo")=="Ingreso" else -abs(x.get("monto",0)) for x in datos.get("contabilidad",[])])
        lbl_ingresos.config(text=f"Total contabilidad: ${total:.2f}")

    refrescar()
    raiz.mainloop()

if __name__ == "__main__":
    iniciar_interfaz()
