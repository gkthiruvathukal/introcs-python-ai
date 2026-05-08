# start: Averager
class Averager:
    def __init__(self):
        self._count = 0
        self._total = 0.0

    def add_datum(self, value: float) -> None:
        self._total += value
        self._count += 1

    def get_average(self) -> float:
        if self._count == 0:
            return float("nan")
        return self._total / self._count

    def get_count(self) -> int:
        return self._count

    def clear(self) -> None:
        self._count = 0
        self._total = 0.0

    def __str__(self) -> str:
        return f"Averager({self._count} values, avg={self.get_average():.4f})"
# end: Averager


if __name__ == '__main__':
    avg = Averager()
    for value in [3.0, 7.5, 2.0, 6.5]:
        avg.add_datum(value)
    print(avg.get_count(), "values")
    print(f"Average: {avg.get_average():.2f}")
    print(avg)
