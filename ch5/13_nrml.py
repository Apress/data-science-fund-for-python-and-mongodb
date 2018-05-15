import numpy as np
import matplotlib.pyplot as plt

def rnd_nrml(m, s, n):
    return np.random.normal(m, s, n)

def nrml(d):
    return [(x-np.amin(d))/(np.amax(d)-np.amin(d)) for x in d]

if __name__ == "__main__":
    mu, sigma, n, c1, c2, b = 10, 15, 100, 'orchid',\
                              'royalblue', True
    s = rnd_nrml(mu, sigma, n)
    plt.figure()
    ax = plt.subplot(211)
    ax.set_title('normal distribution')
    count, bins, ignored = plt.hist(s, 30, color=c1, normed=b)
    sn = nrml(s)
    ax = plt.subplot(212)
    ax.set_title('normal distribution "normalized"')
    count, bins, ignored = plt.hist(sn, 30, color=c2, normed=b)
    plt.tight_layout()
    plt.show()
