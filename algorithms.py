import time

def merge_sort(arr, key_func):
    """
    Manual implementation of Merge Sort algorithm.
    Efficiency: O(n log n)
    """
    if len(arr) <= 1:
        return arr
    
    mid = len(arr) // 2
    left = merge_sort(arr[:mid], key_func)
    right = merge_sort(arr[mid:], key_func)
    
    return merge(left, right, key_func)

def merge(left, right, key_func):
    """ Helper function to merge two sorted halves """
    result = []
    i = j = 0
    
    while i < len(left) and j < len(right):
        if key_func(left[i]) <= key_func(right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
            
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def binary_search(arr, target_id):
    """
    Manual implementation of Binary Search.
    Requires the array to be sorted by ID.
    Efficiency: O(log n)
    """
    low = 0
    high = len(arr) - 1
    
    while low <= high:
        mid = (low + high) // 2
        if arr[mid].id == target_id:
            return arr[mid]
        elif arr[mid].id < target_id:
            low = mid + 1
        else:
            high = mid - 1
    return None

def benchmark_sort(arr, key_func, label="Sort"):
    """ Measures the execution time of the sorting algorithm """
    start_time = time.time()
    sorted_arr = merge_sort(arr, key_func)
    end_time = time.time()
    print(f"⏱️ {label} Benchmark: {end_time - start_time:.6f} seconds")
    return sorted_arr