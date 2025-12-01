import random
import timeit
from typing import List

def merge_sort(array) -> List[int]:
    if len(array) <= 1:
        return array

    middle = len(array) // 2
    
    left = array[:middle]
    right = array[middle:]

    sorted_left = merge_sort(left)
    sorted_right = merge_sort(right)

    return merge(sorted_left, sorted_right)

def merge(left: List[int], right: List[int]):
    i = 0
    j = 0
    result = []

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    while i < len(left):
        result.append(left[i])
        i+=1

    while j < len(right):
        result.append(right[j])
        j+=1

    return result

def insertion_sort(array: List[int]) -> List[int]:
    length = len(array)

    for i in range(1, length):
        insert_index = i
        current_value = array[i]

        for j in range(i - 1, -1, -1):
            if array[j] > current_value:
                array[j + 1] = array[j]
                insert_index = j
            else:
                break

        array[insert_index] = current_value

    return array


def insertion_sort_range(arr: List[int], left: int, right: int) -> None:
    for i in range(left + 1, right + 1):
        current_value = arr[i]
        j = i - 1
        while j >= left and arr[j] > current_value:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = current_value

def tim_sort(arr):
    min_run = 32

    n = len(arr)

    for start in range(0, n, min_run):
        end = min(start + min_run - 1, n - 1)
        insertion_sort_range(arr, start, end)

    size = min_run
    while size < n:
        for start in range(0, n, size * 2):
            midpoint = start + size
            if midpoint >= n:
                continue

            end = min(start + size * 2 - 1, n - 1)

            left = arr[start:midpoint]
            right = arr[midpoint:end + 1]

            merged_array = merge(left, right)
            arr[start:start + len(merged_array)] = merged_array

        size *= 2

    return arr


def generate_random_list(n: int, low: int = 0, high: int = 10**6) -> List[int]:
    return [random.randint(low, high) for _ in range(n)]


def benchmark():
    sizes = [50, 100, 1_000, 5_000, 10_000]
    repeats = 5  

    algorithms = {
        "insertion_sort": lambda arr: insertion_sort(arr.copy()),
        "merge_sort": lambda arr: merge_sort(arr.copy()),
        "tim_sort":     lambda arr: tim_sort(arr.copy()),
        "built_in_sorted": lambda arr: sorted(arr),
    }

    for n in sizes:
        base_data = generate_random_list(n)
        print(f"\n=== n = {n} ===")

        for name, func in algorithms.items():
            t = timeit.timeit(
                stmt=lambda f=func, data=base_data: f(data),
                number=repeats
            )
            avg = t / repeats
            print(f"{name:16} -> {avg:.6f} s (avg over {repeats} runs)")


if __name__ == "__main__":
    benchmark()