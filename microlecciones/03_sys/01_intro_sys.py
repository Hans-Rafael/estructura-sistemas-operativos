"""Microleccion 01 de sys.

Tema:
- Informacion basica del interprete y del entorno de ejecucion.

Que vas a observar:
- Version de Python.
- Ruta del ejecutable.
- Plataforma detectada.

Como ejecutar:
- python3 /python/03_sys/01_intro_sys.py

Concepto SO relacionado:
- Dependencia del proceso con el entorno donde corre.
"""

import sys

print("[Paso 1] Leyendo version de Python...")
print("[Resultado] version:", sys.version.split()[0])

print("[Paso 2] Leyendo ejecutable activo...")
print("[Resultado] executable:", sys.executable)

print("[Paso 3] Leyendo plataforma detectada...")
print("[Resultado] platform:", sys.platform)

print("[Ejercicio] Ejecuta el script con otro interprete y compara executable/version.")
print("[Pregunta] ¿Por que es util conocer sys.executable en proyectos reales?")
