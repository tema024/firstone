import numpy as np
import matplotlib.pyplot as plt

mean = 0
std = 1

sample_sizes = [10, 50, 100, 500, 1000, 10000]

fig, axes = plt.subplots(nrows=3, ncols=2, figsize=(12, 9))

for i, size in enumerate(sample_sizes):
    row = i // 2
    col = i % 2
    sample = np.random.normal(mean, std, size)
    axes[row, col].hist(sample, bins=size, density = True, alpha=1)
    axes[row, col].set_title(f"n = {size}")

    x = np.linspace(mean - 3 * std, mean + 3 * std, 100)
    axes[row, col].plot(x, 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std ** 2)))

plt.show()
