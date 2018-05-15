from bs4 import BeautifulSoup
import requests, json

def build_title(t):
    t = t.text
    t = t.split()
    ls = []
    for row in t:
        if row != '-':
            ls.append(row)
        elif row == '-':
            break
    return ' '.join(ls)

def release_date(r):
    r = r.text
    r = r.split()
    prefix = r[0] + s + r[1]
    if len(r) == 5:
        date = r[2] + s + r[3] + s + r[4]
    else:
        date = r[2] + s + r[3]
    return prefix, date        

def write_json(f, d):
    with open(f, 'w') as fout:
        json.dump(d, fout)

def read_json(f):
    with open(f) as f:
        return json.load(f)

if __name__ == '__main__':
    s = ' '
    dic_ls = []
    base_url = "https://ssearch.oreilly.com/?q=data+science"
    soup = BeautifulSoup(requests.get(base_url).text, 'lxml')
    books = soup.find_all('article')
    for i, row in enumerate(books):
        dic = {}
        tag = row.name
        tag_val = row['class']
        title = row.find('p', {'class' : 'title'})
        title = build_title(title)
        url = row.find('a', {'class' : 'learn-more'})
        learn_more = url.get('href')
        author = row.find('p', {'class' : 'note'}).text
        release = row.find('p', {'class' : 'note date2'})
        prefix, date = release_date(release)
        if len(tag_val) == 2:
            publisher = row.find('p', {'class' : 'note publisher'}).text
            item = row.find('img', {'class' : 'book'})
            cat = item.get('class')[0]
        else:
            publisher, cat = None, None
            desc = row.find('p', {'class' : 'description'}).text.split()
            desc = [row for i, row in enumerate(desc) if i < 7]
            desc = ' '.join(desc) + ' ...'
        dic['title'] = title
        dic['learn_more'] = learn_more
        if author[0:3] != 'Pub':
            dic['author'] = author
        if publisher is not None:
            dic['publisher'] = publisher
            dic['category'] = cat
        else:
            dic['event'] = desc 
        dic['date'] = date
        dic_ls.append(dic)
    f = 'data/scraped.json'
    write_json(f, dic_ls)
    data = read_json(f)
    for i, row in enumerate(data):
        if i < 6:
            print (row['title'])
            if 'author' in row.keys():
                print (row['author'])
            if 'publisher' in row.keys():
                print (row['publisher'])
            if 'category' in row.keys():
                print ('Category:', row['category'])
                print ('Release Date:', row['date'])
            if 'event' in row.keys():
                print ('Event:', row['event'])
                print ('Publish Date:', row['date'])
            print ('Learn more:', row['learn_more'])
            print ()
