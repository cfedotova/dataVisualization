import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# np.random.seed(0)
# heights = np.random.normal(72, 3, 1000)
# weights = np.random.normal(200, 25, 1000)
# ages = np.random.normal(28, 5, 1000)
#
# data = np.column_stack((heights, weights, ages))
# np.save("problem3.npy", data)

data = np.load("problem3.npy")
heights, weights, ages = data[:, 0], data[:, 1], data[:, 2]
fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].scatter(heights, weights, alpha=0.5, edgecolor="none")
axes[0, 0].set_xlabel("Height (inches)")
axes[0, 0].set_ylabel("Weight (pounds)")
axes[0, 0].set_title("Scatter Plot of Height vs Weight")

slope, intercept, r_value, _, _ = linregress(heights, weights)
x_vals = np.linspace(min(heights), max(heights), 100)
axes[0, 0].plot(x_vals, slope * x_vals + intercept, color="red",
                label=f"y={slope:.2f}x+{intercept:.2f}, r^2={r_value ** 2:.2f}")
axes[0, 0].legend()

axes[0, 1].hist(heights, bins=20, color="skyblue", edgecolor="black")
axes[0, 1].set_xlabel("Height (inches)")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Histogram of Heights")

axes[1, 0].hist(weights, bins=20, color="lightgreen", edgecolor="black")
axes[1, 0].set_xlabel("Weight (pounds)")
axes[1, 0].set_ylabel("Frequency")
axes[1, 0].set_title("Histogram of Weights")

axes[1, 1].hist(ages, bins=20, color="salmon", edgecolor="black")
axes[1, 1].set_xlabel("Age (years)")
axes[1, 1].set_ylabel("Frequency")
axes[1, 1].set_title("Histogram of Ages")

plt.tight_layout()
plt.show()
