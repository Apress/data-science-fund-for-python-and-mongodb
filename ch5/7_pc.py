import matplotlib.pyplot as plt
import pandas as pd
from pandas.plotting import parallel_coordinates

if __name__ == "__main__":
    data = pd.read_csv('data/iris.csv')
    plt.figure()
    parallel_coordinates(data, 'Name',
                         color=['b','mediumspringgreen','r'])
    plt.show()
