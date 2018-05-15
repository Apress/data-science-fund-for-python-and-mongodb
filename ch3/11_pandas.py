import pandas as pd

if __name__ == "__main__":
    data = [
        [41, 72, 180], [27, 66, 140],
        [18, 59, 101], [57, 72, 160],
        [21, 59, 112], [29, 77, 250],
        [55, 60, 120], [28, 72, 110],
        [19, 59, 99], [32, 68, 125],
        [31, 79, 322], [36, 69, 111]
        ]
    headers = ['age', 'height', 'weight']
    df = pd.DataFrame(data, columns=headers)
    n = 3
    print ('First', n, '"df" rows:\n', df.head(n))
    print ('\nFirst "df" row:')
    print (df[0:1])
    print ('\nRows 2 through 4')
    print (df[2:5])
    print ('\nFirst', n, 'rows "age" column')
    print (df[['age']].head(n))
    print ('\nLast', n, 'rows "weight" and "age" columns')
    print (df[['weight', 'age']].tail(n))
    print ('\nRows 3 through 6 "weight" and "age" columns')
    print (df.ix[3:6, ['weight', 'age']])
