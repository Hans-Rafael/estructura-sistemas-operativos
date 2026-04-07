"""Microleccion 01 de psutil.

Tema:
- Verificar instalacion de psutil.

Que vas a observar:
- Confirmacion de instalacion y version.
- Instruccion de instalacion si falta el modulo.

Como ejecutar:
- python3 /python/08_psutil/01_intro_psutil.py

Salida esperada aproximada:
- [Resultado] psutil esta instalado correctamente.
  o
- [Resultado] psutil no esta instalado.

Concepto SO relacionado:
- Herramientas de observabilidad del sistema.
"""

try:
    import psutil
except ImportError:
    print("[Resultado] psutil no esta instalado.")
    print("[Guia] Instalacion sugerida: python -m pip install psutil")
else:
    print("[Resultado] psutil esta instalado correctamente.")
    print("[Resultado] Version de psutil:", psutil.__version__)

print("[Ejercicio] Desinstala temporalmente psutil en un entorno de prueba y observa la salida alternativa.")
print("[Pregunta] ¿Que comando exacto muestra el script para instalar psutil?")

