"""Microleccion 03 de sys.

Tema:
- Flujo estandar con stdout y stderr.

Que vas a observar:
- Escritura normal por stdout.
- Escritura de error por stderr.

Como ejecutar:
- python3 /python/03_sys/03_stdio_sys.py

Concepto SO relacionado:
- Canales de salida del proceso para logging y diagnostico.
"""

import sys

print("[Paso 1] Mensaje por stdout")
print("[Resultado] stdout: operacion informativa")

print("[Paso 2] Mensaje por stderr", file=sys.stderr)
print("[Resultado] stderr: operacion de diagnostico", file=sys.stderr)

print("[Ejercicio] Redirige stderr a archivo y compara con stdout.")
print("[Pregunta] ¿Cuando conviene separar stdout y stderr?")
