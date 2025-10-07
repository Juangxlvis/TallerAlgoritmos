# Algoritmos de Búsqueda para Python

def binary_search(arr, x):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (high + low) // 2
        if arr[mid] < x:
            low = mid + 1
        elif arr[mid] > x:
            high = mid - 1
        else:
            return mid
    return -1

def jump_search(arr, x):
    n = len(arr)
    step = int(n**0.5)
    prev = 0
    while arr[min(step, n) - 1] < x:
        prev = step
        step += int(n**0.5)
        if prev >= n:
            return -1
    while arr[prev] < x:
        prev += 1
        if prev == min(step, n):
            return -1
    if arr[prev] == x:
        return prev
    return -1

def ternary_search(arr, x):
    l, r = 0, len(arr) - 1
    while r >= l:
        mid1 = l + (r - l) // 3
        mid2 = r - (r - l) // 3
        if arr[mid1] == x:
            return mid1
        if arr[mid2] == x:
            return mid2
        if x < arr[mid1]:
            r = mid1 - 1
        elif x > arr[mid2]:
            l = mid2 + 1
        else:
            l = mid1 + 1
            r = mid2 - 1
    return -1