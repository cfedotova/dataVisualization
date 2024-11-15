import numpy as np
import matplotlib.pyplot as plt

# np.random.seed(0)
# years = np.random.uniform(2000, 2010, 17000)
# magnitudes = np.random.uniform(5.0, 9.0, 17000)
# longitudes = np.random.uniform(-180, 180, 17000)
# latitudes = np.random.uniform(-90, 90, 17000)
#
# data = np.column_stack((years, magnitudes, longitudes, latitudes))
#
# np.save("problem4.npy", data)

data = np.load("problem4.npy")
years, magnitudes, longitudes, latitudes = data[:, 0], data[:, 1], data[:, 2], data[:, 3]

plt.figure(figsize=(10, 6))
plt.hist(years, bins=np.arange(2000, 2011), color="skyblue", edgecolor="black")
plt.xlabel("Year")
plt.ylabel("Number of Earthquakes")
plt.title("Number of Earthquakes Each Year (2000-2010)")
plt.show()

plt.figure(figsize=(10, 6))
plt.hist(magnitudes, bins=20, color="salmon", edgecolor="black")
plt.xlabel("Magnitude")
plt.ylabel("Frequency")
plt.title("Frequency of Earthquakes by Magnitude")
plt.show()

plt.figure(figsize=(10, 6))
plt.scatter(longitudes, latitudes, c=magnitudes, cmap="viridis", alpha=0.5, edgecolor="none")
plt.colorbar(label="Magnitude")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("Geographic Distribution of Earthquakes (2000-2010)")
plt.axis("equal")
plt.show()
