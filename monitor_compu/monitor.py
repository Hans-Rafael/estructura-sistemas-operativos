import os
import sys
import time
from pathlib import Path

def test_velocidad_disco():
    # Creamos un archivo de 100MB para la prueba
    ruta_test = Path("test_velocidad.tmp")
    datos = b"0" * 1024 * 1024  # 1 MB de datos en memoria
    
    start_time = time.time()
    try:
        with open(ruta_test, "wb") as f:
            for _ in range(100):  # Escribimos 1MB cien veces
                f.write(datos)
                os.fsync(f.fileno()) # Forzamos al SO a escribir físicamente en el disco
        
        end_time = time.time()
        duracion = end_time - start_time
        velocidad = 100 / duracion # MB por segundo
        
        # Borramos el archivo de prueba usando os
        os.remove(ruta_test)
        return velocidad
    except Exception as e:
        return f"Error en disco: {e}"

def analizar_sistema():
    print("=== REPORTE DE RENDIMIENTO (LINUX MINT) ===")
    
    # 1. CPU (Carga de procesos en cola)
    carga_1min = os.getloadavg()[0]
    num_cpus = os.cpu_count()
    uso_cpu_pct = (carga_1min / num_cpus) * 100
    print(f"CPU: {uso_cpu_pct:.1f}% de carga media")

    # 2. RAM (Lectura directa de /proc/meminfo)
    mem_info = Path("/proc/meminfo").read_text().splitlines()
    total_kb = int(mem_info[0].split()[1])
    disponible_kb = int(mem_info[2].split()[1]) # MemAvailable
    uso_ram_pct = 100 - (disponible_kb / total_kb * 100)
    print(f"RAM: {uso_ram_pct:.1f}% en uso")

    # 3. DISCO (Prueba de escritura real)
    print("Midiendo velocidad de disco (espera un momento)...")
    vel_escritura = test_velocidad_disco()
    print(f"DISCO: {vel_escritura:.2f} MB/s de escritura")

    # VEREDICTO DE CUELLO DE BOTELLA
    print("\n--- CONCLUSIÓN ---")
    if uso_cpu_pct > 95:
        print("RESULTADO: Cuello de botella en PROCESADOR.")
    elif uso_ram_pct > 90:
        print("RESULTADO: Cuello de botella en MEMORIA RAM.")
    elif isinstance(vel_escritura, float) and vel_escritura < 20:
        print("RESULTADO: Cuello de botella en DISCO (Velocidad muy baja).")
    else:
        print("RESULTADO: El sistema funciona con fluidez.")

if __name__ == "__main__":
    # Verificamos argumentos del sistema con sys
    if len(sys.argv) > 1:
        print(f"Argumentos detectados: {sys.argv[1:]}")
    analizar_sistema()
