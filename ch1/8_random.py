import csv, random, time

def read_dict(f, h):
    input_file = csv.DictReader(open(f), fieldnames=h)
    return (input_file)

def conv_reg_dict(d):
    return [dict(x) for x in d]

def r_inds(ls, n):
    length = len(ls) - 1
    yield [random.randrange(length) for _ in range(n)]

def get_slice(ls, n):
    return ls[:n]

def p_line():
    print ()

if __name__ == '__main__':
    f = 'data/names.csv'
    headers = ['first', 'last']
    r_dict = read_dict(f, headers)
    dict_ls = conv_reg_dict(r_dict)
    n = len(dict_ls)
    r = random.randrange(0, n-1)
    print ('randomly selected index:', r)
    print ('randomly selected element:', dict_ls[r])    
    elements = 3
    generator = next(r_inds(dict_ls, elements))
    p_line()
    print (elements, 'randomly generated indicies:', generator)
    print (elements, 'elements based on indicies:')
    for row in generator:
        print (dict_ls[row])
    x = [[i] for i in range(n-1)]
    random.shuffle(x)
    p_line()
    print ('1st', elements, 'shuffled elements:')
    ind = get_slice(x, elements)
    for row in ind:
        print (dict_ls[row[0]])
    seed = 1
    random_seed = random.seed(seed)
    rs1 = random.randrange(0, n-1)
    p_line()
    print ('deterministic seed', str(seed) + ':', rs1)
    print ('corresponding element:', dict_ls[rs1])
    t = time.time()
    random_seed = random.seed(t)
    rs2 = random.randrange(0, n-1)
    p_line()
    print ('non-deterministic time seed', str(t) + ' index:', rs2)
    print ('corresponding element:', dict_ls[rs2], '\n')
    print (elements, 'random elements seeded with time:')
    for i in range(elements):
        r = random.randint(0, n-1)
        print (dict_ls[r], r)
    random_seed = random.seed()
    rs3 = random.randrange(0, n-1)
    p_line()
    print ('non-deterministic auto seed:', rs3)
    print ('corresponding element:', dict_ls[rs3], '\n')
    print (elements, 'random elements auto seed:')
    for i in range(elements):
        r = random.randint(0, n-1)
        print (dict_ls[r], r)
    names = []
    for row in dict_ls:
        name = row['last'] + ', ' + row['first']
        names.append(name)
    p_line()
    print (elements, 'names with "random.choice()":')
    for row in range(elements):
        print (random.choice(names))
    p_line()
    print (elements, 'names with "random.sample()":')
    print (random.sample(names, elements))
