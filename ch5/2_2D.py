import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import numpy as np, random
from scipy.special import ndtri

def inverse_normal_cdf(r):
    return ndtri(r)

def random_normal():
    return inverse_normal_cdf(random.random())

def scatter(loc):
    plt.scatter(xs, ys1, marker='.', color='black', label='ys1')
    plt.scatter(xs, ys2, marker='.', color='gray',  label='ys2')
    plt.xlabel('xs')
    plt.ylabel('ys')
    plt.legend(loc=loc)
    plt.tight_layout()

if __name__ == "__main__":
    xs = [random_normal() for _ in range(1000)]
    ys1 = [ x + random_normal() / 2 for x in xs]
    ys2 = [-x + random_normal() / 2 for x in xs]
    gs = gridspec.GridSpec(2, 2)
    fig = plt.figure()
    ax1 = fig.add_subplot(gs[0,0])
    plt.title('ys1 data')
    n, bins, ignored = plt.hist(ys1, 50, normed=1,
                                facecolor='chartreuse', alpha=0.75)
    ax2 = fig.add_subplot(gs[0,1])
    plt.title('ys2 data')
    n, bins, ignored = plt.hist(ys2, 50, normed=1,
                                facecolor='fuchsia', alpha=0.75)
    ax3 = fig.add_subplot(gs[1,:])
    plt.title('Correlation')
    scatter(6)
    print (np.corrcoef(xs, ys1)[0, 1])
    print (np.corrcoef(xs, ys2)[0, 1])
    plt.show()
