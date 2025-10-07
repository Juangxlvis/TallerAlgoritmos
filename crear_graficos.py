import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import os
import numpy as np 

print("Creando todos los gráficos comparativos...")


# Ordenamiento
df_python_ord = pd.read_csv("results/tiempos_ordenamiento_python.csv")
df_java_ord = pd.read_csv("results/tiempos_ordenamiento_java.csv", delimiter=';', decimal=',')
df_ordenamiento = pd.concat([df_python_ord, df_java_ord]).reset_index(drop=True)
df_ordenamiento['tiempo'] = pd.to_numeric(df_ordenamiento['tiempo'], errors='coerce')


df_ordenamiento.replace([np.inf, -np.inf], np.nan, inplace=True)
placeholder_time = 500
df_ordenamiento.fillna({'tiempo': placeholder_time}, inplace=True)

# Búsqueda
df_python_busq = pd.read_csv("results/tiempos_busqueda_python.csv")
df_java_busq = pd.read_csv("results/tiempos_busqueda_java.csv", delimiter=';', decimal=',')
df_busqueda = pd.concat([df_python_busq, df_java_busq]).reset_index(drop=True)
df_busqueda['tiempo'] = pd.to_numeric(df_busqueda['tiempo'], errors='coerce')
df_busqueda.dropna(subset=['tiempo'], inplace=True)

# Tamaños que vamos a graficar
tamaños = [10000, 100000, 1000000]

# Crear la carpeta para los gráficos si no existe
if not os.path.exists("results/graphics"):
    os.makedirs("results/graphics")


for tam in tamaños:
    df_filtrado = df_ordenamiento[df_ordenamiento['tamaño'] == tam]
    
    plt.figure(figsize=(14, 8))
    palette = {"Python": "#3498db", "Java": "#e74c3c"}
    ax = sns.barplot(x="algoritmo", y="tiempo", hue="lenguaje", data=df_filtrado, palette=palette)
    
    plt.yscale('log')
    plt.ylabel("Tiempo (segundos) - Escala Logarítmica", fontsize=12)
    plt.xlabel("Algoritmo", fontsize=12)
    plt.title(f"Rendimiento de Ordenamiento ({tam:,} elementos)", fontsize=16)
    plt.xticks(rotation=45, ha='right')

    for p in ax.patches:
        if p.get_height() > 0:
            valor = f"{p.get_height():.4f}"
            ax.annotate(valor, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=10)

    if tam == 1000000:
        plt.text(0.02, 0.7,
                 '*Nota: Las barras de ShakerSort se muestran\n'
                 'a una altura simbólica para fines visuales.\n'
                 'Tiempos reales estimados:\n'
                 '  - Java: >15 minutos\n'
                 '  - Python: >11 horas',
                 transform=plt.gca().transAxes,
                 fontsize=12,
                 verticalalignment='center',
                 bbox=dict(boxstyle='round,pad=0.5', fc='wheat', alpha=0.8))

    plt.tight_layout()
    ruta_guardado = f"results/graphics/grafico_ordenamiento_{tam}.png"
    plt.savefig(ruta_guardado)
    print(f" Gráfico de ordenamiento para {tam} guardado en '{ruta_guardado}'")
    plt.close()

# --- Bucle para generar los gráficos de BÚSQUEDA ---
for tam in tamaños:
    df_filtrado = df_busqueda[df_busqueda['tamaño'] == tam]
    
    plt.figure(figsize=(12, 7))
    ax = sns.barplot(x="algoritmo", y="tiempo", hue="lenguaje", data=df_filtrado, palette=["#2ecc71", "#f39c12"])
    
    plt.ylabel("Tiempo (segundos)", fontsize=12)
    plt.xlabel("Algoritmo", fontsize=12)
    plt.title(f"Rendimiento de Búsqueda ({tam:,} elementos)", fontsize=16)

    for p in ax.patches:
        if not pd.isna(p.get_height()):
            valor = f"{p.get_height():.8f}"
            ax.annotate(valor, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=10)

    plt.tight_layout()
    ruta_guardado = f"results/graphics/grafico_busqueda_{tam}.png"
    plt.savefig(ruta_guardado)
    print(f"Gráfico de búsqueda para {tam} guardado en '{ruta_guardado}'")
    plt.close()

print("\nProceso completado")