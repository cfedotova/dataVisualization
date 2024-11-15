import numpy as np
import matplotlib.pyplot as plt

# populations = np.random.uniform(1, 300, 20)
# gdps = np.random.uniform(10, 2000, 20)
# male_heights = np.random.uniform(160, 185, 20)
# female_heights = np.random.uniform(150, 175, 20)
#
# data = np.column_stack((populations, gdps, male_heights, female_heights))
# np.save("problem5and7.npy", data)

data = np.load("problem5and7.npy")
populations, gdps, male_heights, female_heights = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
countries = ["Austria", "Bolivia", "Brazil", "China", "Finland", "Germany", "Hungary",
             "India", "Japan", "North Korea", "Montenegro", "Norway", "Peru", "South Korea",
             "Sri Lanka", "Switzerland", "Turkey", "United Kingdom", "United States", "Vietnam"]

fig, axes = plt.subplots(2, 2, figsize=(12, 10))

axes[0, 0].hist(populations, bins=10, color="skyblue", edgecolor="black")
axes[0, 0].set_xlabel("Population (millions)")
axes[0, 0].set_ylabel("Frequency")
axes[0, 0].set_title("Histogram of Population Sizes")

axes[0, 1].hist(gdps, bins=10, color="salmon", edgecolor="black")
axes[0, 1].set_xlabel("GDP (billions USD)")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Histogram of GDP")

x = np.arange(len(countries))
width = 0.4
axes[1, 0].bar(x - width / 2, male_heights, width, label="Male Height", color="lightblue")
axes[1, 0].bar(x + width / 2, female_heights, width, label="Female Height", color="lightpink")
axes[1, 0].set_xlabel("Country")
axes[1, 0].set_ylabel("Average Height (cm)")
axes[1, 0].set_title("Average Male and Female Height by Country")
axes[1, 0].set_xticks(x)
axes[1, 0].set_xticklabels(countries, rotation=90)
axes[1, 0].legend()

axes[1, 1].scatter(populations, gdps, color="green", alpha=0.5)
axes[1, 1].set_xlabel("Population (millions)")
axes[1, 1].set_ylabel("GDP (billions USD)")
axes[1, 1].set_title("Scatter Plot of GDP vs Population")

plt.tight_layout()
plt.show()
