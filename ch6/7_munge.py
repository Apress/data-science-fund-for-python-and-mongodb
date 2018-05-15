import json, numpy as np, sys, os, humanfriendly as hf
from time import clock
sys.path.append(os.getcwd()+'/classes')
import conn

def read_json(f):
    with open(f) as f:
        return json.load(f)

def get_column(A, v):
    return [A_i[v] for A_i in A]

def remove_nr(v1, v2):
    set_v1 = set(v1)
    set_v2 = set(v2)
    diff = list(set_v1 - set_v2)
    return diff

def get_info(*args):
    a = [arg for arg in args]
    ratings = [int(row[a[0][1]]) for row in a[2] if row[a[0][0]] == a[1]]
    uids = [row[a[0][3]] for row in a[2] if row[a[0][0]] == a[1]]
    title = [row[a[0][2]] for row in a[3] if row[a[0][0]] == a[1]]
    age = [int(row[a[0][4]]) for col in uids for row in a[4] if col == row[a[0][3]]]
    gender = [row[a[0][5]] for col in uids for row in users if col == row[a[0][3]]]
    return (ratings, title[0], uids, age, gender)

def generate(k, v, r, m, u):
   for i, mid in enumerate(v):
       dic = {}
       rec = get_info(k, mid, r, m, u)
       dic = {'_id':i, 'mid':mid, 'title':rec[1], 'avg_rating':np.mean(rec[0]),
              'n_ratings':len(rec[0]), 'avg_age':np.mean(rec[3]),
              'M':rec[4].count('M'), 'F':rec[4].count('F')}
       dic['avg_rating'] = round(float(str(dic['avg_rating'])[:6]),2)
       dic['avg_age'] = round(float(str(dic['avg_age'])[:6]))
       yield dic

def gen_ls(g):
    for i, row in enumerate(g):
        yield row

if __name__ == "__main__":
    print ('... creating datasets ...\n')
    m = 'data/cmovies.json'
    movies = np.array(read_json(m))
    r = 'data/ratings.json'
    ratings = np.array(read_json(r))
    r = 'data/users.json'
    users = np.array(read_json(r))
    print ('... creating movie indicies vector data ...\n')
    mv = get_column(movies, 'movie_id')
    rv = get_column(ratings, 'movie_id')
    print ('... creating unrated movie indicies vector ...\n')
    nrv = remove_nr(mv, rv)
    diff = [int(row) for row in nrv]
    print (np.sort(diff), '\n')
    new_mv = [x for x in mv if x not in nrv]
    mid = '1'
    keys = ('movie_id', 'rating', 'title', 'user_id', 'age', 'gender')
    stats = get_info(keys, mid, ratings, movies, users)
    avg_rating = np.mean(stats[0])
    avg_age = np.mean(stats[3])
    n_ratings = len(stats[0])
    title = stats[1]
    M, F = stats[4].count('M'), stats[4].count('F')
    print ('avg rating for:', end=' "')
    print (title + '" is', round(avg_rating, 2), end=' (')
    print (n_ratings, 'ratings)\n')
    gen = generate(keys, new_mv, ratings, movies, users)
    gls = gen_ls(gen)
    obj = conn.conn('test')
    db = obj.getDB()
    movie_info = db.movie_info
    movie_info.drop()
    print ('... saving movie_info to MongoDB ...\n')
    start = clock()
    for row in gls:
        movie_info.insert(row)
    end = clock()
    elapsed_ls = end - start
    print (hf.format_timespan(elapsed_ls, detailed=True))
