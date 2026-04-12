"""Microleccion 01 de os.

Tema:
- Datos basicos del sistema y del entorno del proceso.

Que vas a observar:
- Directorio de trabajo actual.
- Variable personal HOME/USERPROFILE segun sistema.

Como ejecutar:
- python3 /python/02_os/01_intro_os.py

Salida esperada aproximada:
- [Resultado] Directorio de trabajo: ...
- [Resultado] HOME/USERPROFILE: ...

Concepto SO relacionado:
- Variables de entorno y contexto de ejecucion del proceso.
"""

import os

print("[Paso 1] Leyendo directorio de trabajo del proceso...")
directorio = os.getcwd()

print("[Paso 2] Buscando directorio personal en variables de entorno...")
# En Linux/WSL2 suele usarse HOME; en Windows suele usarse USERPROFILE.
home = os.environ.get("HOME")
if home is None:
    home = os.environ.get("USERPROFILE")

print("[Resultado] Directorio de trabajo:", directorio)
print("[Resultado] HOME/USERPROFILE:", home)

print("[Ejercicio] Agrega un print para mostrar cuantas variables de entorno hay con len(os.environ).\n")
print(f"En os.environ la cantidad de variables que hay son: {len(os.environ)}")
print("[Pregunta] ¿Por que HOME y USERPROFILE pueden variar segun sistema?")
print(f"Porque cada SO tiene su propia convención para el directorio del usuario:")
print(f"Linux/macOS usa HOME  /home/hans o /Users/hans")
print(r"Windows usa USERPROFILE  C:\Users\hans")
print(f"En Linux se puede usar el comando 'echo $HOME' para ver el valor de la variable de entorno HOME")

print("===========Extra practicas==========")
# --- PROCESOS (Limpiar pantalla) ---
# Esta línea detecta tu sistema y ejecuta el comando de "limpiar terminal"
# (Es una acción, no devuelve texto, por eso no lleva print afuera)
# os.system('cls' if os.name == 'nt' else 'clear')
print("La pantalla se limpio antes de mostrar esto! ")
# ---  NAVEGACIÓN Y RUTAS ---
# Guardamos la ruta actual en una variable
original = os.getcwd()
print(f"La ruta original es: {original}")
# Acción: Subir un nivel (salir de la carpeta actual)
os.chdir('..')
print(f"Ahora que subo un nivel estoy en: {os.getcwd()}")
# para regresar a la carpeta
print(
    f"regreso a la carpeta con os.chdir(original) o os.chdir('../')  : {os.chdir('../')} {os.getcwd()}")
# ---  LISTADO Y ARCHIVOS ---
# Ruta donde está este archivo (main.py)
ruta_script = os.path.dirname(os.path.abspath(__file__))
# Creamos una carpeta real en el disco duro
nombre_carpeta = "carpeta_temporal"
ruta_completa = os.path.join(ruta_script, nombre_carpeta)
if not os.path.exists(ruta_completa):  # reviso si ya no existe
    os.mkdir(ruta_completa)                # Acción: Crear la carpeta física
    print(f"Se creo la carpeta: {ruta_completa}")
# Obtenemos la lista de archivos "aquí mismo"
archivos = os.listdir(ruta_script)
print(f"Los archivos en esta carpeta son: {archivos}")
# --------- VARIABLES DE ENTORNO ---
# Consultamos una variable del sistema (el PATH)
rutas_sistema = os.environ.get("PATH")
# Separamos las rutas por el separador del sistema
rutas = rutas_sistema.split(":")
cantidad_rutas = len(rutas)
print(
    f"Las rutas del sistema son,{cantidad_rutas} y estas son: {rutas_sistema}")

# Creamos una variable de entorno "fantasma" que solo vive en este programa
os.environ['MI_VARIABLE'] = 'PythonEsGenial'
print(f"Variable creada: {os.environ['MI_VARIABLE']}")
