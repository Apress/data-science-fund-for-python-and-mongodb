import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import radviz

if __name__ == "__main__":
    data = pd.read_csv('data/iris.csv')
    plt.figure()
    radviz(data, 'Name',
           color=['b','mediumspringgreen','r'])
    plt.show()
