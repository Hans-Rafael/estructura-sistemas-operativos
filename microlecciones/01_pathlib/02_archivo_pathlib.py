"""Microleccion 02 de pathlib.

Tema:
- Crear y leer un archivo con Path.

Que vas a observar:
- Uso de carpeta .tmp para pruebas.
- Escritura y lectura de texto con pathlib.

Concepto SO relacionado:
- Operaciones basicas de filesystem desde un proceso.
"""
# Path → crear, leer, escribir, renombrar, eliminar un archivo o directorio
# Libreria : shutil ->  Copia archivo, mueve archivo o carpeta, elimina carpeta, copia carpeta entera, crea un zip/tar, devuelve espacio total, usado y libre del disco
from pathlib import Path

print("[Paso 1] Preparando carpeta temporal .tmp...")
# debo crear el objeto primero para poder llamar al mkdir
tmp_dir = Path(".tmp")
# Si no existe → lo crea. Si ya existe → no hace nada (no lanza error).
tmp_dir.mkdir(exist_ok=True)

# agredo el archivo a un objeto que guarda el file
archivo = tmp_dir / "pathlib_demo.txt"

print("[Paso 2] Escribiendo archivo de ejemplo...")
archivo.write_text("hola desde pathlib\n", encoding="utf-8")

print("[Paso 3] Leyendo archivo...")
# no olvidar strip para para quitar espacios en blanco al final y al principio
contenido = archivo.read_text(encoding="utf-8").strip()

print("[Resultado] Archivo creado:", archivo)
print("[Resultado] Contenido leido:", contenido)

print(f"\n[Ejercicio] Cambia el nombre del archivo a pathlib_demo_2.txt y vuelve a ejecutar.")
print("[Pregunta] ¿Que ventaja practica te da usar Path en lugar de concatenar rutas como texto?")
# seguridad y la compatibilidad. pues en win usa\ y en linux y mac /
# me evito tener que usar (open, write, close)
# al no tener que concatenar evito poner por error barras / de mas
archivo = tmp_dir / "pathlib_demo_2.txt"
archivo.write_text("hola con pathlib file2 created \n", encoding="utf-8")
print("[Paso 3] Leyendo archivo...")
contenido = archivo.read_text(encoding="utf-8").strip()
print("[Resultado] Archivo creado:", archivo)
print("[Resultado] Contenido leido:", contenido)

print(f"\n =======================================================\n")
print(f"   Practica del codigo Reescrito por mi\n")
print(f" =======================================================\n")
# archivo nuevo que se renombrara
archivox = tmp_dir / "sera_renombrado.txt"
archivox.write_text(
    "hola es contenido de un archivo a ser renombrado \n", encoding="utf-8")
contenido_leido = archivox.read_text(encoding="utf-8").strip()
print(f"contenido del archivo  sera_renombrado.txt : \n {contenido_leido}")
# Renombrando un archivo.
a_n = archivox.rename(tmp_dir / "renombrado_correctamente.txt")
print(f"archivo renombrado : {a_n}")
# crear archivo sera borrado en el directorio temp.
archivox = tmp_dir / "a_ser_borrado.txt"
archivox.write_text(
    "hola es contenido de un archivo a ser Borrado \n", encoding="utf-8")
print("**archivox** borrado, existe aun?:", archivox.exists())
archivox.unlink(missing_ok=True)  # archivo borrado
print("**archivox** borrado, existe aun?:", archivox.exists())
# reescribiendo el codigo para practicar
ruta_donde_estoy = Path(".").resolve()
print(f"la ruta donde estoy ahora es: \n {ruta_donde_estoy}")
tmp_dir2 = Path(".temp")  # creo el objeto que tiene la direcion a temp
tmp_dir2.mkdir(exist_ok=True)  # creo el directorio temporal
# compruebo si el directorio existe para ver si se creo efectivamente.
existe = tmp_dir2.exists()
print(f"el directorio temp existe, se creo ?: {existe}")  # (la carpeta)
ruta_a_temp = Path(".temp").resolve()  # direccion absoluta al directorio temp
print(f"El nuevo directorio es: {tmp_dir2}")
print(f"la ruta absoluta  a temp es:    \n {ruta_a_temp}")
es_directorio = ruta_a_temp.is_dir()
print(f" ruta a temp es a un directorio ?: {es_directorio}")
print(f" la ruta temp existe? : {ruta_a_temp.exists()} ")
# creo un archivo de texto dentro de temp
text_file = tmp_dir2 / "pathlib_demo_3.txt"
# escribo en el archivo
text_file.write_text(
    "Hola este es el manseje de prueba para el demo3 en temp\n Es un archivo corto de dos lineas ", encoding="utf-8")
# leo el contenido del archivo
text_readed = text_file.read_text(encoding="utf-8").strip()
print(f"El texto guardado en el demo_3 en temp dice:\n'''{text_readed}'''")

print("\n-----------------------------\n")

# primero creo objeto
tempo_dir = Path(".tempo")
# reviso si existe el direcctorio
print("existe directorio .tempo ?: ", tempo_dir.is_dir())
# si no existe creo el directorio
Path(".tempo").mkdir(exist_ok=True)
# reviso si se creo el direcctorio
print(" YA existe directorio .tempo ?: ", tempo_dir.is_dir())
# reviso si dentro del directorio existe el archivo (nuevo_archivo.md)
print("existe archivo nuevo_archivo.md ?: ",
      (tempo_dir / "nuevo_archivo.md").exists())
# nuevo archivo texto podria ser tambien Path(".tempo/nuevo_archivo.md")
archivo_texto = tempo_dir/"nuevo_archivo.md"
# crea el archivo si lo quiero dejar VACIO sino debo escribir datos si o si
archivo_texto.touch()
print("Ya existe archivo nuevo_archivo.md pero vacio ?: ", archivo_texto.exists())
# ahora le agregamos texto dentro.
archivo_texto.write_text(
    "#Este archivo ahora es en marckdown\n dentro de nuevo_archivo.md en la carpeta .tempo", encoding="utf-8")
# leeo para imprimir por pantalla
lectura = archivo_texto.read_text(encoding="utf-8").strip()
print(f"Contenido del archivo markdown recien creado:\n {lectura}")
# borrado del archivo con unlink solo sirve para achivos o enlaces simbolico
archivo_texto.unlink(missing_ok=True)
print("el archivo (archivo_texto) aun existe?:",archivo_texto.exists())