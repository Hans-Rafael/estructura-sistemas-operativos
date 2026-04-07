"""Microleccion 01 del bloque integrador de procesos.

Tema:
- Proceso hijo, estados basicos y codigo de salida.

Que vas a observar:
- Estado antes de start (no iniciado).
- Estado durante ejecucion (vivo).
- Estado luego de join (finalizado).

Como ejecutar:
- python3 /python/13_integrador_procesos/01_proceso_estado.py

Concepto SO relacionado:
- Ciclo de vida de proceso: creado, en ejecucion, finalizado.
"""

import multiprocessing as mp
import os
import time


def tarea_hija(segundos):
    print("[Hijo] PID:", os.getpid())
    print("[Hijo] Trabajando", segundos, "segundos...")
    time.sleep(segundos)
    print("[Hijo] Finalizando trabajo.")


def main():
    print("[Paso 1] PID proceso padre:", os.getpid())

    proceso = mp.Process(target=tarea_hija, args=(1.5,))
    print("[Paso 2] Estado inicial is_alive:", proceso.is_alive())

    proceso.start()
    print("[Paso 3] Estado tras start is_alive:", proceso.is_alive())

    proceso.join()
    print("[Paso 4] Estado tras join is_alive:", proceso.is_alive())
    print("[Resultado] exitcode del hijo:", proceso.exitcode)

    print("[Ejercicio] Cambia 1.5 por 0.2 y compara la transicion de estados.")
    print("[Pregunta] ¿Que garantiza join() respecto del proceso hijo?")


if __name__ == "__main__":
    main()
