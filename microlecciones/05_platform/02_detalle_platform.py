"""Microleccion 02 de platform.

Tema:
- Obtener mas detalles de la plataforma.

Que vas a observar:
- Arquitectura, maquina y procesador.

Concepto SO relacionado:
- Caracteristicas del entorno donde corre el proceso.
"""

import platform

print("[Paso 1] Consultando datos extendidos de plataforma...")
print("[Resultado] machine:", platform.machine())
print("[Resultado] processor:", platform.processor())
print("[Resultado] platform:", platform.platform())

print("[Ejercicio] Ejecuta el mismo script en Windows y en WSL2 y compara resultados.")
print("[Pregunta] ¿Por que platform.platform() puede ayudarte en problemas de compatibilidad?")
