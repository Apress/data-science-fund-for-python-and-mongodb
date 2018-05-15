import random, numpy as np, pandas as pd
import matplotlib.pyplot as plt
import matplotlib.cm as cm
import matplotlib.colors as colors

if __name__ == "__main__":
    np.random.seed(0)
    df = pd.DataFrame({'a': np.random.randint(0, 50, 1000)})
    df['b'] = df['a'] + np.random.normal(0, 10, 1000)
    df['c'] = 100 - df['a'] + np.random.normal(0, 5, 1000)
    df['d'] = np.random.randint(0, 50, 1000)
    colormap = cm.viridis
    colorlist = [colors.rgb2hex(colormap(i))
                 for i in np.linspace(0, 1, len(df['a']))]
    df['colors'] = colorlist
    print (df.corr())
    pd.plotting.scatter_matrix(df, c=df['colors'], diagonal='d',
                               figsize=(10, 6))
    plt.show()
