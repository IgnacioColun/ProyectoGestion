import json
import os
from datetime import datetime

ARCHIVO_DATOS = "datos.json"

def cargar_datos():
    if not os.path.exists(ARCHIVO_DATOS):
        datos = {"usuarios": [], "productos": [], "contabilidad": []}
        guardar_datos(datos)
        return datos
    try:
        with open(ARCHIVO_DATOS, "r", encoding="utf-8") as f:
            datos = json.load(f)
        if not isinstance(datos, dict):
            datos = {"usuarios": [], "productos": [], "contabilidad": []}
        if "usuarios" not in datos or not isinstance(datos["usuarios"], list):
            datos["usuarios"] = []
        if "productos" not in datos or not isinstance(datos["productos"], list):
            datos["productos"] = []
        if "contabilidad" not in datos or not isinstance(datos["contabilidad"], list):
            datos["contabilidad"] = []
        guardar_datos(datos)
        return datos
    except Exception:
        datos = {"usuarios": [], "productos": [], "contabilidad": []}
        guardar_datos(datos)
        return datos

def guardar_datos(datos):
    with open(ARCHIVO_DATOS, "w", encoding="utf-8") as f:
        json.dump(datos, f, indent=4, ensure_ascii=False)

def generar_id_lista(lista):
    if not lista:
        return 1
    try:
        return max(item.get("id", 0) for item in lista) + 1
    except:
        return len(lista) + 1

def agregar_usuario_diccion(datos, nombre):
    nuevo = {"id": generar_id_lista(datos["usuarios"]), "nombre": nombre, "creado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    datos["usuarios"].append(nuevo)
    guardar_datos(datos)
    return nuevo

def agregar_producto_diccion(datos, nombre, cantidad, precio, categoria, descripcion):
    nuevo = {
        "id": generar_id_lista(datos["productos"]),
        "nombre": nombre,
        "cantidad": float(cantidad),
        "precio": float(precio),
        "categoria": categoria,
        "descripcion": descripcion,
        "creado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    datos["productos"].append(nuevo)
    guardar_datos(datos)
    return nuevo

def actualizar_producto_diccion(datos, prod_id, nombre, cantidad, precio, categoria, descripcion):
    for p in datos["productos"]:
        if p.get("id") == prod_id:
            p["nombre"] = nombre
            p["cantidad"] = float(cantidad)
            p["precio"] = float(precio)
            p["categoria"] = categoria
            p["descripcion"] = descripcion
            guardar_datos(datos)
            return p
    return None

def eliminar_producto_diccion(datos, prod_id):
    datos["productos"] = [p for p in datos["productos"] if p.get("id") != prod_id]
    guardar_datos(datos)

def agregar_asiento_diccion(datos, tipo, monto, descripcion, usuario):
    nuevo = {"id": generar_id_lista(datos["contabilidad"]), "tipo": tipo, "monto": float(monto), "descripcion": descripcion, "usuario": usuario, "creado_en": datetime.now().strftime("%Y-%m-%d %H:%M:%S")}
    datos["contabilidad"].append(nuevo)
    guardar_datos(datos)
    return nuevo

def obtener_lista_productos(datos):
    return datos.get("productos", [])

def obtener_lista_usuarios(datos):
    return datos.get("usuarios", [])

def obtener_asientos_contables(datos):
    return datos.get("contabilidad", [])