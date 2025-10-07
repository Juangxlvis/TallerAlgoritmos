import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

print("📊 Creando todos los gráficos comparativos...")

# --- Carga y limpieza de datos (se hace una sola vez) ---

# Ordenamiento
df_python_ord = pd.read_csv("results/tiempos_ordenamiento_python.csv")
df_java_ord = pd.read_csv("results/tiempos_ordenamiento_java.csv", delimiter=';', decimal=',')
df_ordenamiento = pd.concat([df_python_ord, df_java_ord]).reset_index(drop=True)
df_ordenamiento['tiempo'] = pd.to_numeric(df_ordenamiento['tiempo'], errors='coerce')
df_ordenamiento.dropna(subset=['tiempo'], inplace=True)

# Búsqueda
df_python_busq = pd.read_csv("results/tiempos_busqueda_python.csv")
df_java_busq = pd.read_csv("results/tiempos_busqueda_java.csv", delimiter=';', decimal=',')
df_busqueda = pd.concat([df_python_busq, df_java_busq]).reset_index(drop=True)
df_busqueda['tiempo'] = pd.to_numeric(df_busqueda['tiempo'], errors='coerce')
df_busqueda.dropna(subset=['tiempo'], inplace=True)


# Tamaños que vamos a graficar
tamaños = [10000, 100000, 1000000]

# --- Bucle para generar los gráficos de ORDENAMIENTO ---
for tam in tamaños:
    # Filtramos los datos para el tamaño actual
    df_filtrado = df_ordenamiento[df_ordenamiento['tamaño'] == tam]
    
    plt.figure(figsize=(14, 8))
    ax = sns.barplot(x="algoritmo", y="tiempo", hue="lenguaje", data=df_filtrado, palette=["#3498db", "#e74c3c"])
    
    # --- ¡LA SOLUCIÓN A LA ESCALA! ---
    # Usamos escala logarítmica para poder ver las barras de Java
    plt.yscale('log')
    
    plt.ylabel("Tiempo (segundos) - Escala Logarítmica", fontsize=12)
    plt.xlabel("Algoritmo", fontsize=12)
    plt.title(f"Rendimiento de Ordenamiento ({tam:,} elementos)", fontsize=16)
    plt.xticks(rotation=45, ha='right')

    for p in ax.patches:
        if p.get_height() > 0: # Solo anotar si la barra es visible
            valor = f"{p.get_height():.4f}"
            ax.annotate(valor, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=10)

    plt.tight_layout()
    # Guardamos el archivo con un nombre único para cada tamaño
    ruta_guardado = f"results/graphics/grafico_ordenamiento_{tam}.png"
    plt.savefig(ruta_guardado)
    print(f"✅ Gráfico de ordenamiento para {tam} guardado en '{ruta_guardado}'")
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
        valor = f"{p.get_height():.8f}"
        ax.annotate(valor, (p.get_x() + p.get_width() / 2., p.get_height()), ha='center', va='center', xytext=(0, 9), textcoords='offset points', fontsize=10)

    plt.tight_layout()
    ruta_guardado = f"results/graphics/grafico_busqueda_{tam}.png"
    plt.savefig(ruta_guardado)
    print(f"✅ Gráfico de búsqueda para {tam} guardado en '{ruta_guardado}'")
    plt.close()