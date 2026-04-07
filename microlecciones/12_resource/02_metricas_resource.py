"""Microleccion 02 de resource.

Tema:
- Leer memoria maxima residente del proceso.

Que vas a observar:
- Valor ru_maxrss en KB y MB aprox.

Concepto SO relacionado:
- Medicion de consumo de memoria del proceso.
"""

try:
    resource = __import__("resource")
except ImportError:
    print("[Resultado] La libreria 'resource' no esta disponible en este sistema.")
    print("[Guia] Ejecuta esta leccion en Linux/WSL2.")
else:
    print("[Paso 1] Leyendo metricas del proceso actual...")
    uso = resource.getrusage(resource.RUSAGE_SELF)

    # En Linux/WSL, ru_maxrss suele expresarse en KB.
    memoria_kb = uso.ru_maxrss
    memoria_mb = memoria_kb / 1024

    print("[Resultado] Memoria maxima residente (KB):", memoria_kb)
    print("[Resultado] Memoria maxima residente (MB aprox):", round(memoria_mb, 2))
    print("[Resultado] Maximo de RAM usado por este proceso desde que inicio.")

print("[Ejercicio] Ejecuta el script dos veces y compara si ru_maxrss cambia.")
print("[Pregunta] ¿Que significa 'memoria maxima residente' del proceso?")
