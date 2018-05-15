import numpy as np
import matplotlib.pyplot as plt

def rnd_nrml(m, s, n):
    return np.random.normal(m, s, n)

def ctr(d):
    return [x-np.mean(d) for x in d]

if __name__ == "__main__":
    mu, sigma, n, c1, c2, b = 10, 15, 100, 'pink',\
                              'springgreen', True
    s = rnd_nrml(mu, sigma, n)
    plt.figure()
    ax = plt.subplot(211)
    ax.set_title('normal distribution')
    count, bins, ignored = plt.hist(s, 30, color=c1, normed=b)
    sc = ctr(s)
    ax = plt.subplot(212)
    ax.set_title('normal distribution "centered"')
    count, bins, ignored = plt.hist(sc, 30, color=c2, normed=b)
    plt.tight_layout()
    plt.show()
