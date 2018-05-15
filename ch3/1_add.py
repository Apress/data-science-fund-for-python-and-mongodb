import matplotlib.pyplot as plt, numpy as np

def vector_add(a, b):
    return np.add(a, b)

def set_up():
    plt.figure()
    plt.xlim(-.05, add_vectors[0]+0.4)
    plt.ylim(-1.1, add_vectors[1]+0.4)

if __name__ == "__main__":
    v1, v2 = np.array([3, -1]), np.array([2, 3])
    add_vectors = vector_add(v1, v2)
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc='b', ec='b')
    ax.text(1.5, -0.35, 'a')
    ax.set_facecolor('honeydew')
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc='b', ec='b')
    ax.arrow(3, -1, 2, 3, head_width=0.1, fc='crimson', ec='crimson')
    ax.text(1.5, -0.35, 'a')
    ax.text(4, -0.1, 'b')
    ax.set_facecolor('honeydew')
    set_up()
    ax = plt.axes()
    ax.arrow(0, 0, 3, -1, head_width=0.1, fc='b', ec='b')
    ax.arrow(3, -1, 2, 3, head_width=0.1, fc='crimson', ec='crimson')
    ax.arrow(0, 0, 5, 2, head_width=0.1, fc='springgreen', ec='springgreen')
    ax.text(1.5, -0.35, 'a')
    ax.text(4, -0.1, 'b')
    ax.text(2.3, 1.2, 'a + b')
    ax.text(4.5, 2.08, add_vectors, color='fuchsia')
    ax.set_facecolor('honeydew')
    plt.show()
