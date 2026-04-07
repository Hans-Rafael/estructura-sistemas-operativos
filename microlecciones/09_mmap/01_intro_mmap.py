"""Microleccion 01 de mmap.

Tema:
- Mapeo de un archivo en memoria para lectura rapida.

Que vas a observar:
- Creacion de archivo temporal en .tmp.
- Lectura del contenido mediante mmap.

Como ejecutar:
- python3 /python/09_mmap/01_intro_mmap.py

Salida esperada aproximada:
- [Resultado] Contenido leido con mmap: hola mmap

Concepto SO relacionado:
- Relacion entre archivo en disco y espacio de memoria del proceso.
"""

import mmap
from pathlib import Path

print("[Paso 1] Preparando carpeta temporal .tmp...")
tmp_dir = Path(".tmp")
tmp_dir.mkdir(exist_ok=True)
archivo_demo = tmp_dir / "mmap_demo.txt"

print("[Paso 2] Escribiendo archivo de prueba...")
with open(archivo_demo, "wb") as archivo:
    archivo.write(b"hola mmap")

print("[Paso 3] Mapeando archivo en memoria y leyendo contenido...")
with open(archivo_demo, "r+b") as archivo:
    with mmap.mmap(archivo.fileno(), 0) as region:
        contenido = region.read().decode("utf-8")

print("[Resultado] Contenido leido con mmap:", contenido)

print("[Ejercicio] Cambia el texto 'hola mmap' por otro y verifica la lectura final.")
print("[Pregunta] ¿En que carpeta se crea el archivo de prueba de esta microleccion?")

