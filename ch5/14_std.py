import numpy as np, csv
import matplotlib.pyplot as plt

def rnd_nrml(m, s, n):
    return np.random.normal(m, s, n)

def std_nrml(d, m, s):
    return [(x-m)/s for x in d]

if __name__ == "__main__":
    mu, sigma, n, b = 0, 1, 1000, True
    c1, c2 = 'peachpuff', 'lime'
    s = rnd_nrml(mu, sigma, n)
    plt.figure(1)
    plt.title('standard normal distribution')
    count, bins, ignored = plt.hist(s, 30, color=c1, normed=b)
    plt.plot(bins, 1/(sigma * np.sqrt(2 * np.pi)) *
             np.exp( - (bins - mu)**2 / (2 * sigma**2) ),
             linewidth=2, color=c2)
    start1, start2 = 5, 600
    mu1, sigma1, n, b = 10, 15, 500, True
    x1 = np.arange(start1, n+start1, 1)
    y1 = rnd_nrml(mu1, sigma1, n)
    mu2, sigma2, n, b = 25, 5, 500, True
    x2 = np.arange(start2, n+start2, 1)
    y2 = rnd_nrml(mu2, sigma2, n)
    plt.figure(2)
    ax = plt.subplot(211)
    ax.set_title('dataset1 (mu=10, sigma=15)')
    count, bins, ignored = plt.hist(y1, 30, color='r', normed=b)
    ax = plt.subplot(212)
    ax.set_title('dataset2 (mu=5, sigma=5)')
    count, bins, ignored = plt.hist(y2, 30, color='g', normed=b)
    plt.tight_layout()
    plt.figure(3)
    ax = plt.subplot(211)
    ax.set_title('Normal Distributions')
    g1, g2 = (x1, y1), (x2, y2)
    data = (g1, g2)
    colors = ('red', 'green')
    groups = ('dataset1', 'dataset2')
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none',
                   s=30, label=group)
    plt.legend(loc=4)
    ax = plt.subplot(212)
    ax.set_title('Standard Normal Distributions')    
    ds1 = (x1, std_nrml(y1, mu1, sigma1))
    y1_sn = ds1[1]
    ds2 = (x2, std_nrml(y2, mu2, sigma2))
    y2_sn = ds2[1]
    g1, g2 = (x1, y1_sn), (x2, y2_sn)
    data = (g1, g2)
    for data, color, group in zip(data, colors, groups):
        x, y = data
        ax.scatter(x, y, alpha=0.8, c=color, edgecolors='none',
                   s=30, label=group)
    plt.tight_layout()        
    plt.show()
