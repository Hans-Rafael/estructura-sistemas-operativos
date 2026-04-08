"""Microleccion 01 de sys.

Tema:
- Informacion basica del interprete y del entorno de ejecucion.

Que vas a observar:
- Version de Python.
- Ruta del ejecutable.
- Plataforma detectada.

Como ejecutar:
- python3 /python/03_sys/01_intro_sys.py

Concepto SO relacionado:
- Dependencia del proceso con el entorno donde corre.
"""

import sys

print("[Paso 1] Leyendo version de Python...")
print("[Resultado] version:", sys.version.split()[0])# remueve fecha con split y muestro pocicion 0

print("[Paso 2] Leyendo ejecutable activo...")
print("[Resultado] executable:", sys.executable)

print("[Paso 3] Leyendo plataforma detectada...")
print("[Resultado] platform:", sys.platform)

print("[Ejercicio] Ejecuta el script con otro interprete y compara executable/version.")
print("[Respuesta] Desde un entorno virtual la ruta mostrada es diferente")
print("[Pregunta] ¿Por que es util conocer sys.executable en proyectos reales?")
print("[Respuesta] como comentario")
'''

La función sys.executable devuelve la ruta completa al intérprete de Python que está actualmente en uso. 
Esto es útil en proyectos reales porque permite:

1. **Automatización y Scripts**: Saber exactamente qué intérprete se está utilizando puede ser crucial para scripts que necesitan ejecutar otros programas o scripts, asegurándose de usar el mismo intérprete.

2. **Entornos Virtuales**: En entornos virtuales, esta información ayuda a confirmar que se está usando el intérprete correcto del entorno virtual en lugar del sistema global.

3. **Depuración y Diagnóstico**: Puede ayudar en la depuración para verificar que el código se está ejecutando en el entorno esperado.

4. **Gestión de Aplicaciones**: En aplicaciones más grandes, puede ser necesario asegurar que ciertos componentes se ejecuten con el intérprete correcto, especialmente cuando hay múltiples versiones de Python instaladas.

5. **Scripts de Instalación o Configuración**: Al crear scripts de instalación o configuración, es importante asegurar que se usen las rutas correctas y el intérprete adecuado.

En resumen, sys.executable proporciona una forma de obtener información sobre el entorno de ejecución, lo cual es clave para garantizar que los scripts y aplicaciones funcionen correctamente en diferentes entornos.

'''

print("===== Extra practicas =============")
# ---  INFO DEL SISTEMA ---
# # Identifica si es Windows (win32) o Linux/Mac
print(f"Sistema operativo: {sys.platform}")
# Muestra la versión técnica instalada
print(f"Versión de Python: {sys.version}")
print("-" * 30)
# --- PROCESOS (Cerrar) ---
sys.exit() # Detiene todo inmediatamente. 
#Nada de lo que escribas abajo se ejecutará.