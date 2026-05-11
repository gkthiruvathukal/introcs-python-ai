import math
import random
import time
import matplotlib.pyplot as plt
from monte_carlo import generate_darts, estimate_pi


# start: plot_darts
def plot_darts(darts: list[dict], filename: str = 'darts.png') -> None:
    """Scatter-plot dart throws, coloring inside/outside the circle differently."""
    inside_x  = [d['x'] for d in darts if     d['inside']]
    inside_y  = [d['y'] for d in darts if     d['inside']]
    outside_x = [d['x'] for d in darts if not d['inside']]
    outside_y = [d['y'] for d in darts if not d['inside']]

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.scatter(inside_x,  inside_y,  s=0.5, color='steelblue', alpha=0.4, label='inside')
    ax.scatter(outside_x, outside_y, s=0.5, color='salmon',    alpha=0.4, label='outside')

    theta = [math.tau * i / 1000 for i in range(1001)]
    ax.plot([math.cos(t) for t in theta], [math.sin(t) for t in theta],
            'k-', linewidth=1.5)

    pi_est = estimate_pi(darts)
    ax.set_aspect('equal')
    ax.set_title(f'Monte Carlo: π ≈ {pi_est:.5f}  (n = {len(darts):,})')
    ax.legend(markerscale=8, loc='lower right')
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    plt.close()
    print(f"Saved {filename}")
# end: plot_darts


# start: sample_and_estimate
def _sample_and_estimate(n: int, max_display: int,
                          chunk_size: int = 10_000_000) -> tuple[float, list[dict]]:
    """Return (pi_estimate, display_sample) for n darts.

    Processes in chunks of chunk_size so arbitrarily large n never requires
    more than ~160 MB of working memory (two float64 arrays of chunk_size).
    The display sample is taken from the first chunk.
    """
    import numpy as np

    inside_total = 0
    sample: list[dict] = []
    remaining = n

    while remaining > 0:
        chunk = min(chunk_size, remaining)
        x = np.random.uniform(-1.0, 1.0, chunk)
        y = np.random.uniform(-1.0, 1.0, chunk)
        mask = x * x + y * y <= 1.0
        inside_total += int(mask.sum())

        if len(sample) < max_display:
            k = min(chunk, max_display - len(sample))
            sample.extend(
                {'x': float(x[i]), 'y': float(y[i]), 'inside': bool(mask[i])}
                for i in range(k)
            )

        remaining -= chunk

    return 4.0 * inside_total / n, sample
# end: sample_and_estimate


# start: plot_convergence_grid
def plot_convergence_grid(sizes: list[int],
                           filename: str = 'convergence_grid.png',
                           max_display: int = 50_000) -> None:
    """Grid of scatter plots showing dart throws at multiple scales.

    The layout is determined automatically from the number of sizes.
    Pi is estimated from all n darts; only max_display points are plotted
    per panel so large n renders quickly.
    """
    if len(sizes) <= 3:
        cols, rows = len(sizes), 1
    else:
        cols = math.ceil(math.sqrt(len(sizes)))
        rows = math.ceil(len(sizes) / cols)
    theta = [math.tau * i / 1000 for i in range(1001)]
    cos_t = [math.cos(t) for t in theta]
    sin_t = [math.sin(t) for t in theta]

    fig, axes = plt.subplots(rows, cols, figsize=(5 * cols, 5 * rows))
    ax_list = list(axes.flat)

    for ax, n in zip(ax_list, sizes):
        print(f"  generating n={n:,} ...", flush=True)
        t0 = time.perf_counter()
        pi_est, sample = _sample_and_estimate(n, max_display)
        elapsed = time.perf_counter() - t0

        inside_x  = [d['x'] for d in sample if     d['inside']]
        inside_y  = [d['y'] for d in sample if     d['inside']]
        outside_x = [d['x'] for d in sample if not d['inside']]
        outside_y = [d['y'] for d in sample if not d['inside']]

        pt_size = max(0.3, 10 / (math.log10(n) ** 1.5))
        alpha   = max(0.15, 0.7 - 0.1 * math.log10(n))

        ax.scatter(inside_x,  inside_y,  s=pt_size, color='steelblue', alpha=alpha)
        ax.scatter(outside_x, outside_y, s=pt_size, color='salmon',    alpha=alpha)
        ax.plot(cos_t, sin_t, 'k-', linewidth=1.0)
        ax.set_aspect('equal')
        ax.set_xlim(-1.05, 1.05)
        ax.set_ylim(-1.05, 1.05)
        ax.set_title(f'n = {n:,}   π ≈ {pi_est:.5f}   t = {elapsed:.2f}s', fontsize=12)
        ax.set_xticks([])
        ax.set_yticks([])

    for ax in ax_list[len(sizes):]:
        ax.set_visible(False)

    fig.suptitle('Monte Carlo Estimation of π', fontsize=14)
    plt.tight_layout()
    plt.savefig(filename, dpi=100)
    plt.close()
    print(f"Saved {filename}")
# end: plot_convergence_grid


if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(
        description='Monte Carlo dart-throw visualizations.'
    )
    sub = parser.add_subparsers(dest='command', required=True)

    p_scatter = sub.add_parser('scatter', help='Single scatter plot of dart throws.')
    p_scatter.add_argument('-n', '--darts', type=int, default=20_000,
                           help='Number of darts (default: 20000)')
    p_scatter.add_argument('-o', '--output', default='darts.png')
    p_scatter.add_argument('--seed', type=int, default=None)

    p_grid = sub.add_parser('grid', help='Convergence grid at multiple scales.')
    p_grid.add_argument('--sizes', type=int, nargs='+',
                        default=[100, 1_000, 100_000, 1_000_000,
                                 10_000_000, 100_000_000,
                                 1_000_000_000, 10_000_000_000],
                        metavar='N',
                        help='Dart counts for each panel (default: 6 sizes from 100 to 100M)')
    p_grid.add_argument('-o', '--output', default='convergence_grid.png')
    p_grid.add_argument('--max-display', type=int, default=50_000,
                        help='Max points plotted per panel (default: 50000)')
    p_grid.add_argument('--seed', type=int, default=None)

    args = parser.parse_args()

    if args.seed is not None:
        random.seed(args.seed)

    if args.command == 'scatter':
        darts = generate_darts(args.darts)
        plot_darts(darts, args.output)

    elif args.command == 'grid':
        plot_convergence_grid(args.sizes, args.output, args.max_display)
