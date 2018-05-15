import matplotlib.pyplot as plt, pandas as pd
import numpy as np, json, random as rnd
from sklearn.preprocessing import StandardScaler
from pandas.plotting import parallel_coordinates

def read_json(f):
    with open(f) as f:
        return json.load(f)

def unique_features(k, d):
    return list(set([dic[k] for dic in d]))

def sire_features(k, d):
    return [{k: row[k] for k in (k)} for row in d]

def sire_numeric(k, d):
    s = conv_float(sire_features(k, d))
    return s

def sire_sample(k, v, d, m):
    indices = np.arange(0, len(d), 1)
    s = [d[i] for i in indices if d[i][k] == v]
    n = len(s)
    num_keys = ['sale', 'quan', 'disc', 'prof']
    for i, row in enumerate(s):
        for k in num_keys:
            row[k] = float(row[k])
    s = rnd_sample(m, len(s), s)
    return (s, n)

def rnd_sample(m, n, d):
    indices = sorted(rnd.sample(range(n), m))
    return [d[i] for i in indices]

def conv_float(d):
    return [dict([k, float(v)] for k, v in row.items()) for row in d]

if __name__ == "__main__":
    f = 'data/wrangled.json'
    data = read_json(f)
    segm = unique_features('segm', data)
    print ('classes in "segm" feature:')
    print (segm)
    keys = ['sale', 'quan', 'disc', 'prof', 'segm']
    features = sire_features(keys, data)
    num_keys = ['sale', 'quan', 'disc', 'prof']
    numeric_data = sire_numeric(num_keys, features)
    k, v = "segm", "Home Office"
    m = 100
    s_home = sire_sample(k, v, features, m)
    v = "Consumer"
    s_cons = sire_sample(k, v, features, m)
    v = "Corporate"
    s_corp = sire_sample(k, v, features, m)
    print ('\nHome Office slice:', s_home[1])
    print('Consumer slice:', s_cons[1])
    print ('Coporate slice:', s_corp[1])
    print ('sample size:', m)
    df_home = pd.DataFrame(s_home[0])
    df_cons = pd.DataFrame(s_cons[0])
    df_corp = pd.DataFrame(s_corp[0])
    frames = [df_home, df_cons, df_corp]
    result = pd.concat(frames)
    plt.figure()
    parallel_coordinates(result, 'segm', color=
                         ['orange','lime','fuchsia'])
    df = pd.DataFrame(numeric_data)
    X = df.ix[:].values
    X_std = StandardScaler().fit_transform(X)
    mean_vec = np.mean(X_std, axis=0)
    cov_mat = np.cov(X_std.T)
    print ('\ncovariance matrix:\n', cov_mat)
    eig_vals, eig_vecs = np.linalg.eig(cov_mat)
    print ('\nEigenvectors:\n', eig_vecs)
    print ('\nEigenvalues:\n', np.sort(eig_vals)[::-1])
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    print ('\nvariance explained:\n', var_exp)
    corr_mat = np.corrcoef(X.T)
    print ('\ncorrelation matrix:\n', corr_mat)    
    eig_vals, eig_vecs = np.linalg.eig(corr_mat)
    print ('\nEigenvectors:\n', eig_vecs)
    print ('\nEigenvalues:\n', np.sort(eig_vals)[::-1])
    tot = sum(eig_vals)
    var_exp = [(i / tot)*100 for i in sorted(eig_vals, reverse=True)]
    print ('\nvariance explained:\n', var_exp)
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
