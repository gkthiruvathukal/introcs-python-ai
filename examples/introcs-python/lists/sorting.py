def selection_sort(data: list) -> None:
    """Sort data in place using selection sort — O(N²)."""
    n = len(data)
    for i in range(n):
        min_pos = i
        for j in range(i + 1, n):
            if data[j] < data[min_pos]:
                min_pos = j
        data[i], data[min_pos] = data[min_pos], data[i]


def bubble_sort(data: list) -> None:
    """Sort data in place using bubble sort — O(N²)."""
    n = len(data)
    for i in range(n - 1):
        for j in range(n - 1 - i):
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]


def insertion_sort(data: list) -> None:
    """Sort data in place using insertion sort — O(N²), efficient for nearly-sorted data."""
    for i in range(1, len(data)):
        key = data[i]
        j = i - 1
        while j >= 0 and data[j] > key:
            data[j + 1] = data[j]
            j -= 1
        data[j + 1] = key


if __name__ == '__main__':
    for sort_fn in (selection_sort, bubble_sort, insertion_sort):
        nums = [12, 8, -5, 22, 9, 2]
        sort_fn(nums)
        print(f"{sort_fn.__name__}: {nums}")
