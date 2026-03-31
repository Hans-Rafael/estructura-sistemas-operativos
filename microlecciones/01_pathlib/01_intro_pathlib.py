"""Microleccion 01 de pathlib.

Tema:
- Rutas y directorios con objetos Path.

Que vas a observar:
- Como ubicar donde corre el proceso.
- Como validar si una ruta existe y si es directorio.

Como ejecutar:
- python3 /python/01_pathlib/01_intro_pathlib.py

Salida esperada aproximada:
- [Paso 1] Ruta de trabajo detectada
- [Resultado] ...

Concepto SO relacionado:
- Directorio de trabajo actual del proceso.
"""

from pathlib import Path

print("[Paso 1] Tomando la ruta actual del proceso...")
ruta_actual = Path(".").resolve()

print("[Paso 2] Consultando propiedades de la ruta...")
existe = ruta_actual.exists()
es_directorio = ruta_actual.is_dir()

print("[Resultado] Ruta absoluta:", ruta_actual)
print("[Resultado] Existe:", existe)
print("[Resultado] Es directorio:", es_directorio)

print("[Ejercicio] Cambia Path('.') por Path('docs') y compara los resultados de existe/es_directorio.")
print("[Pregunta] ¿Que informacion te da resolve() sobre la ruta actual?")