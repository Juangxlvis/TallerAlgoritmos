# -----------------------------------------------------------------------------
# 1. Shaker Sort (Cocktail Sort)
# Fuente: https://www.geeksforgeeks.org/dsa/cocktail-sort/
# -----------------------------------------------------------------------------
def shaker_sort(a):
    n = len(a)
    swapped = True
    start = 0
    end = n - 1
    while (swapped == True):
        swapped = False
        for i in range(start, end):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        if (swapped == False):
            break
        swapped = False
        end = end - 1
        for i in range(end - 1, start - 1, -1):
            if (a[i] > a[i + 1]):
                a[i], a[i + 1] = a[i + 1], a[i]
                swapped = True
        start = start + 1

# -----------------------------------------------------------------------------
# 2. Dual-Pivot QuickSort
# Fuente: https://www.geeksforgeeks.org/dsa/dual-pivot-quicksort/
# -----------------------------------------------------------------------------
def dual_pivot_quicksort_partition(arr, low, high):
    if arr[low] > arr[high]:
        arr[low], arr[high] = arr[high], arr[low]

    j = k = low + 1
    g, p, q = high - 1, arr[low], arr[high]
    
    while k <= g:
        if arr[k] < p:
            arr[k], arr[j] = arr[j], arr[k]
            j += 1
        elif arr[k] >= q:
            while arr[g] > q and k < g:
                g -= 1
            arr[k], arr[g] = arr[g], arr[k]
            g -= 1
            if arr[k] < p:
                arr[k], arr[j] = arr[j], arr[k]
                j += 1
        k += 1

    j -= 1
    g += 1
    
    arr[low], arr[j] = arr[j], arr[low]
    arr[high], arr[g] = arr[g], arr[high]
    
    return j, g

def dual_pivot_quicksort_recursive(arr, low, high):
    if low < high:
        lp, rp = dual_pivot_quicksort_partition(arr, low, high)
        dual_pivot_quicksort_recursive(arr, low, lp - 1)
        dual_pivot_quicksort_recursive(arr, lp + 1, rp - 1)
        dual_pivot_quicksort_recursive(arr, rp + 1, high)

def dual_pivot_quicksort(arr):
    dual_pivot_quicksort_recursive(arr, 0, len(arr) - 1)


# -----------------------------------------------------------------------------
# 3. Heap Sort
# Fuente: https://www.geeksforgeeks.org/dsa/heap-sort/
# -----------------------------------------------------------------------------
def heapify(arr, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    if r < n and arr[r] > arr[largest]:
        largest = r
        
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def heap_sort(arr):
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)

# -----------------------------------------------------------------------------
# 4. Merge Sort
# Fuente: https://www.geeksforgeeks.org/dsa/merge-sort/
# -----------------------------------------------------------------------------
def merge(arr, l, m, r):
    n1 = m - l + 1
    n2 = r - m
    L = [0] * n1
    R = [0] * n2
    for i in range(0, n1):
        L[i] = arr[l + i]
    for j in range(0, n2):
        R[j] = arr[m + 1 + j]
    i = 0
    j = 0
    k = l
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1
    while i < n1:
        arr[k] = L[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = R[j]
        j += 1
        k += 1

def merge_sort_recursive(arr, l, r):
    if l < r:
        m = l + (r - l) // 2
        merge_sort_recursive(arr, l, m)
        merge_sort_recursive(arr, m + 1, r)
        merge(arr, l, m, r)

def merge_sort(arr):
    merge_sort_recursive(arr, 0, len(arr) - 1)


# -----------------------------------------------------------------------------
# 5. Radix Sort
# Fuente: https://www.geeksforgeeks.org/python/python-program-for-radix-sort/
# -----------------------------------------------------------------------------
def counting_sort_for_radix(arr, exp1):
    n = len(arr)
    output = [0] * n
    count = [0] * 10
    
    for i in range(0, n):
        index = arr[i] // exp1
        count[index % 10] += 1
        
    for i in range(1, 10):
        count[i] += count[i - 1]
        
    i = n - 1
    while i >= 0:
        index = arr[i] // exp1
        output[count[index % 10] - 1] = arr[i]
        count[index % 10] -= 1
        i -= 1
        
    i = 0
    for i in range(0, len(arr)):
        arr[i] = output[i]

def radix_sort(arr):
    max1 = max(arr)
    exp = 1
    while max1 / exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10