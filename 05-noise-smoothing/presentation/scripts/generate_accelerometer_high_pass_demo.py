"""Generate noisy accelerometer data and a high-pass collision-detection plot.

Run with:
    .venv/bin/python scripts/generate_accelerometer_high_pass_demo.py

The random seed makes the classroom example repeatable.
"""

from pathlib import Path

import matplotlib

matplotlib.use("Agg")

import matplotlib.pyplot as plt
import numpy as np


def generate_accelerometer_data(
    seed: int = 752,
) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    """Return time, accelerometer readings, and slow low-frequency drift."""
    rng = np.random.default_rng(seed)
    time = np.arange(0.0, 8.0, 0.01)

    # Slow motion or tilt changes the reading over several seconds.
    slow_drift = (
        1.7 * np.sin(2 * np.pi * time / 6.5)
        + 0.8 * np.sin(2 * np.pi * time / 2.8)
    )
    noise = rng.normal(0.0, 0.12, size=time.size)

    # A short collision impulse creates a sudden change in the measurement.
    impact = 8.0 * np.exp(-0.5 * ((time - 4.2) / 0.045) ** 2)
    rebound = -3.0 * np.exp(-0.5 * ((time - 4.34) / 0.06) ** 2)
    acceleration = slow_drift + noise + impact + rebound

    return time, acceleration, slow_drift


def high_pass_filter(readings: np.ndarray, beta: float = 0.8) -> np.ndarray:
    """Apply y = beta * (previous y + input change) to sensor readings."""
    filtered = np.zeros_like(readings)

    for index in range(1, len(readings)):
        filtered[index] = beta * (
            filtered[index - 1] + readings[index] - readings[index - 1]
        )

    return filtered


def plot_demo(output_path: Path) -> None:
    time, acceleration, slow_drift = generate_accelerometer_data()
    change = high_pass_filter(acceleration, beta=0.8)
    detection_threshold = 1.5

    plt.rcParams.update(
        {
            "font.family": "DejaVu Sans",
            "text.color": "#eef6ff",
            "axes.labelcolor": "#cbd5e1",
            "xtick.color": "#94a3b8",
            "ytick.color": "#94a3b8",
        }
    )

    figure, axes = plt.subplots(
        2,
        1,
        sharex=True,
        figsize=(10.5, 5.7),
        dpi=200,
        gridspec_kw={"height_ratios": [1, 1.15]},
    )
    figure.patch.set_facecolor("#020617")

    for axis in axes:
        axis.set_facecolor("#0f172a")
        axis.grid(color="#64748b", alpha=0.22, linewidth=0.8)
        axis.spines[:].set_color("#334155")
        axis.axvspan(4.05, 4.5, color="#fb923c", alpha=0.08)

    axes[0].plot(
        time,
        acceleration,
        color="#94a3b8",
        linewidth=1.25,
        label="raw accelerometer",
    )
    axes[0].plot(
        time,
        slow_drift,
        color="#f8fbff",
        linewidth=1.8,
        linestyle=(0, (5, 4)),
        alpha=0.8,
        label="low-frequency drift",
    )
    axes[0].axhline(detection_threshold, color="#fb923c", linewidth=1.7, linestyle=(0, (4, 4)), label="raw threshold ±1.5")
    axes[0].axhline(-detection_threshold, color="#fb923c", linewidth=1.7, linestyle=(0, (4, 4)))
    axes[0].set_ylabel("acceleration (m/s²)")
    axes[0].set_ylim(-3.5, 8.5)
    axes[0].set_title("Slow drift hides a sudden collision", loc="left", pad=10, fontweight="bold")
    axes[0].legend(
        loc="upper right",
        frameon=True,
        facecolor="#111827",
        edgecolor="#475569",
        labelcolor="#eef6ff",
        fontsize=8.5,
    )

    axes[1].plot(
        time,
        change,
        color="#a78bfa",
        linewidth=2.5,
        label="high-pass output (β = 0.8)",
    )
    axes[1].axhline(
        detection_threshold,
        color="#fb923c",
        linewidth=1.7,
        linestyle=(0, (4, 4)),
        label="collision threshold",
    )
    axes[1].axhline(-detection_threshold, color="#fb923c", linewidth=1.7, linestyle=(0, (4, 4)))
    axes[1].set_xlabel("time (s)")
    axes[1].set_ylabel("change signal")
    axes[1].set_ylim(-4.0, 6.0)
    axes[1].legend(
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
    plot_demo(project_root / "public" / "accelerometer_high_pass_demo.png")
