import json, humanfriendly as hf
from time import clock

def read_json(f):
    with open(f) as f:
        return json.load(f)

def mk_gen(k, d):
    for row in d:
        dic = {}
        for key in k:
            dic[key] = float(row[key])
        yield dic

def conv_float(keys, d):
    return [dict([k, float(v)] for k, v in row.items()
                 if k in keys) for row in d]

if __name__ == "__main__":
    f = 'data/wrangled.json'
    data = read_json(f)
    keys = ['sale', 'quan', 'disc', 'prof']
    print ('create, convert, and display list:')
    start = clock()
    data = conv_float(keys, data)
    for i, row in enumerate(data):
        if i < 5:
            print (row)
    end = clock()
    elapsed_ls = end - start
    print (hf.format_timespan(elapsed_ls, detailed=True))
    print ('\ncreate, convert, and display generator:')
    start = clock()
    generator = mk_gen(keys, data)
    for i, row in enumerate(generator):
        if i < 5:
            print (row)
    end = clock()
    elapsed_gen = end - start
    print (hf.format_timespan(elapsed_gen, detailed=True))
    speed = round(elapsed_ls / elapsed_gen, 2)
    print ('\ngenerator is', speed, 'times faster')
