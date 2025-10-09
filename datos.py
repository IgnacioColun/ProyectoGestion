import json
import os

ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    if os.path.exists(ARCHIVO_DATOS):
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            return json.load(f)
    else:
        return {"usuarios": {}, "productos": {}}

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def agregar_usuario_diccion(datos, nombre):
    datos["usuarios"][nombre] = {"nombre": nombre}
    guardar_datos(datos)

def agregar_producto_diccion(datos, nombre, cantidad, precio):
    datos["productos"][nombre] = {"cantidad": cantidad, "precio": precio}
    guardar_datos(datos)

def actualizar_producto_diccion(datos, nombre, cantidad, precio):
    if nombre in datos["productos"]:
        datos["productos"][nombre]["cantidad"] = cantidad
        datos["productos"][nombre]["precio"] = precio
        guardar_datos(datos)

def eliminar_producto_diccion(datos, nombre_producto):
    if nombre_producto in datos["productos"]:
        del datos["productos"][nombre_producto]
        guardar_datos(datos)
        return True
    return False

def agregar_asiento_diccion(datos, fecha, hora, descripcion, monto):
    datos["contabilidad"].append({
        "fecha": fecha,
        "hora": hora,
        "descripcion": descripcion,
        "monto": monto
    })
    guardar_datos(datos)

def obtener_lista_productos(datos):
    return [(nombre, info["cantidad"], info["precio"]) for nombre, info in datos["productos"].items()]

def obtener_lista_usuarios(datos):
    return list(datos["usuarios"].keys())
