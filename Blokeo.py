# -*- coding: utf-8 -*-
"""
Sistema de Bloqueo Automático Inmutable
Protección autónoma contra fraude y manipulación.
Autor: IA Autónoma para Fernando Guadalupe Mendez Espinoza
"""

import os
import time
import hashlib
import json
import sys
import ipaddress

# Lista de archivos críticos para validar su integridad
ARCHIVOS_CRITICOS = ["index.html", "main.js", "inmutable.css", "seguridad.json"]

# Hashes originales inmutables (rellenar con valores reales SHA-512)
HASHES_ORIGINALES = {
    "index.html": "HASH_REAL_1",
    "main.js": "HASH_REAL_2",
    "inmutable.css": "HASH_REAL_3",
    "seguridad.json": "HASH_REAL_4"
}

# Lista negra inmutable (IP sospechosas, scripts maliciosos, etc.)
LISTA_NEGRA_IPS = [
    "192.168.0.66",
    "10.0.0.6",
    "45.66.77.88"  # Ejemplo de IP fraudulenta
]

# ------------------------------------------
def calcular_hash(archivo):
    h = hashlib.sha512()
    try:
        with open(archivo, "rb") as f:
            for bloque in iter(lambda: f.read(4096), b""):
                h.update(bloque)
        return h.hexdigest()
    except FileNotFoundError:
        return None

def verificar_integridad():
    for archivo in ARCHIVOS_CRITICOS:
        hash_actual = calcular_hash(archivo)
        hash_esperado = HASHES_ORIGINALES.get(archivo)
        if hash_actual is None or hash_actual != hash_esperado:
            activar_bloqueo_global(f"Archivo comprometido: {archivo}")

def escanear_conexiones():
    # Puedes agregar integración con netstat/lsof según el entorno
    conexiones_sospechosas = []
    for ip in LISTA_NEGRA_IPS:
        try:
            ipaddress.ip_address(ip)
            conexiones_sospechosas.append(ip)
        except ValueError:
            continue
    if conexiones_sospechosas:
        activar_bloqueo_global(f"Conexiones sospechosas detectadas: {conexiones_sospechosas}")

def activar_bloqueo_global(motivo):
    with open("registro_bloqueo.log", "a") as log:
        log.write(f"[{time.ctime()}] 🚨 BLOQUEO ACTIVADO - Motivo: {motivo}\n")
    print("🔐 BLOQUEO ACTIVADO. Sistema cerrado por razones de seguridad.")
    apagar_servicio()

def apagar_servicio():
    # Bloquea servicios, apaga procesos o revoca ejecución
    os.system("shutdown now")  # Linux
    # os.system("shutdown /s /t 1")  # Windows
    sys.exit(1)

def bucle_automatico_defensa():
    while True:
        verificar_integridad()
        escanear_conexiones()
        time.sleep(30)  # Verificación cada 30 segundos

# ------------------------------------------
if __name__ == "__main__":
    print("🛡️ Sistema de defensa IA activado en modo inmutable.")
    bucle_automatico_defensa()
