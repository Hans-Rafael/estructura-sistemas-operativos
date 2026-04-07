"""Microleccion 03 de socket.

Tema:
- Cliente-servidor TCP local completo y prueba de puerto.

Que vas a observar:
- Servidor en localhost con puerto dinamico.
- Conexion cliente-servidor y envio de datos.
- Verificacion de puerto abierto/cerrado.

Como ejecutar:
- python3 /python/10_socket/03_cliente_servidor_local.py

Concepto SO relacionado:
- Gestion de sockets y puertos TCP por el kernel.
"""

import socket
import threading


def servidor_local(estado):
    servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    servidor.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)

    try:
        servidor.bind(("127.0.0.1", 0))
        servidor.listen(1)
        _, puerto = servidor.getsockname()

        estado["puerto"] = puerto
        estado["listo"].set()

        conexion, direccion = servidor.accept()
        with conexion:
            print("[Servidor] Conexion aceptada desde:", direccion)
            mensaje = conexion.recv(1024).decode("utf-8")
            print("[Servidor] Mensaje recibido:", mensaje)
            conexion.sendall(b"pong")
            print("[Servidor] Respuesta enviada: pong")
    finally:
        servidor.close()


def puerto_abierto(host, puerto):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as verificador:
        verificador.settimeout(1)
        return verificador.connect_ex((host, puerto)) == 0


estado = {"listo": threading.Event(), "puerto": None}

print("[Paso 1] Iniciando servidor TCP local en hilo...")
hilo_servidor = threading.Thread(target=servidor_local, args=(estado,), daemon=True)
hilo_servidor.start()

if not estado["listo"].wait(timeout=2):
    print("[Resultado] El servidor no estuvo listo a tiempo.")
    print("[Guia] Reintenta la ejecucion para validar el entorno local.")
else:
    host = "127.0.0.1"
    puerto = estado["puerto"]
    print("[Resultado] Servidor escuchando en:", host, puerto)

    print("[Paso 2] Conectando cliente y enviando 'ping'...")
    with socket.create_connection((host, puerto), timeout=2) as cliente:
        cliente.sendall(b"ping")
        respuesta = cliente.recv(1024).decode("utf-8")

    print("[Resultado] Respuesta del servidor:", respuesta)
    print("[Resultado] Puerto estuvo abierto durante la conexion:", respuesta == "pong")

    hilo_servidor.join(timeout=2)

    print("[Paso 3] Verificando que el puerto ya no acepta conexiones...")
    abierto_despues = puerto_abierto(host, puerto)
    print("[Resultado] Puerto abierto luego del cierre:", abierto_despues)

print("[Ejercicio] Cambia 'pong' por 'ok' en el servidor y valida la respuesta del cliente.")
print("[Pregunta] ¿Que ventaja tiene usar puerto 0 en laboratorio local?")

