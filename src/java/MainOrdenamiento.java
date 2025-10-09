import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;
import java.util.Map;
import java.util.HashMap;

public class MainOrdenamiento {

    public static int[] leerDatos(String archivo) throws FileNotFoundException {
        List<Integer> numeros = new ArrayList<>();
        Scanner scanner = new Scanner(new File(archivo));
        while (scanner.hasNextInt()) {
            numeros.add(scanner.nextInt());
        }
        scanner.close();
        
        int[] arr = new int[numeros.size()];
        for (int i = 0; i < numeros.size(); i++) {
            arr[i] = numeros.get(i);
        }
        return arr;
    }

    public static void main(String[] args) throws FileNotFoundException {
        System.err.println("Iniciando benchmarks de ORDENAMIENTO en Java...");
        
        String[] nombresAlgoritmos = {"ShakerSort", "DualPivotQuickSort", "HeapSort", "MergeSort", "RadixSort"};
        int[] tamaños = {10000, 100000, 1000000};
        
        Map<String, String> complejidades = new HashMap<>();
        complejidades.put("ShakerSort", "O(n²)");
        complejidades.put("DualPivotQuickSort", "O(n log n)");
        complejidades.put("HeapSort", "O(n log n)");
        complejidades.put("MergeSort", "O(n log n)");
        complejidades.put("RadixSort", "O(n·k)");
        
        try (PrintWriter writer = new PrintWriter("results/tiempos_ordenamiento_java.csv")) {
            
            writer.println("algoritmo;complejidad;lenguaje;tamaño;tiempo");
            
            for (int tam : tamaños) {
                String rutaArchivo = String.format("data/datos_%d.txt", tam);
                int[] datosOriginales = leerDatos(rutaArchivo);
                
                System.err.println(String.format("\n--- Probando con %d elementos ---", tam));

                for (String nombreAlg : nombresAlgoritmos) {
                    String complejidad = complejidades.get(nombreAlg);

                    if (nombreAlg.equals("ShakerSort") && tam == 1000000) {
                        writer.println(String.format("ShakerSort;%s;Java;1000000;", complejidad));
                        System.err.println(String.format("--- Omitiendo ShakerSort (%s) para 1,000,000 elementos por ser demasiado lento ---", complejidad));
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
                    
                    System.err.println(String.format("  - %s (%s): %.4f segundos", nombreAlg, complejidad, tiempoTotal));
                    writer.println(String.format("%s;%s;Java;%d;%.4f", nombreAlg, complejidad, tam, tiempoTotal));
                }
            }
        } 

        System.err.println("\nBenchmarks en Java finalizados. Archivo CSV generado.");
    }
}