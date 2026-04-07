"""Microleccion 02 de os.

Tema:
- Listar entradas del directorio de trabajo.

Que vas a observar:
- Listado simple de archivos/carpetas.
- Conteo de elementos.

Concepto SO relacionado:
- Interaccion del proceso con el directorio actual.
"""

import os

print("[Paso 1] Leyendo directorio de trabajo...")
cwd = os.getcwd()

print("[Paso 2] Listando contenido del directorio...")
entradas = os.listdir(cwd)

print("[Resultado] Directorio:", cwd)
print("[Resultado] Cantidad de entradas:", len(entradas))

# Mostramos hasta 10 entradas para mantener salida corta y didactica.
for nombre in entradas[:10]:
    print("[Entrada]", nombre)

print("[Ejercicio] Modifica el script para mostrar 20 entradas en vez de 10.")
print("[Pregunta] ¿Que diferencia hay entre os.getcwd() y os.listdir(cwd)?")
