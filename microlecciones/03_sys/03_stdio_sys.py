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
print ("=== Extra practica ===")
# Código ANSI para Rojo: \033[91m
# Código ANSI para Resetear: \033[0m
ROJO = "\033[91m"
RESET = "\033[0m"
def dividir(a, b):
    try:
        resultado = a / b
        # Esto va al canal NORMAL (stdout)
        print(f"Éxito: El resultado es {resultado}")
    except ZeroDivisionError:
        # Esto va al canal de ERROR (stderr)
        sys.stderr.write(f"{ROJO}ERROR CRÍTICO: No puedes dividir entre cero.{RESET}\n")
        # Opcional: cerramos el programa con un código de error (1)
        sys.exit(1)

dividir(10, 0)