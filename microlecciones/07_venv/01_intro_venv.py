"""Microleccion 01 de venv.

Tema:
- Verificar si hay un entorno virtual activo.

Que vas a observar:
- Deteccion de VIRTUAL_ENV.
- Comandos para crear/activar el entorno.

Como ejecutar:
- python3 /python/07_venv/01_intro_venv.py

Salida esperada aproximada:
- [Resultado] Entorno virtual detectado. (o no detectado)

Concepto SO relacionado:
- Aislamiento de entorno de ejecucion y variables de entorno.
"""

import os
import platform

print("[Paso 1] Verificando variable VIRTUAL_ENV...")
venv_activo = os.environ.get("VIRTUAL_ENV")

if venv_activo:
    print("[Resultado] Entorno virtual detectado.")
    print("[Resultado] Ruta:", venv_activo)
else:
    print("[Resultado] No hay entorno virtual activo.")
    print("[Guia] Creacion sugerida: python3 -m venv .venv")

    # Indicamos activacion segun shell/sistema.
    if platform.system() == "Windows":
        print("[Guia] Activacion en PowerShell: .venv\\Scripts\\Activate.ps1")
    else:
        print("[Guia] Activacion en Bash: source .venv/bin/activate")

print("[Ejercicio] Activa un venv y vuelve a ejecutar para comparar la salida.")
print("[Pregunta] ¿Que variable de entorno usa el script para detectar venv activo?")

