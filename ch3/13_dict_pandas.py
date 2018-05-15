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
    d = {}
    dls = []
    key = ['age', 'height', 'weight']
    for row in data:
        for i, num in enumerate(row):
            d[key[i]] = num
        dls.append(d)
        d = {}
    df = pd.DataFrame(dls)
    print ('dict elements from list:')
    for row in dls:
        print (row)
    print ('\nheight from 1st dict element is:', end=' ')
    print (dls[0]['height'])
    print ('\n"df" converted from dict list:\n', df)
    print ('\nheight 1st df element:\n', df[['height']].head(1))
