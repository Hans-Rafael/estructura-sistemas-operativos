"""Microleccion 02 de signal.

Tema:
- Diferenciar senal (interrupcion) y excepcion.

Que vas a observar:
- Llegada de SIGINT al proceso.
- Manejo de ZeroDivisionError como excepcion.

Concepto SO relacionado:
- Evento externo (senal) vs error interno del codigo (excepcion).
"""

import signal

estado = {"senal_recibida": False}


def manejar_sigint(signum, _frame):
    estado["senal_recibida"] = True
    print("[Resultado] Senal recibida:", signum)


print("[Paso 1] Registrando manejador SIGINT...")
signal.signal(signal.SIGINT, manejar_sigint)

print("[Paso 2] Simulando SIGINT con raise_signal...")
signal.raise_signal(signal.SIGINT)
print("[Resultado] Estado senal_recibida:", estado["senal_recibida"])

print("[Paso 3] Provocando excepcion de ejemplo...")
try:
    _ = 10 / 0
except ZeroDivisionError:
    print("[Resultado] Excepcion capturada: ZeroDivisionError")

print("[Ejercicio] Comenta temporalmente el bloque try/except y observa la diferencia.")
print("[Pregunta] ¿Cual es la diferencia esencial entre senal y excepcion?")
