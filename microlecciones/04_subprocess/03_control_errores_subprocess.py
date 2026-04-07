"""Microleccion 03 de subprocess.

Tema:
- Control de errores al ejecutar procesos hijos.

Que vas a observar:
- Comando exitoso con returncode 0.
- Comando con error y returncode no-cero.
- Diferencia entre check=False y check=True.
- Error por comando inexistente.

Como ejecutar:
- python3 /python/04_subprocess/03_control_errores_subprocess.py

Concepto SO relacionado:
- Estados de finalizacion de procesos y propagacion de errores.
"""

import subprocess
import sys


print("[Paso 1] Ejecutando un comando exitoso...")
comando_ok = [sys.executable, "-c", "print('ok desde hijo')"]
resultado_ok = subprocess.run(comando_ok, capture_output=True, text=True, check=False)
print("[Resultado] stdout:", resultado_ok.stdout.strip())
print("[Resultado] returncode:", resultado_ok.returncode)

print("[Paso 2] Ejecutando un comando que falla (check=False)...")
comando_falla = [
    sys.executable,
    "-c",
    "import sys; print('error controlado', file=sys.stderr); sys.exit(5)",
]
resultado_falla = subprocess.run(comando_falla, capture_output=True, text=True, check=False)
print("[Resultado] stderr:", resultado_falla.stderr.strip())
print("[Resultado] returncode:", resultado_falla.returncode)

print("[Paso 3] Repitiendo la falla con check=True...")
try:
    subprocess.run(comando_falla, capture_output=True, text=True, check=True)
except subprocess.CalledProcessError as error:
    print("[Resultado] Excepcion capturada: CalledProcessError")
    print("[Resultado] returncode en excepcion:", error.returncode)
    print("[Resultado] stderr en excepcion:", (error.stderr or "").strip())

print("[Paso 4] Probando comando inexistente...")
try:
    subprocess.run(["comando_que_no_existe_12345"], check=False)
except FileNotFoundError:
    print("[Resultado] Excepcion capturada: FileNotFoundError")

print("[Ejercicio] Cambia sys.exit(5) por sys.exit(2) y compara resultados.")
print("[Pregunta] ¿Cuando conviene usar check=True en vez de check=False?")

