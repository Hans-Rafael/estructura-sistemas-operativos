"""Microleccion 03 del bloque integrador de procesos.

Tema:
- IPC basico con Queue y sincronizacion con Lock.

Que vas a observar:
- Envio de mensajes entre procesos con Queue.
- Seccion critica protegida con Lock para contador compartido.

Como ejecutar:
- python3 /python/13_integrador_procesos/03_ipc_sincronizacion_basica.py

Concepto SO relacionado:
- Comunicacion entre procesos y exclusion mutua.
"""

import multiprocessing as mp
import os


def trabajador(nombre, cola, contador, lock):
    with lock:
        valor_actual = contador.value
        contador.value = valor_actual + 1
        nuevo_valor = contador.value

    mensaje = f"{nombre} (PID {os.getpid()}) incremento contador a {nuevo_valor}"
    cola.put(mensaje)


def main():
    cola = mp.Queue()
    lock = mp.Lock()
    contador = mp.Value("i", 0)

    print("[Paso 1] Lanzando procesos trabajadores...")
    procesos = [
        mp.Process(target=trabajador, args=("P1", cola, contador, lock)),
        mp.Process(target=trabajador, args=("P2", cola, contador, lock)),
        mp.Process(target=trabajador, args=("P3", cola, contador, lock)),
    ]

    for proceso in procesos:
        proceso.start()

    for proceso in procesos:
        proceso.join()

    print("[Paso 2] Leyendo mensajes IPC desde Queue...")
    while not cola.empty():
        print("[Resultado]", cola.get())

    print("[Resultado] Valor final del contador compartido:", contador.value)
    print("[Ejercicio] Quita temporalmente el lock y observa si el resultado siempre coincide.")
    print("[Pregunta] ¿Por que Queue y Lock resuelven problemas distintos?")


if __name__ == "__main__":
    main()
