import random
import math
import pandas as pd


# start: generate_darts
def generate_darts(n: int) -> pd.DataFrame:
    """Generate n random darts thrown at the 2×2 square [−1,1]×[−1,1]."""
    x = [random.uniform(-1, 1) for _ in range(n)]
    y = [random.uniform(-1, 1) for _ in range(n)]
    inside = [xi * xi + yi * yi <= 1.0 for xi, yi in zip(x, y)]
    return pd.DataFrame({'x': x, 'y': y, 'inside': inside})
# end: generate_darts


# start: estimate_pi
def estimate_pi(darts: pd.DataFrame) -> float:
    """Estimate pi from dart throws: 4 × (inside / total)."""
    return 4.0 * darts["inside"].sum() / len(darts)
# end: estimate_pi


# start: save_darts
def save_darts(darts: pd.DataFrame, filename: str = 'darts.csv') -> None:
    """Save dart throws to a CSV file with columns x, y, inside."""
    darts.to_csv(filename, index=False)
# end: save_darts


# start: load_darts
def load_darts(filename: str) -> pd.DataFrame:
    """Load a previously saved darts CSV back into a DataFrame."""
    return pd.read_csv(filename)
# end: load_darts


# start: convergence
def convergence_table(sizes: list[int]) -> None:
    """Print how the pi estimate improves as n grows."""
    print(f"{'n':>10}  {'π estimate':>12}  {'error':>10}")
    print("-" * 38)
    for n in sizes:
        darts = generate_darts(n)
        estimate = estimate_pi(darts)
        print(f"{n:>10,}  {estimate:>12.6f}  {abs(estimate - math.pi):>10.6f}")
# end: convergence


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Monte Carlo π estimator.'
    )
    parser.add_argument('-n', '--darts', type=int, default=100_000,
                        help='Number of darts to throw (default: 100000)')
    parser.add_argument('--save', metavar='FILE',
                        help='Save dart data to a CSV file')
    parser.add_argument('--load', metavar='FILE',
                        help='Load darts from a CSV file instead of generating')
    parser.add_argument('--convergence', action='store_true',
                        help='Print a convergence table across several dart counts')
    parser.add_argument('--seed', type=int, default=None,
                        help='Random seed for reproducibility')
    args = parser.parse_args()

    if args.load:
        darts = load_darts(args.load)
        print(f"Loaded {len(darts):,} darts from {args.load}")
    else:
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
