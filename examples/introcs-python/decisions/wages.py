def weekly_wages(hours: float, rate: float) -> float:
    """Return total weekly wages including 1.5x overtime above 40 hours."""
    if hours <= 40:
        return hours * rate
    else:
        overtime = hours - 40
        return 40 * rate + overtime * rate * 1.5


if __name__ == '__main__':
    hours = float(input("Hours worked: "))
    rate = float(input("Hourly rate: $"))
    print(f"Weekly wages: ${weekly_wages(hours, rate):.2f}")
