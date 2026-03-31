"""Microleccion 02 de pathlib.

Tema:
- Crear y leer un archivo con Path.

Que vas a observar:
- Uso de carpeta .tmp para pruebas.
- Escritura y lectura de texto con pathlib.

Concepto SO relacionado:
- Operaciones basicas de filesystem desde un proceso.
"""

from pathlib import Path

print("[Paso 1] Preparando carpeta temporal .tmp...")
tmp_dir = Path(".tmp")
tmp_dir.mkdir(exist_ok=True)

archivo = tmp_dir / "pathlib_demo.txt"

print("[Paso 2] Escribiendo archivo de ejemplo...")
archivo.write_text("hola desde pathlib\n", encoding="utf-8")

print("[Paso 3] Leyendo archivo...")
contenido = archivo.read_text(encoding="utf-8").strip()

print("[Resultado] Archivo creado:", archivo)
print("[Resultado] Contenido leido:", contenido)

print(f"\n[Ejercicio] Cambia el nombre del archivo a pathlib_demo_2.txt y vuelve a ejecutar.")
print("[Pregunta] ¿Que ventaja practica te da usar Path en lugar de concatenar rutas como texto?")
#seguridad y la compatibilidad. pues en win usa\ y en linux y mac /
# me evito tener que usar (open, write, close)
# al no tener que concatenar evito poner por error barras / de mas
archivo = tmp_dir / "pathlib_demo_2.txt"
archivo.write_text("hola con pathlib file2 created \n", encoding="utf-8")
print("[Paso 3] Leyendo archivo...")
contenido = archivo.read_text(encoding="utf-8").strip()
print("[Resultado] Archivo creado:", archivo)
print("[Resultado] Contenido leido:", contenido)