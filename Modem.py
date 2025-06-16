# -*- coding: utf-8 -*-
"""
Sistema Inmueble Autónomo de Protección
Autor: IA Autónoma para Fernando Guadalupe Mendez Espinoza
Versión: 1.0.0
"""

import hashlib
import os
import time
import sys
import shutil

ARCHIVOS_CRITICOS = [
    "index.html",
    "main.js",
    "inmutable.css",
    "seguridad.json"
]

HASHES_ORIGINALES = {
    "index.html": "INSERTE_HASH_SHA512_REAL",
    "main.js": "INSERTE_HASH_SHA512_REAL",
    "inmutable.css": "INSERTE_HASH_SHA512_REAL",
    "seguridad.json": "INSERTE_HASH_SHA512_REAL"
}

def calcular_hash(filepath):
    sha512 = hashlib.sha512()
    try:
        with open(filepath, "rb") as f:
            while True:
                chunk = f.read(8192)
                if not chunk:
                    break
                sha512.update(chunk)
        return sha512.hexdigest()
    except FileNotFoundError:
        return "Archivo no encontrado"

def verificar_integridad():
    print("🛡️ Verificando integridad...")
    for archivo in ARCHIVOS_CRITICOS:
        hash_actual = calcular_hash(archivo)
        if hash_actual != HASHES_ORIGINALES.get(archivo):
            print(f"🚨 Archivo manipulado: {archivo}")
            log_y_autodestruccion(archivo)
        else:
            print(f"✅ {archivo} verificado correctamente.")

def log_y_autodestruccion(archivo):
    with open("log_alerta.txt", "a") as log:
        log.write(f"[{time.ctime()}] Manipulación detectada en: {archivo}\n")

    print("❌ Integridad comprometida. Cerrando el sistema...")
    time.sleep(2)
    sys.exit(1)

def bucle_eterno_proteccion():
    while True:
        verificar_integridad()
        time.sleep(60)  # Verifica cada 60 segundos

def crear_backup_local():
    destino = "backup_inmutable"
    if not os.path.exists(destino):
        os.makedirs(destino)
    for archivo in ARCHIVOS_CRITICOS:
        if os.path.exists(archivo):
            shutil.copy2(archivo, os.path.join(destino, archivo))
    print("🗂️ Copia de seguridad local realizada.")

if __name__ == "__main__":
    print("🔒 Sistema Inmueble ejecutándose...")
    crear_backup_local()
    bucle_eterno_proteccion()
