import math


class Rational:
    def __init__(self, numerator: int, denominator: int = 1):
        if denominator == 0:
            raise ValueError("Denominator cannot be zero")
        g = math.gcd(abs(numerator), abs(denominator))
        sign = -1 if denominator < 0 else 1
        self._num = sign * numerator // g
        self._denom = sign * denominator // g

    def numerator(self) -> int:
        return self._num

    def denominator(self) -> int:
        return self._denom

    def __str__(self) -> str:
        if self._denom == 1:
            return str(self._num)
        return f"{self._num}/{self._denom}"

    def __repr__(self) -> str:
        return f"Rational({self._num}, {self._denom})"

    def __add__(self, other: "Rational") -> "Rational":
        return Rational(
            self._num * other._denom + other._num * self._denom,
            self._denom * other._denom,
        )

    def __sub__(self, other: "Rational") -> "Rational":
        return Rational(
            self._num * other._denom - other._num * self._denom,
            self._denom * other._denom,
        )

    def __mul__(self, other: "Rational") -> "Rational":
        return Rational(self._num * other._num, self._denom * other._denom)

    def __truediv__(self, other: "Rational") -> "Rational":
        return Rational(self._num * other._denom, self._denom * other._num)

    def __eq__(self, other: object) -> bool:
        if not isinstance(other, Rational):
            return NotImplemented
        return self._num == other._num and self._denom == other._denom

    def __lt__(self, other: "Rational") -> bool:
        return self._num * other._denom < other._num * self._denom

    def __le__(self, other: "Rational") -> bool:
        return self == other or self < other

    def __float__(self) -> float:
        return self._num / self._denom

    @classmethod
    def parse(cls, s: str) -> "Rational":
        if "/" in s:
            num, denom = s.split("/")
            return cls(int(num), int(denom))
        if "." in s:
            digits_after = len(s.split(".")[1])
            value = int(s.replace(".", ""))
            return cls(value, 10 ** digits_after)
        return cls(int(s))


if __name__ == '__main__':
    f = Rational(6, -10)
    h = Rational(1, 2)

    print(f)               # -3/5
    print(f + h)           # -1/10
    print(f * h)           # -3/10
    print(h > f)           # True
    print(float(f))        # -0.6

    print(Rational.parse("-12/30"))   # -2/5
    print(Rational.parse("1.125"))    # 9/8
    print(Rational.parse("7"))        # 7
