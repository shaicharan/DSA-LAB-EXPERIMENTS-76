import random
def randomized_partition(arr, low, high):
    pivot_index = random.randint(low, high)
    arr[pivot_index], arr[high] = arr[high], arr[pivot_index]
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
def randomized_select(arr, low, high, k):
    if low == high:
        return arr[low]
    pivot_index = randomized_partition(arr, low, high)
    num_elements = pivot_index - low + 1
    if num_elements == k:
        return arr[pivot_index]
    elif k < num_elements:
        return randomized_select(arr, low, pivot_index - 1, k)
    else:
        return randomized_select(arr, pivot_index + 1, high, k - num_elements)
def find_kth_smallest(arr, k):
    if k < 1 or k > len(arr):
        raise ValueError("k is out of bounds.")
    return randomized_select(arr, 0, len(arr) - 1, k)
arr = [7, 10, 4, 3, 20, 15]
k = 3
print(f"The {k}-th smallest element is {find_kth_smallest(arr, k)}")
