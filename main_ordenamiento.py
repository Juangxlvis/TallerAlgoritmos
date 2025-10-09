import time
import pandas as pd
# Importamos todas las funciones que pegaste en el otro archivo
from src.python.ordenamiento import *

def leer_datos(archivo):
    """Carga los números desde un archivo de texto."""
    with open(archivo, 'r') as f:
        return [int(line.strip()) for line in f]

# --- Bucle principal para medir tiempos ---
print("Iniciando benchmarks de ORDENAMIENTO en Python...")

resultados = []
# Diccionario que asocia el nombre del algoritmo con su función
algoritmos = {
    "ShakerSort": (shaker_sort, "O(n²)"),
    "DualPivotQuickSort": (dual_pivot_quicksort, "O(n log n)"),
    "HeapSort": (heap_sort, "O(n log n)"),
    "MergeSort": (merge_sort, "O(n log n)"),
    "RadixSort": (radix_sort, "O(n·k)")
}

tamaños = [10000, 100000, 1000000]

for tam in tamaños:
    ruta_archivo = f"data/datos_{tam}.txt"
    datos = leer_datos(ruta_archivo)
    print(f"\n--- Probando con {tam} elementos ---")

    for nombre, (funcion_sort, complejidad) in algoritmos.items():

        if nombre == "ShakerSort" and tam == 1000000:
            print(f" {nombre} ({complejidad}): Omitido por ser demasiado lento (estimado > 10 horas)")
            # Añadimos un resultado simbólico para que el CSV quede completo
            resultados.append({
                "algoritmo": nombre,
                "complejidad": complejidad,
                "lenguaje": "Python",
                "tamaño": tam,
                "tiempo": float('inf') # Usamos infinito para representar el tiempo
            })
            continue
        # ¡Importante! Copiamos los datos para que cada algoritmo ordene el arreglo original
        datos_a_ordenar = datos.copy()

        start_time = time.perf_counter()
        funcion_sort(datos_a_ordenar)
        end_time = time.perf_counter()

        tiempo_total = end_time - start_time
        print(f" check : {nombre} ({complejidad}): {tiempo_total:.4f} segundos")
        
        resultados.append({
            "algoritmo": nombre,
            "complejidad": complejidad,
            "lenguaje": "Python",
            "tamaño": tam,
            "tiempo": tiempo_total
        })

# --- Guardar resultados en CSV ---
df_resultados = pd.DataFrame(resultados)
ruta_csv = "results/tiempos_ordenamiento_python.csv"
df_resultados.to_csv(ruta_csv, index=False)

print(f"\n¡Benchmarks finalizados! Resultados guardados en '{ruta_csv}'")