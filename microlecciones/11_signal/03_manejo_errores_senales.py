"""Microleccion 03 de signal.

Tema:
- Manejo de errores y senales segun entorno.

Que vas a observar:
- Deteccion de senales disponibles por plataforma.
- Manejo de SIGINT con signal.signal.
- Diferencia entre KeyboardInterrupt y otra excepcion.

Como ejecutar:
- python3 /python/11_signal/03_manejo_errores_senales.py

Concepto SO relacionado:
- Variaciones de senales entre sistemas operativos y control robusto del proceso.
"""

import signal
import sys

estado = {"sigint": 0}


def manejar_sigint(signum, _frame):
    estado["sigint"] = estado["sigint"] + 1
    print("[Resultado] SIGINT recibido:", signum)
    print("[Resultado] Total SIGINT:", estado["sigint"])


print("[Paso 1] Detectando entorno de ejecucion...")
print("[Resultado] sys.platform:", sys.platform)
print("[Resultado] SIGINT disponible:", hasattr(signal, "SIGINT"))
print("[Resultado] SIGTERM disponible:", hasattr(signal, "SIGTERM"))

print("[Paso 2] Registrando manejador de SIGINT...")
signal.signal(signal.SIGINT, manejar_sigint)

print("[Paso 3] Simulando SIGINT para validar el manejador...")
signal.raise_signal(signal.SIGINT)

print("[Paso 4] Simulando KeyboardInterrupt y otra excepcion...")
try:
    raise KeyboardInterrupt("interrupcion manual")
except KeyboardInterrupt as error:
    print("[Resultado] Excepcion capturada: KeyboardInterrupt")
    print("[Resultado] Detalle:", error)

try:
    int("no-numero")
except ValueError as error:
    print("[Resultado] Excepcion capturada: ValueError")
    print("[Resultado] Detalle:", error)

print("[Ejercicio] Ejecuta en Linux/WSL2 y en Windows; compara disponibilidad de SIGTERM.")
print("[Pregunta] ¿Por que conviene tratar interrupciones del usuario distinto a errores de parseo?")
