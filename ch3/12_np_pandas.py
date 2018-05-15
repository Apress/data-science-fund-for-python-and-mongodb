import pandas as pd, numpy as np

if __name__ == "__main__":
    data = [
        [41, 72, 180], [27, 66, 140],
        [18, 59, 101], [57, 72, 160],
        [21, 59, 112], [29, 77, 250],
        [55, 60, 120], [28, 72, 110],
        [19, 59, 99], [32, 68, 125],
        [31, 79, 322], [36, 69, 111]
        ]
    A = np.matrix(data)
    headers = ['age', 'height', 'weight']
    df = pd.DataFrame(A, columns=headers)
    print ('Entire "df":')
    print (df, '\n')
    print ('Sliced by "age" and "height":')
    print (df[['age', 'height']])
