"""Microleccion 01 de platform.

Tema:
- Identificar plataforma de ejecucion.

Que vas a observar:
- Nombre del sistema operativo.
- Version del kernel/sistema.

Como ejecutar:
- python3 /python/05_platform/01_intro_platform.py

Salida esperada aproximada:
- [Resultado] Sistema: Linux
- [Resultado] Version: ...

Concepto SO relacionado:
- Compatibilidad de software segun plataforma.
"""

import platform

print("[Paso 1] Consultando datos de plataforma...")
sistema = platform.system()
version = platform.release()

print("[Resultado] Sistema:", sistema)
print("[Resultado] Version:", version)

print("[Ejercicio] Ejecuta el script en otro entorno (Windows/WSL2) y compara system/release.")
print("[Pregunta] ¿Para que sirve conocer platform.system() antes de ejecutar comandos?")

