import numpy as np
import matplotlib.pyplot as plt


def rosenbrock(x, y):
    return (1 - x) ** 2 + 100 * (y - x ** 2) ** 2


x = np.linspace(-2, 2, 400)
y = np.linspace(-1, 3, 400)
X, Y = np.meshgrid(x, y)
Z = rosenbrock(X, Y)

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

heatmap = ax1.pcolormesh(X, Y, Z, shading="auto", cmap="viridis")
fig.colorbar(heatmap, ax=ax1, label="f(x, y)")
ax1.scatter(1, 1, color="red", label="Minimum (1,1)")
ax1.set_xlabel("x")
ax1.set_ylabel("y")
ax1.set_title("Heat Map of Rosenbrock Function")
ax1.legend()

contours = ax2.contour(X, Y, Z, levels=20, cmap="plasma")
ax2.clabel(contours, inline=True, fontsize=8)
ax2.scatter(1, 1, color="red", label="Minimum (1,1)")
ax2.set_xlabel("x")
ax2.set_ylabel("y")
ax2.set_title("Contour Plot of Rosenbrock Function")
ax2.legend()

plt.tight_layout()
plt.show()
