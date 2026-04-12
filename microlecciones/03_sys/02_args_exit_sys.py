"""Microleccion 02 de sys.

Tema:
- Argumentos de linea de comandos y salida con codigo de estado.

Que vas a observar:
- Lectura de sys.argv.
- Uso de sys.exit para exito y error.

Como ejecutar:
- python3 /python/03_sys/02_args_exit_sys.py hola

Concepto SO relacionado:
- Parametros de proceso y estado de finalizacion.
"""

import sys

print("[Paso 1] Argumentos recibidos:", sys.argv)

if len(sys.argv) < 2:
    print("[Resultado] Falta argumento de texto.")
    print("[Guia] Ejemplo: python3 /python/03_sys/02_args_exit_sys.py hola")
    sys.exit(2)

texto = sys.argv[1]
print("[Paso 2] Argumento principal:", texto)
print("[Resultado] Ejecucion valida.")
sys.exit(0)
