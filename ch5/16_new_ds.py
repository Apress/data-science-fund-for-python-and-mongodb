import json

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
    jsonf = 'data/superstore.json'
    json_data = read_json(jsonf)
    l = len(list(mk_data(json_data)))
    generator = mk_data(json_data)
    jsonf= 'data/wrangled.json'
    with open(jsonf, 'w') as f:
        f.write('[')
    for i, row in enumerate(generator):
        j = json.dumps(row)
        if i < l - 1:
            with open(jsonf, 'a') as f:
                f.write(j)
                f.write(',')
        else:
            with open(jsonf, 'a') as f:
                f.write(j)
                f.write(']')            
    json_data = read_json(jsonf)
    for i, row in enumerate(json_data):
        if i < 5:
            print (row['cust'], row['item'], row['sale'])
        else:
            break
