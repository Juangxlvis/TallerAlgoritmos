// Contenedor para los algoritmos de búsqueda
public class Busqueda {

    public static int binarySearch(int arr[], int x) {
        int l = 0, r = arr.length - 1;
        while (l <= r) {
            int m = l + (r - l) / 2;
            if (arr[m] == x) return m;
            if (arr[m] < x) l = m + 1;
            else r = m - 1;
        }
        return -1;
    }

    public static int jumpSearch(int arr[], int x) {
        int n = arr.length;
        int step = (int)Math.floor(Math.sqrt(n));
        int prev = 0;
        while (arr[Math.min(step, n) - 1] < x) {
            prev = step;
            step += (int)Math.floor(Math.sqrt(n));
            if (prev >= n) return -1;
        }
        while (arr[prev] < x) {
            prev++;
            if (prev == Math.min(step, n)) return -1;
        }
        if (arr[prev] == x) return prev;
        return -1;
    }

    public static int ternarySearch(int arr[], int x) {
        int l = 0, r = arr.length - 1;
        while (r >= l) {
            int mid1 = l + (r - l) / 3;
            int mid2 = r - (r - l) / 3;
            if (arr[mid1] == x) return mid1;
            if (arr[mid2] == x) return mid2;
            if (x < arr[mid1]) r = mid1 - 1;
            else if (x > arr[mid2]) l = mid2 + 1;
            else {
                l = mid1 + 1;
                r = mid2 - 1;
            }
        }
        return -1;
    }
}