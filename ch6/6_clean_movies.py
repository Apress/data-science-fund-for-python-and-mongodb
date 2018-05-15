import json, numpy as np

def read_json(f):
    with open(f) as f:
        return json.load(f)

def dump_json(f, d):
    with open(f, 'w') as fout:
        json.dump(d, fout)    

def display(n, d):
    [print (row) for i,row in enumerate(d) if i < n]

def get_indx(k, d):
    return [row[k] for row in d if 'null' in row]

def get_data(k, l, d):
    return [row for i, row in enumerate(d) if row[k] in l]

def get_unique(key, d):
    s = set()
    for row in d:
        for k, v in row.items():
            if k in key:
                s.add(v)
    return np.sort(list(s))

if __name__ == "__main__":
    mf = 'data/movies.json'
    m = read_json(mf)
    n = 20
    display(n, m)
    print ()
    indx = get_indx('movie_id', m)
    for row in m:
        if row['movie_id'] in indx:
            row['title'] = row['title'] + ':' + row['genres']
            row['genres'] = row['null'][0]
            del row['null']
        title = row['title'].split(" ")
        year = title.pop()
        year = ''.join(c for c in year if c not in '()')
        row['title'] = ' '.join(title)
        row['year'] = year
    data = get_data('movie_id', indx, m)
    n = 2
    display(n, data)
    s = get_unique('year', m)
    print ('\n', s, '\n')
    rec = get_data('year', ['Assignment'], m)
    print (rec[0])
    rec = get_data('year', ["L'Associe1982"], m)
    print (rec[0], '\n')
    b1, b2, cnt = False, False, 0
    for row in m:
        if row['movie_id'] in ['1001']:
            row['year'] = '1982'
            print (row)
            b1 = True
        elif row['movie_id'] in ['2382']:
            row['title'] = 'Police Academy 5: Assignment: Miami Beach'
            row['genres'] = 'Comedy'
            row['year'] = '1988'
            print (row)
            b2 = True
        elif b1 and b2: break
        cnt += 1
    print ('\n', cnt, len(m))
    mf = 'data/cmovies.json'    
    dump_json(mf, m)
    m = read_json(mf)
    display(n, m)
