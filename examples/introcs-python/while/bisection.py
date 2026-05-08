def bisection(f, a: float, b: float, tolerance: float = 1e-10) -> float | None:
    """Return an approximate root of f in [a, b].

    Requires f(a) and f(b) to have opposite signs.
    Returns None if that precondition is not met.
    """
    if f(a) * f(b) > 0:
        return None

    while (b - a) > tolerance:
        c = (a + b) / 2
        if f(c) == 0:
            return c
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c
    return (a + b) / 2


if __name__ == '__main__':
    def f(x: float) -> float:
        return x**2 - 2

    root = bisection(f, 0, 2)
    print(f"Root ≈ {root:.10f}")
    print(f"math.sqrt(2) = {2**0.5:.10f}")
