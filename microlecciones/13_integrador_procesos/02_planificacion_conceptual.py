"""Microleccion 02 del bloque integrador de procesos.

Tema:
- Planificacion conceptual con Round Robin y quantum.

Que vas a observar:
- Reparto de CPU por turnos.
- Efecto del quantum sobre cantidad de rondas.

Como ejecutar:
- python3 /python/13_integrador_procesos/02_planificacion_conceptual.py

Concepto SO relacionado:
- Planificacion preventiva por quantum (modelo simplificado).
"""

from collections import deque


def simular_round_robin(tareas, quantum):
    cola = deque(tareas)
    linea_tiempo = []
    ciclo = 0

    while cola:
        nombre, restante = cola.popleft()
        uso = min(quantum, restante)
        restante -= uso
        ciclo += 1

        linea_tiempo.append((ciclo, nombre, uso, restante))

        if restante > 0:
            cola.append((nombre, restante))

    return linea_tiempo


def main():
    tareas = [("A", 5), ("B", 3), ("C", 7)]
    quantum = 2

    print("[Paso 1] Tareas (rafagas):", tareas)
    print("[Paso 2] Quantum:", quantum)

    timeline = simular_round_robin(tareas, quantum)

    print("[Paso 3] Linea de tiempo de ejecucion:")
    for ciclo, nombre, uso, restante in timeline:
        print(f"[Ciclo {ciclo}] Proceso {nombre} usa {uso} -> restante {restante}")

    print("[Resultado] Total de ciclos:", len(timeline))
    print("[Ejercicio] Cambia quantum de 2 a 1 y compara la cantidad de ciclos.")
    print("[Pregunta] ¿Que trade-off aparece al usar quantum muy chico?")


if __name__ == "__main__":
    main()
