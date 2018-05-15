import matplotlib.pyplot as plt
import random, numpy as np

def rnd():
    return [random.randint(-10,10) for i in range(3)]

def random_vectors(n):
    ls = []
    for v in range(n):
        ls.append([random.randint(-10,10) for i in range(3)])
    return ls

def sos_gradient(v):
    return [2 * v_i for v_i in v]

def negate(function):
    def new_function(*args, **kwargs):
        return np.negative(function(*args, **kwargs))
    return new_function

def in_random_order(data):
    indexes = [i for i, _ in enumerate(data)]
    random.shuffle(indexes)
    for i in indexes:
        yield data[i]

if __name__ == "__main__":
    v, x, y = rnd(), random_vectors(3), random_vectors(3)
    data = list(zip(x, y))
    theta, alpha = v, 0.01
    neg_gradient = negate(sos_gradient)
    n, x = 1000, 1
    for i, row in enumerate(range(n)):
        y = np.linalg.norm(theta)
        plt.scatter(x, y, c='r')
        x = x + 1
        g = []
        for x_i, y_i in in_random_order(data):
            g.extend([neg_gradient(theta), neg_gradient(x_i),
                      neg_gradient(y_i)])
            for v in g:
                theta = np.around(np.subtract(theta,alpha*np.array(v)),3)
            g = []
    print ('maximum:', np.around(theta, 4),
           'with', i+1, 'iterations')
    print ('magnitude of max vector:', np.linalg.norm(theta))
    plt.show()
