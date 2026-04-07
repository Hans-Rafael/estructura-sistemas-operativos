"""Microleccion 01 de subprocess.

Tema:
- Ejecutar un comando del sistema desde Python.

Que vas a observar:
- Salida estandar de un comando.
- Codigo de retorno del proceso hijo.

Como ejecutar:
- python3 /python/04_subprocess/01_intro_subprocess.py

Salida esperada aproximada:
- [Resultado] Salida del comando: hola desde subprocess
- [Resultado] Codigo de retorno: 0

Concepto SO relacionado:
- Creacion y finalizacion de procesos.
"""

import subprocess

comando = ["echo", "hola desde subprocess"]
print("[Paso 1] Ejecutando comando:", comando)

# check=False deja explicito que no lanzamos excepcion por retorno no-cero.
resultado = subprocess.run(
    comando,
    capture_output=True,
    text=True,
    check=False,
)

print("[Resultado] Salida del comando:", resultado.stdout.strip())
print("[Resultado] Codigo de retorno:", resultado.returncode)

print("[Ejercicio] Cambia el texto del comando echo y verifica la nueva salida.")
print("[Pregunta] ¿Que indica un returncode igual a 0?")

