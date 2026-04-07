"""Microleccion 01 de signal.

Tema:
- Capturar una senal SIGINT en un proceso Python.

Que vas a observar:
- Registro de manejador con signal.signal(...).
- Prueba de senal con signal.raise_signal(...).

Como ejecutar:
- python3 /python/11_signal/01_intro_signal.py

Salida esperada aproximada:
- [Resultado] Senal recibida: 2
- [Resultado] Total de interrupciones: 1

Concepto SO relacionado:
- Interrupcion/senal (evento externo) vs excepcion (error interno).
"""

import signal

# Diccionario para guardar estado sin usar variables globales sueltas.
estado = {"interrupciones": 0}


def al_interrumpir(signum, _frame):
    """Manejador para SIGINT (Ctrl+C)."""
    estado["interrupciones"] = estado["interrupciones"] + 1
    print("[Resultado] Senal recibida:", signum)
    print("[Resultado] Total de interrupciones:", estado["interrupciones"])


print("[Paso 1] Registrando manejador de SIGINT...")
signal.signal(signal.SIGINT, al_interrumpir)

print("[Guia] Escribi PROBAR para simular SIGINT o SALIR para terminar.")
print("[Guia] PROBAR equivale a simular Ctrl+C dentro del proceso.")

while True:
    comando = input("Comando: ").strip().upper()

    if comando == "PROBAR":
        # Simulamos Ctrl+C enviando SIGINT al proceso actual.
        signal.raise_signal(signal.SIGINT)
    elif comando == "SALIR":
        print("[Resultado] Fin de la microleccion.")
        break
    else:
        print("[Guia] Comando no valido. Usa PROBAR o SALIR.")

print("[Ejercicio] Ejecuta PROBAR dos veces y verifica el contador de interrupciones.")
print("[Pregunta] ¿Cual es la diferencia entre una senal y una excepcion?")

