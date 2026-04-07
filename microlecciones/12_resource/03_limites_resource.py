"""Microleccion 03 de resource.

Tema:
- Medicion comparativa de memoria y lectura de limites del proceso.

Que vas a observar:
- Cambio de ru_maxrss antes y despues de reservar memoria.
- Lectura de un limite del proceso (soft/hard) si el entorno lo permite.

Como ejecutar:
- python3 /python/12_resource/03_limites_resource.py

Concepto SO relacionado:
- Limites de recursos y observabilidad de consumo de memoria por proceso.
"""

import gc


def a_mb_desde_kb(valor_kb):
    return round(valor_kb / 1024, 2)


try:
    resource = __import__("resource")
except ImportError:
    print("[Resultado] La libreria 'resource' no esta disponible en este sistema.")
    print("[Guia] Ejecuta esta leccion en Linux/WSL2 para ver limites reales.")
else:
    print("[Paso 1] Midiendo ru_maxrss inicial...")
    uso_inicial = resource.getrusage(resource.RUSAGE_SELF)
    rss_inicial_kb = uso_inicial.ru_maxrss
    print("[Resultado] ru_maxrss inicial (KB):", rss_inicial_kb)
    print("[Resultado] ru_maxrss inicial (MB aprox):", a_mb_desde_kb(rss_inicial_kb))

    print("[Paso 2] Reservando memoria en el proceso...")
    bloque = bytearray(20 * 1024 * 1024)  # 20 MB aprox
    for indice in range(0, len(bloque), 4096):
        bloque[indice] = 1

    uso_despues = resource.getrusage(resource.RUSAGE_SELF)
    rss_despues_kb = uso_despues.ru_maxrss
    delta_kb = rss_despues_kb - rss_inicial_kb

    print("[Resultado] ru_maxrss despues (KB):", rss_despues_kb)
    print("[Resultado] ru_maxrss despues (MB aprox):", a_mb_desde_kb(rss_despues_kb))
    print("[Resultado] Delta de ru_maxrss (KB):", delta_kb)

    del bloque
    gc.collect()

    print("[Paso 3] Leyendo limites de recursos del proceso...")
    if hasattr(resource, "RLIMIT_AS"):
        soft, hard = resource.getrlimit(resource.RLIMIT_AS)
        print("[Resultado] RLIMIT_AS soft/hard:", soft, hard)
    elif hasattr(resource, "RLIMIT_DATA"):
        soft, hard = resource.getrlimit(resource.RLIMIT_DATA)
        print("[Resultado] RLIMIT_DATA soft/hard:", soft, hard)
    else:
        print("[Resultado] No hay RLIMIT_AS/RLIMIT_DATA disponibles en este entorno.")

print("[Ejercicio] Cambia 20 MB por 40 MB y compara el delta de ru_maxrss.")
print("[Pregunta] ¿Que diferencia hay entre medir consumo y consultar limites del proceso?")
