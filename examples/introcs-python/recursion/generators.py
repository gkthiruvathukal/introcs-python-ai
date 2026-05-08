from itertools import takewhile


def factorials():
    """Yield 0!, 1!, 2!, 3!, ... without bound."""
    result = 1
    n = 0
    while True:
        yield result
        n += 1
        result *= n


def factorials_up_to(ceiling: int):
    """Yield each factorial that does not exceed ceiling."""
    if ceiling < 1:
        raise ValueError(f"ceiling must be >= 1, got {ceiling}")
    result, n = 1, 0
    while result <= ceiling:
        yield result
        n += 1
        result *= n


def fibonacci():
    """Yield F(0), F(1), F(2), ... without bound."""
    prev, curr = 0, 1
    while True:
        yield prev
        prev, curr = curr, prev + curr


def fibonacci_up_to(ceiling: int):
    """Yield each Fibonacci number that does not exceed ceiling."""
    if ceiling < 0:
        raise ValueError(f"ceiling must be >= 0, got {ceiling}")
    prev, curr = 0, 1
    while prev <= ceiling:
        yield prev
        prev, curr = curr, prev + curr


if __name__ == '__main__':
    print(list(factorials_up_to(1_000_000)))
    print(list(takewhile(lambda x: x <= 1000, fibonacci())))
