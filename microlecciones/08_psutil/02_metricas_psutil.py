"""Microleccion 02 de psutil.

Tema:
- Medir CPU y memoria del sistema.

Que vas a observar:
- Porcentaje de CPU.
- Porcentaje de memoria virtual.

Concepto SO relacionado:
- Monitoreo basico de recursos del sistema.
"""

import psutil

print("[Paso 1] Midiendo uso de CPU...")
cpu = psutil.cpu_percent(interval=0.5)

print("[Paso 2] Midiendo uso de memoria...")
memoria = psutil.virtual_memory().percent

print("[Resultado] CPU %:", cpu)
print("[Resultado] Memoria %:", memoria)

print("[Ejercicio] Ejecuta el script 3 veces y anota como cambia CPU %.")
print("[Pregunta] ¿Que representa virtual_memory().percent en terminos simples?")
