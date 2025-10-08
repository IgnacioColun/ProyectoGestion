from openpyxl import Workbook
import os

def generar_excel(tipo, datos):
    carpeta = "reportes"
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)

    archivo = f"{carpeta}/{tipo}.xlsx"
    libro = Workbook()
    hoja = libro.active
    hoja.title = tipo.capitalize()

    hoja.append(list(datos.keys()))
    hoja.append(list(datos.values()))

    libro.save(archivo)