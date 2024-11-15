import numpy as np
import matplotlib.pyplot as plt
from scipy.special import comb


def bernstein(v, n, x):
    return comb(n, v) * (x ** v) * ((1 - x) ** (n - v))


fig, axes = plt.subplots(4, 4, figsize=(12, 12))
x = np.linspace(0, 1, 100)

for n in range(4):
    for v in range(n + 1):
        ax = axes[n, v]
        y = bernstein(v, n, x)
        ax.plot(x, y, color="blue")
        ax.set_title(f"n={n}, v={v}")
        ax.set_xlim(0, 1)
        ax.set_ylim(0, 1)
        ax.set_xticks([0, 0.5, 1])
        ax.set_yticks([0, 0.5, 1])

plt.tight_layout()
plt.show()
