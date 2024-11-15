import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# data = np.array([
#     [10, 8.04, 10, 9.14, 10, 7.46, 8, 6.58],
#     [8, 6.95, 8, 8.14, 8, 6.77, 8, 5.76],
#     [13, 7.58, 13, 8.74, 13, 12.74, 8, 7.71],
#     [9, 8.81, 9, 8.77, 9, 7.11, 8, 8.84],
#     [11, 8.33, 11, 9.26, 11, 7.81, 8, 8.47],
#     [14, 9.96, 14, 8.10, 14, 8.84, 8, 7.04],
#     [6, 7.24, 6, 6.13, 6, 6.08, 8, 5.25],
#     [4, 4.26, 4, 3.10, 4, 5.39, 19, 12.50],
#     [12, 10.84, 12, 9.13, 12, 8.15, 8, 5.56],
#     [7, 4.82, 7, 7.26, 7, 6.42, 8, 7.91],
#     [5, 5.68, 5, 4.74, 5, 5.73, 8, 6.89]
# ])
#
# np.save("problem1.npy", data)


data = np.load("problem1.npy")

x_range = np.linspace(0, 20, 100)

titles = ["Group I", "Group II", "Group III", "Group IV"]

fig, axes = plt.subplots(2, 2, figsize=(10, 10))
axes = axes.flatten()

for i in range(4):
    x = data[:, 2 * i]
    y = data[:, 2 * i + 1]

    slope, intercept, r_value, _, _ = linregress(x, y)
    regression_line = slope * x_range + intercept

    mean_x, mean_y = np.mean(x), np.mean(y)
    var_x, var_y = np.var(x), np.var(y)

    ax = axes[i]
    ax.scatter(x, y, label="Data points", color="blue")
    ax.plot(x_range, regression_line, color="red", label=f"y={slope:.2f}x+{intercept:.2f}")
    ax.set_xlim(0, 20)
    ax.set_ylim(0, 13)
    ax.set_title(titles[i])
    ax.legend()

    print(f"{titles[i]}:")
    print(f"  Mean of x: {mean_x:.2f}, Variance of x: {var_x:.2f}")
    print(f"  Mean of y: {mean_y:.2f}, Variance of y: {var_y:.2f}")
    print(f"  Slope: {slope:.2f}, Intercept: {intercept:.2f}, Correlation: {r_value:.2f}")
    print()

plt.tight_layout()
plt.show()
