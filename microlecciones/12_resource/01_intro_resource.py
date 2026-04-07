"""Microleccion 01 de resource.

Tema:
- Detectar si WSL2 esta disponible y mostrar version.

Que vas a observar:
- Deteccion de WSL2 en ejecucion.
- Consulta de version desde Windows cuando aplica.

Como ejecutar:
- python3 /python/12_resource/01_intro_resource.py

Salida esperada aproximada:
- [Resultado] WSL2 detectado.
  o
- [Resultado] WSL2 no detectado. + guia de instalacion

Concepto SO relacionado:
- Capa de compatibilidad Linux sobre Windows (WSL).
"""

import os
import platform
import subprocess


def detectar_wsl_en_ejecucion():
    """Devuelve WSL2, WSL1 o None segun el kernel activo."""
    ruta_release = "/proc/sys/kernel/osrelease"
    if not os.path.exists(ruta_release):
        return None

    with open(ruta_release, "r", encoding="utf-8") as archivo:
        release = archivo.read().lower()

    if "microsoft" in release and "wsl2" in release:
        return "WSL2"
    if "microsoft" in release:
        return "WSL1"
    return None


def version_wsl_desde_windows():
    """Intenta leer la version de WSL desde wsl.exe --version."""
    try:
        resultado = subprocess.run(
            ["wsl.exe", "--version"],
            capture_output=True,
            text=True,
            check=False,
        )
    except FileNotFoundError:
        return None

    if resultado.returncode != 0:
        return None

    salida = resultado.stdout.replace("\x00", "")
    lineas = [linea.strip() for linea in salida.splitlines() if linea.strip()]
    if not lineas:
        return "WSL detectado, pero no se pudo extraer version"

    for linea in lineas:
        texto = linea.lower()
        if "version" in texto or "vers" in texto:
            return linea

    return lineas[0]


print("[Paso 1] Verificando si estamos dentro de WSL...")
wsl_actual = detectar_wsl_en_ejecucion()

if wsl_actual == "WSL2":
    print("[Resultado] WSL2 detectado.")
    print("[Resultado] Version del kernel:", platform.release())
elif wsl_actual == "WSL1":
    print("[Resultado] WSL1 detectado (no es WSL2).")
    print("[Resultado] Version del kernel:", platform.release())
else:
    print("[Paso 2] No estamos dentro de WSL; revisando desde Windows...")
    if platform.system() == "Windows":
        version = version_wsl_desde_windows()
        if version is not None:
            print("[Resultado] WSL detectado en Windows.")
            print("[Resultado] Version:", version)
        else:
            print("[Resultado] WSL2 no detectado.")
            print("[Guia] Instalacion sugerida (PowerShell como admin): wsl --install")
            print("[Guia] Luego reiniciar y verificar con: wsl --status")
    else:
        print("[Resultado] WSL2 no detectado en este entorno.")
        print("[Guia] Si usas Windows, instalalo con: wsl --install")

print("[Ejercicio] Ejecuta este script en Windows y luego dentro de WSL2; compara salida.")
print("[Pregunta] ¿Que comando se sugiere para instalar WSL2 si no se detecta?")

