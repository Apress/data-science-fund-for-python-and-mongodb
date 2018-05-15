import matplotlib.pyplot as plt, pandas as pd, numpy as np
from sklearn.preprocessing import StandardScaler
from pandas.plotting import parallel_coordinates

def conv_float(d):
    return d.astype(float)

if __name__ == "__main__":
    df = pd.read_csv('data/iris.csv')
    X = df.ix[:,0:4].values
    y = df.ix[:,4].values
    X_std = StandardScaler().fit_transform(X)
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = np.cov(X_std.T)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    print ('Eigenvectors:\n', eig_vecs)
    print ('\nEigenvalues:\n', eig_vals)
    plt.figure()
    parallel_coordinates(df, 'Name', color=
                         ['orange','lime','fuchsia'])
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    cum_var_exp = np.cumsum(var_exp)
    fig, ax = plt.subplots()
    labels = ['PC1', 'PC2', 'PC3', 'PC4']
    width = 0.35
    index = np.arange(len(var_exp))
    ax.bar(index, var_exp,
           color=['fuchsia', 'lime', 'thistle', 'thistle'])
    for i, v in enumerate(var_exp):
        v = round(v, 2)
        val = str(v) + '%'
        ax.text(i, v+0.5, val, ha='center', color='b',
                fontsize=9, fontweight='bold')
    plt.xticks(index, labels)
    plt.title('Variance Explained')
    plt.show()
