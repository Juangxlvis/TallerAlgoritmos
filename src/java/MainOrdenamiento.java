import java.io.File;
import java.io.FileNotFoundException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.io.PrintWriter;


public class MainOrdenamiento {

    // Método para leer los números de un archivo y devolverlos en un arreglo
    public static int[] leerDatos(String archivo) throws FileNotFoundException {
        List<Integer> numeros = new ArrayList<>();
        Scanner scanner = new Scanner(new File(archivo));
        while (scanner.hasNextInt()) {
            numeros.add(scanner.nextInt());
        }
        scanner.close();
        
        // Convertir la lista a un arreglo de enteros primitivos
        int[] arr = new int[numeros.size()];
        for (int i = 0; i < numeros.size(); i++) {
            arr[i] = numeros.get(i);
        }
        return arr;
    }

    public static void main(String[] args) throws FileNotFoundException {
        // Usamos System.err para los mensajes de estado, que seguirán saliendo en la consola
        System.err.println("Iniciando benchmarks de ORDENAMIENTO en Java...");
        
        String[] nombresAlgoritmos = {"ShakerSort", "DualPivotQuickSort", "HeapSort", "MergeSort", "RadixSort"};
        int[] tamaños = {10000, 100000, 1000000};
        
        // 2. Usamos un "try-with-resources" para crear el archivo y asegurarnos de que se cierre solo.
        try (PrintWriter writer = new PrintWriter("results/tiempos_ordenamiento_java.csv")) {
            
            // 3. Escribimos el encabezado directamente en el archivo.
            writer.println("algoritmo;lenguaje;tamaño;tiempo");
            for (int tam : tamaños) {
                String rutaArchivo = String.format("data/datos_%d.txt", tam);
                int[] datosOriginales = leerDatos(rutaArchivo);
                
                System.err.println(String.format("\n--- Probando con %d elementos ---", tam));

                for (String nombreAlg : nombresAlgoritmos) {
                    if (nombreAlg.equals("ShakerSort") && tam == 1000000) {
                        writer.println("ShakerSort;Java;1000000;>900.0000");
                        System.err.println("--- Omitiendo ShakerSort para 1,000,000 elementos por ser demasiado lento ---");
                        continue;
                    }
                    
                    int[] datosACopiar = Arrays.copyOf(datosOriginales, datosOriginales.length);
                    
                    long startTime = System.nanoTime();

                    switch (nombreAlg) {
                        case "ShakerSort": Ordenamiento.shakerSort(datosACopiar); break;
                        case "DualPivotQuickSort": Ordenamiento.dualPivotQuickSort(datosACopiar, 0, datosACopiar.length - 1); break;
                        case "HeapSort": Ordenamiento.heapSort(datosACopiar); break;
                        case "MergeSort": Ordenamiento.mergeSort(datosACopiar, 0, datosACopiar.length - 1); break;
                        case "RadixSort": Ordenamiento.radixSort(datosACopiar); break;
                    }

                    long endTime = System.nanoTime();
                    double tiempoTotal = (endTime - startTime) / 1e9;

                    // 4. En lugar de System.out, usamos writer.println para guardar en el archivo.
                    writer.println(String.format("%s;Java;%d;%.4f", nombreAlg, tam, tiempoTotal));                }
            }
        } // El archivo se guarda y cierra automáticamente aquí.

        System.err.println("\n¡Benchmarks en Java finalizados! Archivo CSV generado.");
    }
}