"""Microleccion 02 de socket.

Tema:
- Crear un socket TCP local y pedir puerto dinamico.

Que vas a observar:
- Bind en localhost.
- Puerto asignado por el sistema (port 0).

Concepto SO relacionado:
- Gestion de puertos por el kernel.
"""

import socket

print("[Paso 1] Creando socket TCP...")
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    print("[Paso 2] Haciendo bind a localhost con puerto 0...")
    servidor.bind(("127.0.0.1", 0))
    host, puerto = servidor.getsockname()
    print("[Resultado] Host local:", host)
    print("[Resultado] Puerto asignado por el sistema:", puerto)
finally:
    servidor.close()
    print("[Paso 3] Socket cerrado.")

print("[Ejercicio] Ejecuta el script 3 veces y compara los puertos asignados.")
print("[Pregunta] ¿Que significa usar puerto 0 en bind()?")
