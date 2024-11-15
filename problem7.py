import numpy as np
import matplotlib.pyplot as plt

data = np.load("problem5and7.npy")
populations, gdps, male_heights, female_heights = data[:, 0], data[:, 1], data[:, 2], data[:, 3]
countries = ["Austria", "Bolivia", "Brazil", "China", "Finland", "Germany", "Hungary",
             "India", "Japan", "North Korea", "Montenegro", "Norway", "Peru", "South Korea",
             "Sri Lanka", "Switzerland", "Turkey", "United Kingdom", "United States", "Vietnam"]

gdp_per_capita = gdps / populations
sorted_indices = np.argsort(gdp_per_capita)
sorted_countries = [countries[i] for i in sorted_indices]
sorted_gdp_per_capita = gdp_per_capita[sorted_indices]
sorted_populations = populations[sorted_indices]

fig, axes = plt.subplots(2, 2, figsize=(16, 12))

axes[0, 0].barh(sorted_countries, sorted_gdp_per_capita, color="skyblue")
axes[0, 0].set_xlabel("GDP per Capita (thousands USD)")
axes[0, 0].set_title("GDP per Capita by Country")
axes[0, 0].grid(axis="x", linestyle="--", alpha=0.7)

axes[0, 1].hist(male_heights, bins=10, color="blue", alpha=0.6, label="Male Height")
axes[0, 1].hist(female_heights, bins=10, color="pink", alpha=0.6, label="Female Height")
axes[0, 1].set_xlabel("Height (cm)")
axes[0, 1].set_ylabel("Frequency")
axes[0, 1].set_title("Distribution of Average Heights by Gender")
axes[0, 1].legend()

axes[1, 0].bar(sorted_countries, sorted_populations, color="lightgreen")
axes[1, 0].set_xlabel("Country")
axes[1, 0].set_ylabel("Population (millions)")
axes[1, 0].set_title("Population of Countries")
axes[1, 0].tick_params(axis="x", rotation=90)
axes[1, 0].grid(axis="y", linestyle="--", alpha=0.7)

axes[1, 1].scatter(male_heights, gdps, color="purple", alpha=0.7)
axes[1, 1].set_xlabel("Average Male Height (cm)")
axes[1, 1].set_ylabel("GDP (billions USD)")
axes[1, 1].set_title("GDP vs. Average Male Height")
axes[1, 1].grid(True, linestyle="--", alpha=0.5)

plt.tight_layout()
plt.show()