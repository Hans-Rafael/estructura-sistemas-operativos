"""Microleccion 02 de mmap.

Tema:
- Escribir en un archivo mapeado en memoria.

Que vas a observar:
- Modificacion de bytes con mmap.
- Persistencia del cambio en disco.

Concepto SO relacionado:
- Escritura sobre region de memoria asociada a archivo.
"""

import mmap
from pathlib import Path

print("[Paso 1] Preparando archivo de prueba en .tmp...")
tmp_dir = Path(".tmp")
tmp_dir.mkdir(exist_ok=True)
archivo_demo = tmp_dir / "mmap_demo_rw.txt"
archivo_demo.write_bytes(b"12345")

print("[Paso 2] Mapeando y modificando bytes...")
with open(archivo_demo, "r+b") as archivo:
    with mmap.mmap(archivo.fileno(), 0) as region:
        region[0:3] = b"abc"
        region.flush()

print("[Paso 3] Leyendo resultado final...")
contenido = archivo_demo.read_bytes().decode("utf-8")
print("[Resultado] Contenido final:", contenido)

print("[Ejercicio] Cambia 'abc' por 'XYZ' y observa el nuevo contenido final.")
print("[Pregunta] ¿Que prueba que el cambio en mmap quedo persistido en disco?")
