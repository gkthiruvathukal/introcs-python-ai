import pytest
from rational import Rational


# start: basic_tests
def test_normalisation() -> None:
    r = Rational(6, -10)
    assert str(r) == "-3/5"

def test_addition() -> None:
    f = Rational(-3, 5)
    h = Rational(1, 2)
    assert str(f + h) == "-1/10"

def test_multiplication() -> None:
    assert Rational(2, 3) * Rational(3, 4) == Rational(1, 2)

def test_equality() -> None:
    assert Rational(2, 4) == Rational(1, 2)
    assert Rational(1, 3) != Rational(1, 4)

def test_whole_number() -> None:
    assert str(Rational(6, 3)) == "2"

def test_float_conversion() -> None:
    assert float(Rational(1, 4)) == 0.25
# end: basic_tests


def test_zero_denominator() -> None:
    with pytest.raises(ValueError):
        Rational(1, 0)


# start: edge_case_tests
def test_add_zero() -> None:
    r = Rational(3, 4)
    assert r + Rational(0, 1) == r

def test_multiply_by_one() -> None:
    r = Rational(3, 4)
    assert r * Rational(1) == r

def test_negative_numerator_and_denominator() -> None:
    assert str(Rational(-2, -3)) == "2/3"
# end: edge_case_tests


# start: test_classes
class TestRationalArithmetic:
    def test_add(self) -> None:
        assert Rational(1, 3) + Rational(1, 6) == Rational(1, 2)

    def test_sub(self) -> None:
        assert Rational(3, 4) - Rational(1, 4) == Rational(1, 2)


class TestRationalComparison:
    def test_less_than(self) -> None:
        assert Rational(1, 3) < Rational(1, 2)
# end: test_classes
