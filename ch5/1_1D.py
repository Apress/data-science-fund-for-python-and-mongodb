import matplotlib.pyplot as plt
import numpy as np
   
if __name__ == "__main__":
    plt.figure('Uniform Distribution')
    uniform = np.random.uniform(-3, 3, 1000)
    count, bins, ignored = plt.hist(uniform, 20, facecolor='lime')
    plt.xlabel('Interval: [-3, 3]')
    plt.ylabel('Frequency')
    plt.title('Uniform Distribution')
    plt.axis([-3,3,0,100])
    plt.grid(True)
    plt.figure('Normal Distribution')
    normal = np.random.normal(0, 1, 1000)
    count, bins, ignored = plt.hist(normal, 20, facecolor='fuchsia')
    plt.xlabel('Interval: [-3, 3]')
    plt.ylabel('Frequency')
    plt.title('Normal Distribution')
    plt.axis([-3,3,0,140])
    plt.grid(True)
    plt.show()
