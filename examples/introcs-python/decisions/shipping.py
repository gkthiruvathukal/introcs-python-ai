def shipping_cost(weight: float, zone: int) -> float:
    """Return shipping cost based on weight (lbs) and zone (1 or 2)."""
    if zone == 1:
        if weight <= 5:
            return 3.99
        else:
            return 3.99 + 0.50 * (weight - 5)
    else:
        if weight <= 5:
            return 6.99
        else:
            return 6.99 + 0.75 * (weight - 5)


if __name__ == '__main__':
    weight = float(input("Weight (lbs): "))
    zone = int(input("Zone (1 or 2): "))
    print(f"Shipping cost: ${shipping_cost(weight, zone):.2f}")
