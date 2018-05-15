import matplotlib.pyplot as plt
import random, numpy as np

def rnd():
    return [random.randint(-10,10) for i in range(3)]

def random_vectors(n):
    ls = []
    for v in range(n):
        ls.append(rnd())
    return ls

def sos(v):
    return sum(v_i ** 2 for v_i in v)

def sos_gradient(v):
    return [2 * v_i for v_i in v]

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

if __name__ == "__main__":
    v, x, y = rnd(), random_vectors(3), random_vectors(3)
    data = list(zip(x, y))
    theta = v
    alpha, value = 0.01, 0
    min_theta, min_value = None, float("inf")
    iterations_with_no_improvement = 0
    n, x = 30, 1
    for i, _ in enumerate(range(n)):
        y = np.linalg.norm(theta)
        plt.scatter(x, y, c='r')
        x = x + 1
        s = []
        for x_i, y_i in data:
            s.extend([sos(theta), sos(x_i), sos(y_i)])
        value = sum(s)
        if value < min_value:
            min_theta, min_value = theta, value
            iterations_with_no_improvement = 0
            alpha = 0.01
        else:
            iterations_with_no_improvement += 1
            alpha *= 0.9
        g = []
        for x_i, y_i in in_random_order(data):
            g.extend([sos_gradient(theta), sos_gradient(x_i),
                      sos_gradient(y_i)])
            for v in g:
                theta = np.around(np.subtract(theta,alpha*np.array(v)),3)
            g = []
    print ('minimum:', np.around(min_theta, 4),
           'with', i+1, 'iterations')
    print ('iterations with no improvement:',
           iterations_with_no_improvement)
    print ('magnitude of min vector:', np.linalg.norm(min_theta))
    plt.show()
