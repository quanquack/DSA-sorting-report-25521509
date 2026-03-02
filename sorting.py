import numpy as np
import sys

# Phải tăng giới hạn của recursion để tránh lỗi RecursionError với mảng 1 triệu phần tử
sys.setrecursionlimit(2_000_000)
# ==========================================
# QUICKSORT 
# ==========================================
def partition(arr, low, high):
    # Chọn pivot ở giữa để tránh O(N^2) khi mảng đã sắp xếp
    mid = (low + high) // 2
    arr[mid], arr[high] = arr[high], arr[mid]
    pivot = arr[high]
    
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]
            
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1

def quick_sort_recursive(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort_recursive(arr, low, pi - 1)
        quick_sort_recursive(arr, pi + 1, high)

def quick_sort(arr):
    quick_sort_recursive(arr, 0, len(arr) - 1)

# ==========================================
# HEAPSORT
# ==========================================
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

# ==========================================
# MERGESORT
# ==========================================
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid].copy()
        R = arr[mid:].copy()

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0

        while i < len(L) and j < len(R):
            if L[i] <= R[j]:
                arr[k] = L[i]
                i += 1
            else:
                arr[k] = R[j]
                j += 1
            k += 1

        while i < len(L):
            arr[k] = L[i]
            i += 1
            k += 1

        while j < len(R):
            arr[k] = R[j]
            j += 1
            k += 1

# ==========================================
# NUMPY SORT 
# ==========================================
def numpy_sort(arr):
    return np.sort(arr)