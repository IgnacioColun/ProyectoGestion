from openpyxl import Workbook
from datetime import datetime
import os

CARPETA_REPORTES = "reportes"

def exportar_lista_a_excel(lista_dicts, nombre_archivo_sugerido, hoja_nombre="datos", metadata=None):
    if not os.path.exists(CARPETA_REPORTES):
        os.makedirs(CARPETA_REPORTES)
    ahora = datetime.now().strftime("%Y%m%d_%H%M%S")
    ruta = os.path.join(CARPETA_REPORTES, f"{nombre_archivo_sugerido}_{ahora}.xlsx")
    wb = Workbook()
    ws = wb.active
    ws.title = hoja_nombre
    if not lista_dicts:
        ws.append(["No hay datos"])
    else:
        claves = list(lista_dicts[0].keys())
        ws.append(claves)
        for item in lista_dicts:
            ws.append([item.get(k, "") for k in claves])
    if metadata:
        ws_meta = wb.create_sheet("metadata")
        for k, v in metadata.items():
            ws_meta.append([k, v])
    wb.save(ruta)
    return ruta