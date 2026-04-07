"""Microleccion 01 de socket.

Tema:
- Obtener identidad basica de red del host local.

Que vas a observar:
- Nombre del host.
- IP asociada al host.

Como ejecutar:
- python3 /python/10_socket/01_intro_socket.py

Salida esperada aproximada:
- [Resultado] Host: ...
- [Resultado] IP: ...

Concepto SO relacionado:
- Resolucion de nombre de host e interfaces de red.
"""

import socket

print("[Paso 1] Leyendo nombre del host...")
host = socket.gethostname()

print("[Paso 2] Resolviendo una IP asociada al host...")
try:
    ip = socket.gethostbyname(host)
except socket.gaierror:
    print("[Resultado] Host:", host)
    print("[Resultado] No se pudo resolver la IP en este entorno.")
    print("[Guia] Verifica conectividad de red y configuracion DNS.")
else:
    print("[Resultado] Host:", host)
    print("[Resultado] IP:", ip)
    print("[Nota] La IP puede variar segun red/entorno.")

print("[Ejercicio] Ejecuta el script en otra red y compara la IP detectada.")
print("[Pregunta] ¿Por que la IP asociada al host puede cambiar?")

