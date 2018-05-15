from TwitterSearch import *
import json, sys

class twitSearch:
    def __init__(self, cred, ls, limit):
        self.cred = cred
        self.ls = ls
        self.limit = limit
    def search(self):
        num = 0
        dt = []
        dic = {}
        try:
            tso = TwitterSearchOrder()
            tso.set_keywords(self.ls)
            tso.set_language('en')
            tso.set_include_entities(False)
            ts = TwitterSearch(
                consumer_key = self.cred[0]['ck'],
                consumer_secret = self.cred[0]['cs'],
                access_token = self.cred[0]['at'],
                access_token_secret = self.cred[0]['ae']
                )
            for tweet in ts.search_tweets_iterable(tso):
                if num <= self.limit:
                    dic['_id'] = num
                    dic['tweeter'] = tweet['user']['screen_name']
                    dic['tweet_text'] = tweet['text']
                    dt.append(dic)
                    dic = {}
                else:
                    break
                num += 1
        except TwitterSearchException as e:
            print (e)
        return dt

def get_creds():
    with open('data/credentials.json') as json_data:
        d = json.load(json_data)
        json_data.close()
    return d

def write_json(f, d):
    with open(f, 'w') as fout:
        json.dump(d, fout)

def translate():
    return dict.fromkeys(range(0x10000, sys.maxunicode + 1), 0xfffd)

def read_json(f):
    with open(f) as f:
        return json.load(f)

if __name__ == '__main__':
    cred = get_creds()
    ls = ['machine', 'learning']
    limit = 10
    obj = twitSearch(cred, ls, limit)
    data = obj.search()
    f = 'data/TwitterSearch.json'
    write_json(f, data)
    non_bmp_map = translate()
    print ('twitter data:')
    for row in data:
        row['tweet_text'] = str(row['tweet_text']).translate(non_bmp_map)
        tweet_text = row['tweet_text'][0:50]
        print ('{:<3}{:18s}{}'.format(row['_id'], row['tweeter'], tweet_text))
    print ('\nverify JSON:')
    read_data = read_json(f)
    for i, p in enumerate(read_data):
        if i < 3:
            p['tweet_text'] = str(p['tweet_text']).translate(non_bmp_map)
            tweet_text = p['tweet_text'][0:50]
            print ('{:<3}{:18s}{}'.format(p['_id'], p['tweeter'], tweet_text))
