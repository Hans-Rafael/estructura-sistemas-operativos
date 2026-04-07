"""Microleccion 02 de shutil.

Tema:
- Copiar un archivo en .tmp.

Que vas a observar:
- Creacion de archivo origen.
- Copia con shutil.copy2.

Concepto SO relacionado:
- Operacion de copia en filesystem.
"""

import shutil
from pathlib import Path

print("[Paso 1] Preparando archivos en .tmp...")
tmp_dir = Path(".tmp")
tmp_dir.mkdir(exist_ok=True)

origen = tmp_dir / "shutil_origen.txt"
destino = tmp_dir / "shutil_destino.txt"

origen.write_text("contenido de prueba\n", encoding="utf-8")

print("[Paso 2] Copiando archivo...")
shutil.copy2(origen, destino)

print("[Resultado] Origen:", origen)
print("[Resultado] Destino:", destino)
print("[Resultado] Bytes copiados:", destino.stat().st_size)

print("[Ejercicio] Cambia el nombre del destino y verifica que tambien se copie.")
print("[Pregunta] ¿Que evidencia muestra que la copia se realizo correctamente?")
