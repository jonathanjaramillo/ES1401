"""Generate a noisy range-sensor example and a first-order low-pass plot.

Run with:
    .venv/bin/python scripts/generate_range_filter_demo.py

The random seed makes the classroom example repeatable.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def generate_range_data(seed: int = 606) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return time, true range, and noisy sensor readings in inches."""
    rng = np.random.default_rng(seed)
    time = np.arange(0.0, 12.0, 0.1)

    # The robot is still, then approaches a wall at a steady speed.
    true_range = np.where(time < 3.0, 18.0, 18.0 - (time - 3.0) * 12.0 / 9.0)
    noisy_range = true_range + rng.normal(0.0, 0.45, size=time.size)

    # A few occasional echoes make the benefit of filtering easy to see.
    for seconds, glitch in ((4.6, 2.2), (7.1, -2.5), (9.4, 2.0)):
        noisy_range[np.argmin(np.abs(time - seconds))] += glitch

    return time, true_range, noisy_range


def low_pass_filter(readings: np.ndarray, alpha: float = 0.2) -> np.ndarray:
    """Apply y += alpha * (x - y) to a sequence of readings."""
    filtered = np.empty_like(readings)
    filtered[0] = readings[0]

    for index in range(1, len(readings)):
        filtered[index] = filtered[index - 1] + alpha * (
            readings[index] - filtered[index - 1]
        )

    return filtered


def plot_demo(output_path: Path) -> None:
    time, true_range, noisy_range = generate_range_data()
    filtered_range = low_pass_filter(noisy_range, alpha=0.2)

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "text.color": "#eef6ff",
            "axes.labelcolor": "#cbd5e1",
            "xtick.color": "#94a3b8",
            "ytick.color": "#94a3b8",
        }
    )

    figure, axis = plt.subplots(figsize=(10.5, 4.8), dpi=200)
    figure.patch.set_facecolor("#020617")
    axis.set_facecolor("#0f172a")

    axis.plot(
        time,
        noisy_range,
        color="#94a3b8",
        linewidth=1.4,
        alpha=0.9,
        label="raw sensor",
    )
    axis.plot(
        time,
        true_range,
        color="#f8fbff",
        linewidth=2.0,
        linestyle=(0, (5, 4)),
        alpha=0.85,
        label="true range",
    )
    axis.plot(
        time,
        filtered_range,
        color="#2dd4bf",
        linewidth=3.0,
        label="low-pass (α = 0.2)",
    )
    axis.axhline(
        6.0,
        color="#fb923c",
        linewidth=1.8,
        linestyle=(0, (4, 4)),
        label="stop threshold",
    )

    axis.set_title("Fake range sensor: noisy input → filtered estimate", loc="left", pad=12, fontweight="bold")
    axis.set_xlabel("time (s)")
    axis.set_ylabel("distance (in)")
    axis.set_xlim(0, 11.9)
    axis.set_ylim(3.5, 21.0)
    axis.grid(color="#64748b", alpha=0.22, linewidth=0.8)
    axis.spines[:].set_color("#334155")
    axis.legend(
        loc="upper right",
        frameon=True,
        facecolor="#111827",
        edgecolor="#475569",
        labelcolor="#eef6ff",
        fontsize=8.5,
    )
    figure.tight_layout(pad=1.2)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    figure.savefig(output_path, facecolor=figure.get_facecolor(), bbox_inches="tight")
    plt.close(figure)


if __name__ == "__main__":
    project_root = Path(__file__).resolve().parents[1]
    plot_demo(project_root / "public" / "range_low_pass_demo.png")
