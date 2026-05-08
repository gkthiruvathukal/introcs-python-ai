# start: weekly_wages
def weekly_wages(hours: float, rate: float) -> float:
    """Return total weekly wages including 1.5x overtime above 40 hours."""
    if hours <= 40:
        return hours * rate
    return 40 * rate + (hours - 40) * rate * 1.5
# end: weekly_wages


def main() -> None:
    hours = float(input("Hours worked: "))
    rate = float(input("Hourly rate: $"))
    pay = weekly_wages(hours, rate)
    print(f"Weekly wages: ${pay:.2f}")


if __name__ == '__main__':
    main()
