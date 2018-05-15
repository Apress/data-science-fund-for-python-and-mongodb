import sys, os
sys.path.append(os.getcwd() + '/classes')
import conn

def match_item(k, v, d):
    pipeline = [ {'$match' : { k : v }} ]
    q = db.command('aggregate',d,pipeline=pipeline)
    return q

if __name__ == "__main__":
    obj = conn.conn('test')
    db = obj.getDB()
    movie = 'Toy Story'
    q = match_item('title', movie, 'movie_info')
    r = q['result'][0]
    print (movie, 'document:')
    print (r)
    print ('average rating', r['avg_rating'], '\n')
    user_id = '3'
    print ('*** user', user_id, '***')
    q = match_item('user_id', user_id, 'users')
    r = q['result'][0]    
    print ('age', r['age'], 'gender', r['gender'], 'occupation',\
          r['occupation'], 'zip', r['zip'], '\n')
    print ('*** "user 3" movie ratings of 5 ***')
    q = match_item('user_id', user_id, 'ratings')
    mid = q['result']
    for row in mid:
        if row['rating'] == '5':
            q = match_item('movie_id', row['movie_id'], 'movies')
            title = q['result'][0]['title']
            genre = q['result'][0]['genres']
            print (row['movie_id'], title, genre)
    mid = '1136'
    q = match_item('mid', mid, 'movie_info')
    title = q['result'][0]['title']
    avg_rating = q['result'][0]['avg_rating']
    print ()
    print ('"' + title + '"', 'average rating:', avg_rating)
