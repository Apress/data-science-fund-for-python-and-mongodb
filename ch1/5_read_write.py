import csv

def read_txt(f):
    with open(f, 'r') as f:
        d = f.readlines()
        return [x.strip() for x in d]

def conv_csv(t, c):
    data = read_txt(t)
    with open(c, 'w', newline='') as csv_file:
        writer = csv.writer(csv_file)
        for line in data:
            ls = line.split()
            writer.writerow(ls)

def read_csv(f):
    contents = ''
    with open(f, 'r') as f:
        reader = csv.reader(f)
        return list(reader)

def read_dict(f, h):
    input_file = csv.DictReader(open(f), fieldnames=h)
    return input_file

def od_to_d(od):
    return dict(od)

if __name__ == "__main__":
    f = 'data/names.txt'
    data = read_txt(f)
    print ('text file data sample:')
    for i, row in enumerate(data):
        if i < 3:
            print (row)
    csv_f = 'data/names.csv'
    conv_csv(f, csv_f)
    r_csv = read_csv(csv_f)
    print ('\ntext to csv sample:')
    for i, row in enumerate(r_csv):
        if i < 3:
            print (row)
    headers = ['first', 'last']
    r_dict = read_dict(csv_f, headers)
    dict_ls = []
    print ('\ncsv to ordered dict sample:')
    for i, row in enumerate(r_dict):
        r = od_to_d(row)
        dict_ls.append(r)
        if i < 3:
            print (row)
    print ('\nlist of dictionary elements sample:')
    for i, row in enumerate(dict_ls):
        if i < 3:
            print (row)
