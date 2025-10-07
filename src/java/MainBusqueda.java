import java.io.File;
import java.io.FileNotFoundException;
import java.io.PrintWriter; 
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Scanner;

public class MainBusqueda {

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
        // Los mensajes de estado van a la consola de error
        System.err.println("Iniciando benchmarks de BÚSQUEDA en Java...");
        
        String[] nombresAlgoritmos = {"BinarySearch", "JumpSearch", "TernarySearch"};
        int[] tamaños = {10000, 100000, 1000000};
        int elementoABuscar = -1;
        int repeticiones = 100;

        try (PrintWriter writer = new PrintWriter("results/tiempos_busqueda_java.csv")) {
            
            writer.println("algoritmo;lenguaje;tamaño;tiempo");

            for (int tam : tamaños) {
                String rutaArchivo = String.format("data/datos_%d.txt", tam);
                int[] datosOriginales = leerDatos(rutaArchivo);
                
                Arrays.sort(datosOriginales);
                
                System.err.println(String.format("\n--- Probando con %d elementos ordenados ---", tam));

                for (String nombreAlg : nombresAlgoritmos) {
                    long startTime = System.nanoTime();

                    for (int i = 0; i < repeticiones; i++) {
                        switch (nombreAlg) {
                            case "BinarySearch": Busqueda.binarySearch(datosOriginales, elementoABuscar); break;
                            case "JumpSearch": Busqueda.jumpSearch(datosOriginales, elementoABuscar); break;
                            case "TernarySearch": Busqueda.ternarySearch(datosOriginales, elementoABuscar); break;
                        }
                    }

                    long endTime = System.nanoTime();
                    double tiempoTotalPromedio = ((double)(endTime - startTime) / repeticiones) / 1e9;

                    writer.println(String.format("%s;Java;%d;%.8f", nombreAlg, tam, tiempoTotalPromedio));
                }
            }
        } 

        System.err.println("\n¡Benchmarks de búsqueda en Java finalizados! Archivo CSV generado.");
    }
}