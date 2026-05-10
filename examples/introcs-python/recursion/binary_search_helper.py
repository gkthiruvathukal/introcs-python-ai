from hypothesis import given, strategies as st


# start: binary_search_helper
def binary_search(arr: list, key) -> int:
    """Return the index of key in sorted arr, or -1 if not found."""
    def helper(low: int, high: int) -> int:
        if low > high:
            return -1
        mid = (low + high) // 2
        if arr[mid] == key:
            return mid
        elif arr[mid] > key:
            return helper(low, mid - 1)
        else:
            return helper(mid + 1, high)
    return helper(0, len(arr) - 1)
# end: binary_search_helper


# start: hypothesis_test
@given(st.lists(st.integers()), st.integers())
def test_binary_search_property(arr, key):
    arr.sort()
    result = binary_search(arr, key)
    if key not in arr:
        assert result == -1
    else:
        assert 0 <= result < len(arr)
        assert arr[result] == key
# end: hypothesis_test


if __name__ == '__main__':
    data = [-5, 2, 8, 9, 12, 22]
    print(binary_search(data, 9))   # 3
    print(binary_search(data, 7))   # -1
