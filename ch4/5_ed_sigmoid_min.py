import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import random, numpy as np
from scipy.spatial import distance

def step(v, direction, step_size):
    return [v_i + step_size * direction_i
            for v_i, direction_i in zip(v, direction)]

def sigmoid_gradient(v):
    return [v_i * (1-v_i) for v_i in v] 

def mod_vector(v):
    for i, v_i in enumerate(v):
        if v_i == float("inf") or v_i == float("-inf"):
            v[i] = random.randint(-1, 1)
    return v

if __name__ == "__main__":
    v = [random.randint(-10, 10) for i in range(3)]
    tolerance = 0.0000001
    iterations = 1
    fig = plt.figure('Euclidean')
    ax = fig.add_subplot(111, projection='3d')
    while True:
        gradient = sigmoid_gradient(v)
        next_v = step(v, gradient, -0.01)
        xs = gradient[0]
        ys = gradient[1]
        zs = gradient[2]
        ax.scatter(xs, ys, zs, c='lime', marker='o')
        v = mod_vector(v)
        next_v = mod_vector(next_v)
        test_v = distance.euclidean(v, next_v)
        if test_v < tolerance:
            break
        v = next_v
        iterations += 1
    print ('minimum:', test_v, '\niterations:', iterations)
    ax.set_xlabel('X axis')
    ax.set_ylabel('Y axis')
    ax.set_zlabel('Z axis')
    plt.tight_layout()
    plt.show()
