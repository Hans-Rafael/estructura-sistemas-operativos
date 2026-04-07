"""Microleccion 02 de venv.

Tema:
- Verificar estructura minima de un entorno virtual local.

Que vas a observar:
- Si existe carpeta .venv.
- Ruta de binarios de activacion esperados.

Concepto SO relacionado:
- Estructura de directorios para aislamiento de herramientas.
"""

from pathlib import Path
import platform

print("[Paso 1] Buscando carpeta .venv en el proyecto...")
venv_dir = Path(".venv")

if not venv_dir.exists():
    print("[Resultado] .venv no existe.")
    print("[Guia] Crea el entorno con: python3 -m venv .venv")
else:
    print("[Resultado] .venv detectado:", venv_dir.resolve())

    print("[Paso 2] Verificando script de activacion...")
    if platform.system() == "Windows":
        activador = venv_dir / "Scripts" / "Activate.ps1"
    else:
        activador = venv_dir / "bin" / "activate"

    print("[Resultado] Activador esperado:", activador)
    print("[Resultado] Existe:", activador.exists())

print("[Ejercicio] Crea manualmente .venv y vuelve a ejecutar para comparar salida.")
print("[Pregunta] ¿Que archivo de activacion espera el script en Bash?")
