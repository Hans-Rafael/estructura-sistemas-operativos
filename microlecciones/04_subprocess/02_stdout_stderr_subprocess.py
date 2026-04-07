"""Microleccion 02 de subprocess.

Tema:
- Capturar stdout, stderr y codigo de retorno.

Que vas a observar:
- Un comando que escribe en salida y error.
- Codigo de retorno no-cero.

Concepto SO relacionado:
- Flujo estandar de procesos (stdout/stderr/returncode).
"""

import subprocess

print("[Paso 1] Ejecutando comando de prueba en shell POSIX...")
comando = ["sh", "-c", "echo salida_ok; echo salida_error 1>&2; exit 3"]

try:
    resultado = subprocess.run(
        comando,
        capture_output=True,
        text=True,
        check=False,
    )
except FileNotFoundError:
    print("[Resultado] No se encontro 'sh'. Ejecuta esta leccion en Linux/WSL2.")
else:
    print("[Resultado] stdout:", resultado.stdout.strip())
    print("[Resultado] stderr:", resultado.stderr.strip())
    print("[Resultado] returncode:", resultado.returncode)

print("[Ejercicio] Cambia 'exit 3' por 'exit 0' y compara returncode.")
print("[Pregunta] ¿Para que te sirve leer stderr ademas de stdout?")
