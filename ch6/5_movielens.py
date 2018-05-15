import json, csv

def read_dat(h, f):
    return csv.DictReader((line.replace('::', ':')
                           for line in open(f)),
                          delimiter=':', fieldnames=h,
                          quoting=csv.QUOTE_NONE)

def gen_dict(d):
    for row in d:
        yield dict(row)

def dump_json(f, l, d):
    f = open(f, 'w')
    f.write('[')
    for i, row in enumerate(d):
        j = json.dumps(row)
        f.write(j)
        if i < l - 1:
            f.write(',')
        else:
            f.write(']')
    f.close()

def read_json(f):
    with open(f) as f:
        return json.load(f)

def display(n, f):
    for i, row in enumerate(f):
        if i < n:
            print (row)
    print()

if __name__ == "__main__":
    print ('... sizing data ...\n')
    u_dat = 'data/ml-1m/users.dat'
    m_dat = 'data/ml-1m/movies.dat'
    r_dat = 'data/ml-1m/ratings.dat'
    unames = ['user_id', 'gender', 'age', 'occupation', 'zip']
    mnames = ['movie_id', 'title', 'genres']
    rnames = ['user_id', 'movie_id', 'rating', 'timestamp']
    users = read_dat(unames, u_dat)
    ul = len(list(gen_dict(users)))
    movies = read_dat(mnames, m_dat)
    ml = len(list(gen_dict(movies)))
    ratings = read_dat(rnames, r_dat)
    rl = len(list(gen_dict(ratings)))
    print ('size of datasets:')
    print ('users', ul)
    print ('movies', ml)
    print ('ratings', rl)
    print ('\n... dumping data ...\n')
    users = read_dat(unames, u_dat)
    users = gen_dict(users)
    movies = read_dat(mnames, m_dat)
    movies = gen_dict(movies)
    ratings = read_dat(rnames, r_dat)
    ratings = gen_dict(ratings)
    uf = 'data/users.json'
    dump_json(uf, ul, users)
    mf = 'data/movies.json'
    dump_json(mf, ml, movies)
    rf = 'data/ratings.json'
    dump_json(rf, rl, ratings)
    print ('\n... verifying data ...\n')
    u = read_json(uf)
    m = read_json(mf)
    r = read_json(rf)
    n = 1
    display(n, u)
    display(n, m)
    display(n, r)
