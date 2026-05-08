# start: mod_mult_table
def mod_mult_table(n: int) -> None:
    """Print the modular multiplication table for mod n."""
    width = len(str(n))
    fmt = f"{{:>{width}}}"
    header = "* | " + " ".join(fmt.format(i) for i in range(n))
    print(header)
    print("-" * len(header))
    for r in range(n):
        row = fmt.format(r) + " | "
        row += " ".join(fmt.format((r * c) % n) for c in range(n))
        print(row)
# end: mod_mult_table


if __name__ == '__main__':
    mod_mult_table(7)
