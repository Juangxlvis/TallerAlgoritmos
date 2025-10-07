import time
import pandas as pd
from src.python.busqueda import *

def leer_datos(archivo):
    """Carga los números desde un archivo de texto."""
    with open(archivo, 'r') as f:
        return [int(line.strip()) for line in f]

print("Iniciando benchmarks de BÚSQUEDA en Python...")

resultados_busqueda = []
algoritmos_busqueda = {
    "BinarySearch": binary_search,
    "JumpSearch": jump_search,
    "TernarySearch": ternary_search
}

tamaños = [10000, 100000, 1000000]
# Elemento a buscar (peor caso: no existe)
elemento_a_buscar = -1 

for tam in tamaños:
    ruta_archivo = f"data/datos_{tam}.txt"
    datos = leer_datos(ruta_archivo)
    
    # ¡MUY IMPORTANTE! La búsqueda requiere datos ordenados.
    # Este tiempo de ordenamiento NO se mide.
    datos.sort()
    
    print(f"\n--- Probando con {tam} elementos ordenados ---")

    for nombre, funcion_busq in algoritmos_busqueda.items():
        start_time = time.perf_counter()
        # Se realizan múltiples búsquedas para obtener una medición más estable
        for _ in range(100):
             funcion_busq(datos, elemento_a_buscar)
        end_time = time.perf_counter()
        
        # El tiempo total se divide por el número de repeticiones
        tiempo_promedio = (end_time - start_time) / 100
        
        print(f" check : {nombre}: {tiempo_promedio:.8f} segundos")
        
        resultados_busqueda.append({
            "algoritmo": nombre,
            "lenguaje": "Python",
            "tamaño": tam,
            "tiempo": tiempo_promedio
        })

# --- Guardar resultados en CSV ---
df_resultados_busqueda = pd.DataFrame(resultados_busqueda)
ruta_csv_busqueda = "results/tiempos_busqueda_python.csv"
df_resultados_busqueda.to_csv(ruta_csv_busqueda, index=False)

print(f"\n¡Benchmarks finalizados! Resultados guardados en '{ruta_csv_busqueda}'")