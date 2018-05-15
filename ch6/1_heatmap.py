import json, pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def read_json(f):
    with open(f) as f:
        return json.load(f)

def verify_keys(d, **kwargs):
    data = d[0].items()
    k1 = set([tup[0] for tup in data])
    s = kwargs.items()
    k2 = set([tup[1] for tup in s])
    return list(k1.intersection(k2))

def build_ls(k, d):
    return [{k: row[k] for k in (keys)} for row in d]

def get_rows(d, n):
    [print(row) for i, row in enumerate(d) if i < n]

def conv_float(d):
    return [dict([k, float(v)] for k, v in row.items()) for row in d]

if __name__ == "__main__":
    f= 'data/wrangled.json'
    data = read_json(f)
    keys = verify_keys(data, c1='sale', c2='quan', c3='disc', c4='prof')
    heat = build_ls(keys, data)
    print ('1st row in "heat":')
    get_rows(heat, 1)
    heat = conv_float(heat)
    print ('\n1st row in "heat" converted to float:')
    get_rows(heat, 1)
    df = pd.DataFrame(heat)
    plt.figure()
    sns.heatmap(df.corr(), annot=True, cmap='OrRd')
    plt.show()
