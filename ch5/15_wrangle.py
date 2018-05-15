import csv, json

def read_dict(f):
    return csv.DictReader(open(f))

def to_dict(d):
    return [dict(row) for row in d]

def dump_json(f, d):
    with open(f, 'w') as fout:
        json.dump(d, fout)

def read_json(f):
    with open(f) as f:
        return json.load(f)

def mk_data(d):
    for i, row in enumerate(d):
        e = {}
        e['_id'] = i
        e['cust'] = row['Customer Name']
        e['item'] = row['Sub-Category']
        e['sale'] = rnd(row['Sales'])
        e['quan'] = row['Quantity']
        e['disc'] = row['Discount']
        e['prof'] = rnd(row['Profit'])        
        e['segm'] = row['Segment']
        yield e

def rnd(v):
    return str(round(float(v),2))

if __name__ == "__main__":
    f= 'data/superstore.csv'
    d = read_dict(f)
    data = to_dict(d)
    jsonf = 'data/superstore.json'
    dump_json(jsonf, data)
    print ('"superstore" data added to JSON\n')
    json_data = read_json(jsonf)
    print ("{:20s} {:15s} {:10s} {:3s} {:5s} {:12s} {:10s}".
           format('CUSTOMER', 'ITEM', 'SALES', 'Q', 'DISC',
                  'PROFIT', 'SEGMENT'))
    generator = mk_data(json_data)
    for i, row in enumerate(generator):
        if i < 10:
            print ("{:20s} {:15s}".format(row['cust'], row['item']),
                   "{:10s} {:3s}".format(row['sale'], row['quan']),
                   "{:5s} {:12s}".format(row['disc'], row['prof']),
                   "{:10s}".format(row['segm']))
        else:
            break
