import matplotlib.pyplot as plt, numpy as np

def vector_add(a, b):
    return np.add(a, b)

if __name__ == "__main__":
    v1, v2 = np.array([3, -1]), np.array([2, 3])
    add_vectors = vector_add(v1, v2)
    f, ax = plt.subplots(3)
    x, y = [0, 3], [0, -1]
    ax[0].set_xlim([-0.05, 3.1])
    ax[0].set_ylim([-1.1, 0.1])
    ax[0].scatter(x,y,s=1)
    ax[0].arrow(0, 0, 3, -1, head_width=0.1, head_length=0.07,
                fc='b', ec='b')
    ax[0].text(1.5, -0.35, 'a')
    ax[0].set_facecolor('honeydew')
    x, y = ([0, 3, 5]), ([0, -1, 2])
    ax[1].set_xlim([-0.05, 5.1])
    ax[1].set_ylim([-1.2, 2.2])
    ax[1].scatter(x,y,s=0.5)
    ax[1].arrow(0, 0, 3, -1, head_width=0.2, head_length=0.1,
                fc='b', ec='b')
    ax[1].arrow(3, -1, 2, 3, head_width=0.16, head_length=0.1,
                fc='crimson', ec='crimson')
    ax[1].text(1.5, -0.35, 'a')
    ax[1].text(4, -0.1, 'b')
    ax[1].set_facecolor('honeydew')
    x, y = ([0, 3, 5]), ([0, -1, 2])
    ax[2].set_xlim([-0.05, 5.25])
    ax[2].set_ylim([-1.2, 2.3])
    ax[2].scatter(x,y,s=0.5)
    ax[2].arrow(0, 0, 3, -1, head_width=0.15, head_length=0.1,
                fc='b', ec='b')
    ax[2].arrow(3, -1, 2, 3, head_width=0.15, head_length=0.1,
                fc='crimson', ec='crimson')
    ax[2].arrow(0, 0, 5, 2, head_width=0.1, head_length=0.1,
                fc='springgreen', ec='springgreen')
    ax[2].text(1.5, -0.35, 'a')
    ax[2].text(4, -0.1, 'b')
    ax[2].text(2.3, 1.2, 'a + b')
    ax[2].text(4.9, 1.4, add_vectors, color='fuchsia')
    ax[2].set_facecolor('honeydew')
    plt.tight_layout()
    plt.show()
