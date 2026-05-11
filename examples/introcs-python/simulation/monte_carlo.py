import random
import csv


# start: generate_darts
def generate_darts(n: int) -> list[dict]:
    """Generate n random darts thrown at the 2x2 square [-1,1] x [-1,1]."""
    darts = []
    for _ in range(n):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        inside = x * x + y * y <= 1.0
        darts.append({'x': x, 'y': y, 'inside': inside})
    return darts
# end: generate_darts


# start: estimate_pi
def estimate_pi(darts: list[dict]) -> float:
    """Estimate pi from dart throws: 4 * (inside / total)."""
    inside = sum(1 for d in darts if d['inside'])
    return 4.0 * inside / len(darts)
# end: estimate_pi


# start: save_darts
def save_darts(darts: list[dict], filename: str = 'darts.csv') -> None:
    """Save dart throws to a CSV file with columns x, y, inside."""
    with open(filename, 'w', newline='') as f:
        writer = csv.DictWriter(f, fieldnames=['x', 'y', 'inside'])
        writer.writeheader()
        writer.writerows(darts)
# end: save_darts


# start: convergence
def convergence_table(sizes: list[int]) -> None:
    """Print how the pi estimate improves as n grows."""
    print(f"{'n':>10}  {'π estimate':>12}  {'error':>10}")
    print("-" * 38)
    for n in sizes:
        darts = generate_darts(n)
        estimate = estimate_pi(darts)
        print(f"{n:>10,}  {estimate:>12.6f}  {abs(estimate - 3.141593):>10.6f}")
# end: convergence


if __name__ == '__main__':
    import argparse
    import math

    parser = argparse.ArgumentParser(
        description='Monte Carlo π estimator.'
    )
    parser.add_argument('-n', '--darts', type=int, default=100_000,
                        help='Number of darts to throw (default: 100000)')
    parser.add_argument('--save', metavar='FILE',
                        help='Save dart data to a CSV file')
    parser.add_argument('--convergence', action='store_true',
                        help='Print a convergence table across several dart counts')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for reproducibility')
    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    darts = generate_darts(args.darts)
    estimate = estimate_pi(darts)
    print(f"π ≈ {estimate:.6f}  (true: {math.pi:.6f})")

    if args.save:
        save_darts(darts, args.save)
        print(f"Darts saved to {args.save}")

    if args.convergence:
        convergence_table([100, 1_000, 10_000, 100_000, 1_000_000])
