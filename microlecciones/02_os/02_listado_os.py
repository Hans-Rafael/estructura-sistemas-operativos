"""Microleccion 02 de os.

Tema:
- Listar entradas del directorio de trabajo.

Que vas a observar:
- Listado simple de archivos/carpetas.
- Conteo de elementos.

Concepto SO relacionado:
- Interaccion del proceso con el directorio actual.
"""

import os

print("[Paso 1] Leyendo directorio de trabajo...")
cwd = os.getcwd()

print("[Paso 2] Listando contenido del directorio...")
entradas = os.listdir(cwd)

print("[Resultado] Directorio:", cwd)
print("[Resultado] Cantidad de entradas:", len(entradas)," son: ", entradas)

# Mostramos hasta 10 entradas para mantener salida corta y didactica.
for nombre in entradas[:10]:
    print("[Entrada]", nombre)

print("[Ejercicio] Modifica el script para mostrar 20 entradas en vez de 10.")
for nombre in entradas[:20]:
    print("[Entrada]", nombre)
print("[Pregunta] ¿Que diferencia hay entre os.getcwd() y os.listdir(cwd)?")
print("[Respuesta]","os.getcwd() nos devuelve la direccion al directorio actual de trabajo y \n os.listdir(cwd) nos devuelve lo que hay dentro del actual directorio de trabajo")
######
# Los más usados del módulo os en Python:

# **Navegación y rutas**
# Navegación y rutas: Sirve para moverte entre carpetas (como hacer cd en la terminal) o para construir direcciones de archivos que funcionen tanto en Windows como en Linux.
# Ejemplo: Unir C:\Usuarios con documento.txt.

# os.getcwd() — directorio de trabajo actual

# os.chdir(path) — cambia el directorio de trabajo

# os.path.join(a, b) — une rutas de forma segura (multiplataforma)

# os.path.exists(path) — verifica si existe un archivo/carpeta

# os.path.abspath(path) — convierte a ruta absoluta

# # **Listado y archivos**
# Listado y archivos: Es lo que usas para ver qué hay dentro de una carpeta, crear carpetas nuevas, borrar archivos o renombrarlos.
# Módulo clave: os.listdir() o pathlib.

# os.listdir(path) — lista entradas de un directorio

# os.walk(path) — recorre árbol de directorios recursivamente

# os.makedirs(path) — crea directorios (incluyendo intermedios)

# os.remove(path) — elimina un archivo

# os.rename(src, dst) — renombra archivo o carpeta

# **Variables de entorno **
# Variables de entorno: Son configuraciones "ocultas" del sistema, como contraseñas de bases de datos o el nombre del usuario, que no quieres escribir directamente en el código por seguridad.
# Módulo clave: os.environ

# os.environ.get("HOME") — el que ya usaste, lee variable de entorno sin lanzar error si no existe

# os.environ["HOME"] — igual pero lanza KeyError si no existe

# os.getenv("HOME", "/default") — igual a get pero con sintaxis más corta

# ** Procesos **
# Info del sistema: Sirve para saber qué versión de Python usas, en qué sistema operativo estás (Windows, Mac, etc.) o cuánta memoria RAM queda.
# Módulo clave: sys o platfor

# os.getpid() — PID del proceso actual

# os.getppid() — PID del proceso padre

# os.system(cmd) — ejecuta un comando de shell (mejor usar subprocess hoy en día)

# **Info del sistema**
# Info del sistema: Sirve para saber qué versión de Python usas, en qué sistema operativo estás (Windows, Mac, etc.) o cuánta memoria RAM queda.
# Módulo clave: sys o platform

# os.sep — separador de rutas (/ en Linux, \ en Windows)

# os.name — nombre del SO (posix, nt, etc.)

