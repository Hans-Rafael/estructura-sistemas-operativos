"""Microleccion 01 de shutil.

Tema:
- Medir uso de disco del directorio actual.

Que vas a observar:
- Espacio total, usado y libre.

Como ejecutar:
- python3 /python/06_shutil/01_intro_shutil.py

Salida esperada aproximada:
- [Resultado] Total: ... bytes (... GB)
- [Resultado] Libre: ... bytes (... GB)

Concepto SO relacionado:
- Gestion de almacenamiento en filesystem.
"""

import shutil

print("[Paso 1] Consultando uso de disco en el directorio actual...")
uso = shutil.disk_usage(".")

# Convertimos bytes a GB para una lectura mas humana.
total_gb = uso.total / (1024 ** 3)
usado_gb = uso.used / (1024 ** 3)
libre_gb = uso.free / (1024 ** 3)

print(f"[Resultado] Total: {uso.total} bytes ({total_gb:.2f} GB)")
print(f"[Resultado] Usado: {uso.used} bytes ({usado_gb:.2f} GB)")
print(f"[Resultado] Libre: {uso.free} bytes ({libre_gb:.2f} GB)")

print("[Ejercicio] Calcula tambien los valores en MB y compáralos con GB.")
print("[Pregunta] ¿Que diferencia hay entre espacio usado y libre?")

