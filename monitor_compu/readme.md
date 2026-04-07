# Para correrlo.
python3 monitor.py --info

## Explicacion de lo que se uso
* Path (pathlib): Lo usamos para entrar a /proc/meminfo. En Linux, el kernel escribe ahí el estado de la RAM en tiempo real. Leerlo es la forma más directa de saber qué pasa en la arquitectura.
* os: Usamos os.getloadavg(). Esta función le pregunta al SO cuántos procesos están haciendo fila para entrar al procesador. Si hay más procesos que núcleos, el CPU es el cuello de botella.
* sys: Lo usamos para detectar el parámetro --info, demostrando que sabes interactuar con los argumentos de entrada del sistema.
* **Dato de clase**: Un HDD (disco mecánico) suele dar entre 30-100 MB/s, mientras que un SSD suele superar los 200-500 MB/s. Si tu script marca menos de 15 MB/s, ¡tienes un cuello de botella claro en el disco! 

## Resumen de lógica para la tarea (Identificar el cuello de botella):
* CPU: Si os.getloadavg() devuelve un número mayor al total de tus núcleos (puedes verlos con os.cpu_count()), la CPU es el cuello de botella.
* RAM: Si en /proc/meminfo el valor de MemAvailable es muy cercano a cero, la Memoria es el cuello de botella.
* Disco: Puedes usar os.popen('iostat') para ver si el %util del disco supera el 80%