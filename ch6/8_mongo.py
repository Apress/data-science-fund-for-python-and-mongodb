import sys, os, json, humanfriendly as hf
from time import clock
sys.path.append(os.getcwd() + '/classes')
import conn

def read_json(f):
    with open(f) as f:
        return json.load(f)

def create_db(c, d):
    c = db[c]
    c.drop()
    for i, row in enumerate(d):
        row['_id'] = i
        c.insert(row)

if __name__ == "__main__":
    u = read_json('data/users.json')
    m = read_json('data/cmovies.json')
    r = read_json('data/ratings.json')
    obj = conn.conn('test')
    db = obj.getDB()
    print ('... creating MongoDB collections ...\n')
    start = clock()
    create_db('users', u)
    create_db('movies', m)
    create_db('ratings', r)
    end = clock()
    elapsed_ls = end - start
    print (hf.format_timespan(elapsed_ls, detailed=True))
