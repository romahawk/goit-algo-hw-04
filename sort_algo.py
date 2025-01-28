import timeit
import random


# Алгоритм сортування вставками
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


# Алгоритм сортування злиттям
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        L = arr[:mid]
        R = arr[mid:]

        merge_sort(L)
        merge_sort(R)

        i = j = k = 0
        while i < len(L) and j < len(R):
            if L[i] < R[j]:
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

    return arr


# Набори тестових даних
def generate_test_data(size):
    """Генерує випадковий список заданого розміру."""
    return [random.randint(0, 10000) for _ in range(size)]


# Функція для запуску та вимірювання часу
def test_algorithms():
    sizes = [100, 1000, 5000, 10000]  # Розміри списків
    results = {}

    for size in sizes:
        data = generate_test_data(size)

        # Час для сортування вставками
        insertion_time = timeit.timeit(lambda: insertion_sort(data.copy()), number=1)

        # Час для сортування злиттям
        merge_time = timeit.timeit(lambda: merge_sort(data.copy()), number=1)

        # Час для Timsort (вбудована sorted())
        timsort_time = timeit.timeit(lambda: sorted(data.copy()), number=1)

        results[size] = {
            "Insertion Sort": insertion_time,
            "Merge Sort": merge_time,
            "Timsort (sorted)": timsort_time,
        }

    # Виведення результатів
    print(f"{'Size':<10}{'Insertion Sort':<20}{'Merge Sort':<20}{'Timsort (sorted)':<20}")
    for size, times in results.items():
        print(
            f"{size:<10}{times['Insertion Sort']:<20.6f}{times['Merge Sort']:<20.6f}{times['Timsort (sorted)']:<20.6f}"
        )



# Запуск тестів
test_algorithms()
