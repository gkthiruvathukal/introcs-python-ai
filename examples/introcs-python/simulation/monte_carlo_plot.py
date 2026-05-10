import math
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


if __name__ == '__main__':
    darts = generate_darts(20_000)
    plot_darts(darts)
