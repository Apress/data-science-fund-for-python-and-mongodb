import random, numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

if __name__ == "__main__":
    np.random.seed(0)
    x = np.random.randint(0, 50, 1000)
    y = x + np.random.normal(0, 10, 1000)
    print ('highly positive:\n', np.corrcoef(x, y))
    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0,0])
    plt.title('positive correlation')
    plt.scatter(x, y, color='springgreen')
    y = 100 - x + np.random.normal(0, 10, 1000)
    print ('\nhighly negative:\n', np.corrcoef(x, y))
    ax2 = fig.add_subplot(gs[0,1])
    plt.title('negative correlation')
    plt.scatter(x, y, color='crimson')
    y = np.random.normal(0, 10, 1000)
    print ('\nno/weak:\n', np.corrcoef(x, y))
    ax3 = fig.add_subplot(gs[1,:])
    plt.title('weak correlation')
    plt.scatter(x, y, color='peachpuff')
    plt.tight_layout()
    plt.show()
