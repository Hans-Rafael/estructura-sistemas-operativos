"""Microleccion 01 de os.

Tema:
- Datos basicos del sistema y del entorno del proceso.

Que vas a observar:
- Directorio de trabajo actual.
- Variable personal HOME/USERPROFILE segun sistema.

Como ejecutar:
- python3 /python/02_os/01_intro_os.py

Salida esperada aproximada:
- [Resultado] Directorio de trabajo: ...
- [Resultado] HOME/USERPROFILE: ...

Concepto SO relacionado:
- Variables de entorno y contexto de ejecucion del proceso.
"""

import os

print("[Paso 1] Leyendo directorio de trabajo del proceso...")
directorio = os.getcwd()

print("[Paso 2] Buscando directorio personal en variables de entorno...")
# En Linux/WSL2 suele usarse HOME; en Windows suele usarse USERPROFILE.
home = os.environ.get("HOME")
if home is None:
    home = os.environ.get("USERPROFILE")

print("[Resultado] Directorio de trabajo:", directorio)
print("[Resultado] HOME/USERPROFILE:", home)

print("[Ejercicio] Agrega un print para mostrar cuantas variables de entorno hay con len(os.environ).")
print("[Pregunta] ¿Por que HOME y USERPROFILE pueden variar segun sistema?")
