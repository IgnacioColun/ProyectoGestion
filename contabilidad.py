import tkinter as tk
from tkinter import messagebox
from generador_excel import generar_excel

def abrir_contabilidad():
    ventana = tk.Toplevel()
    ventana.title("Contabilidad")
    ventana.geometry("500x400")
    ventana.config(bg="#f8f8f8")

    tk.Label(ventana, text="Fecha:", bg="#f8f8f8").pack()
    entrada_fecha = tk.Entry(ventana)
    entrada_fecha.pack()

    tk.Label(ventana, text="Hora:", bg="#f8f8f8").pack()
    entrada_hora = tk.Entry(ventana)
    entrada_hora.pack()

    tk.Label(ventana, text="Usuario:", bg="#f8f8f8").pack()
    entrada_usuario = tk.Entry(ventana)
    entrada_usuario.pack()

    tk.Label(ventana, text="Monto Ingresos:", bg="#f8f8f8").pack()
    entrada_ingresos = tk.Entry(ventana)
    entrada_ingresos.pack()

    tk.Label(ventana, text="Monto Gastos:", bg="#f8f8f8").pack()
    entrada_gastos = tk.Entry(ventana)
    entrada_gastos.pack()
    
    def guardar():
        datos = {
            "Fecha": entrada_fecha.get(), 
            "Hora": entrada_hora.get(),
            "Usuario": entrada_usuario.get(),
            "Ingreso": entrada_ingresos.get(),
            "Gastos": entrada_gastos.get()
        }
        generar_excel("Contabilidad", datos)
        messagebox.showinfo("Exito", "Archivo de contabilidad generado correctamente")
        
    boton_guardar = tk.Button(ventana, text="Generar hoja de Excel", command=guardar)
    boton_guardar.pack(pady=20)