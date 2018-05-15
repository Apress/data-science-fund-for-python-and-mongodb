import csv, time, numpy as np

def read_dict(f, h):
    input_file = csv.DictReader(open(f), fieldnames=h)
    return (input_file)

def conv_reg_dict(d):
    return [dict(x) for x in d]

def sim_times(d, n):
    i = 0
    lsd, lsgc = [], []
    while i < n:
        start = time.clock()
        [x for x in d]
        time_d = time.clock() - start
        lsd.append(time_d)
        start = time.clock()
        (x for x in d)
        time_gc = time.clock() - start
        lsgc.append(time_gc)
        i += 1
    return (lsd, lsgc)

def gen(d):
    yield (x for x in d)

def sim_gen(d, n):
    i = 0
    lsg = []
    generator = gen(d)
    while i < n:
        start = time.clock()
        for row in generator:
            None
        time_g = time.clock() - start
        lsg.append(time_g)
        i += 1
        generator = gen(d)        
    return lsg

def avg_ls(ls):
    return np.mean(ls)

if __name__ == '__main__':
    f = 'data/names.csv'
    headers = ['first', 'last']
    r_dict = read_dict(f, headers)
    dict_ls = conv_reg_dict(r_dict)
    n = 1000
    ls_times, gc_times = sim_times(dict_ls, n)
    g_times = sim_gen(dict_ls, n)
    avg_ls = np.mean(ls_times)
    avg_gc = np.mean(gc_times)
    avg_g = np.mean(g_times)
    gc_ls = round((avg_ls / avg_gc), 2)
    g_ls = round((avg_ls / avg_g), 2)
    print ('generator comprehension:')
    print (gc_ls, 'times faster than list comprehension\n')
    print ('generator:')
    print (g_ls, 'times faster than list comprehension')
