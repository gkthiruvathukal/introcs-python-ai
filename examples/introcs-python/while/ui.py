# start: prompt_int_float
def prompt_int(message: str) -> int:
    """Keep prompting until the user enters a valid integer."""
    while True:
        try:
            return int(input(message))
        except ValueError:
            print("Please enter a whole number.")


def prompt_float(message: str) -> float:
    """Keep prompting until the user enters a valid float."""
    while True:
        try:
            return float(input(message))
        except ValueError:
            print("Please enter a number.")
# end: prompt_int_float


# start: prompt_int_in_range
def prompt_int_in_range(message: str, low: int, high: int) -> int:
    """Keep prompting until the user enters an integer in [low, high]."""
    while True:
        value = prompt_int(message)
        if low <= value <= high:
            return value
        print(f"{value} is out of range!  Enter a value from {low} to {high}.")
# end: prompt_int_in_range


# start: prompt_yes_no
def prompt_yes_no(message: str) -> bool:
    """Return True if user answers yes, False if no."""
    while True:
        answer = input(message + " (yes/no): ").strip().lower()
        if answer in ("yes", "y"):
            return True
        if answer in ("no", "n"):
            return False
        print("Please answer yes or no.")
# end: prompt_yes_no


if __name__ == '__main__':
    age = prompt_int("Enter your age: ")
    score = prompt_int_in_range("Enter score (0-100): ", 0, 100)
    if prompt_yes_no("Save result?"):
        print(f"Saved: age={age}, score={score}")
