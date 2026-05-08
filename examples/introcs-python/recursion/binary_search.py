# start: binary_search
def binary_search(data: list, target, lo: int = 0, hi: int | None = None) -> int:
    """Return the index of target in sorted data, or -1 if not found."""
    if hi is None:
        hi = len(data) - 1
    if lo > hi:
        return -1
    mid = (lo + hi) // 2
    if data[mid] == target:
        return mid
    elif data[mid] < target:
        return binary_search(data, target, mid + 1, hi)
    else:
        return binary_search(data, target, lo, mid - 1)
# end: binary_search


if __name__ == '__main__':
    data = [-5, 2, 8, 9, 12, 22]
    print(binary_search(data, 9))    # 3
    print(binary_search(data, 7))    # -1
