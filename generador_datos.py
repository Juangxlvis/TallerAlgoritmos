import random

def generar_y_guardar_datos(nombre_archivo, cantidad):
    """Genera números aleatorios de 8 dígitos y los guarda en un archivo."""
    with open(nombre_archivo, 'w') as f:
        for _ in range(cantidad):
            # Genera un número entre 10,000,000 y 99,999,999
            numero = random.randint(10000000, 99999999)
            f.write(str(numero) + '\n')
    print(f"Archivo '{nombre_archivo}' generado con {cantidad} números.")

# Rutas de los archivos de datos
ruta_data = 'data/'
tamaños = [10000, 100000, 1000000]

for tam in tamaños:
    generar_y_guardar_datos(f"{ruta_data}datos_{tam}.txt", tam)