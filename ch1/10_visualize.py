import matplotlib.pyplot as plt
from scipy.stats import norm
import numpy as np

if __name__ == '__main__':
    x = np.linspace(norm.ppf(0.01), norm.ppf(0.99), num=1000)
    x_left = x - 1
    x_right = x + 1
    y = norm.pdf(x)
    plt.ylim(0.02, 0.41)
    plt.scatter(x, y, color='crimson')
    plt.fill_between(x, y, color='crimson')
    plt.scatter(x_left, y, color='chartreuse')
    plt.scatter(x_right, y, color='cyan')
    plt.show()
