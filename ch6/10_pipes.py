import sys, os
sys.path.append(os.getcwd() + '/classes')
import conn

def stages(k, v, r, d):
    pipeline = [ {'$match' : { '$and' : [ { k : v },
                   {'rating':{'$eq':r} }] } },
                 {'$project' : {
                     '_id' : 1,
                     'user_id' : 1,
                     'movie_id' : 1,
                     'rating' : 1 } },
                 {'$limit' : 100}]
    q = db.command('aggregate',d,pipeline=pipeline)
    return q

def match_item(k, v, d):
    pipeline = [ {'$match' : { k : v }} ]
    q = db.command('aggregate',d,pipeline=pipeline)
    return q

if __name__ == "__main__":
    obj = conn.conn('test')
    db = obj.getDB()
    u = '3'
    r = '5'
    q = stages('user_id', u, r, 'ratings')
    result = q['result']
    print ('ratings of', r, 'for user ' + str(u) + ':')
    for i, row in enumerate(result):
        print (row)
    n = i+1
    print ()
    print (n, 'associated movie titles:')
    for i, row in enumerate(result):
        q = match_item('movie_id', row['movie_id'], 'movies')
        r = q['result'][0]
        print (r['title'])
