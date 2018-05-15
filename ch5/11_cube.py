import json

def dump_json(f, d):
    with open(f, 'w') as f:
        json.dump(d, f)

def read_json(f):
    with open(f) as f:
        return json.load(f)

def rnd(n):
    return '{:.2f}'.format(n)

if __name__ == "__main__":
    d = dict()
    googl = dict()
    googl['2017-09-25'] =\
    {'Open':939.450012, 'High':939.750000, 'Low':924.510010,
     'Close':934.280029, 'Adj Close':934.280029, 'Volume':1873400}
    googl['2017-09-26'] =\
    {'Open':936.690002, 'High':944.080017, 'Low':935.119995,
     'Close':937.429993, 'Adj Close':937.429993, 'Volume':1672700}
    googl['2017-09-27'] =\
    {'Open':942.739990, 'High':965.429993, 'Low':941.950012,
     'Close':959.900024, 'Adj Close':959.900024, 'Volume':2334600}
    googl['2017-09-28'] =\
    {'Open':956.250000, 'High':966.179993, 'Low':955.549988,
     'Close':964.809998, 'Adj Close':964.809998, 'Volume':1400900}
    googl['2017-09-29'] =\
    {'Open':966.000000, 'High':975.809998, 'Low':966.000000,
     'Close':973.719971, 'Adj Close':973.719971, 'Volume':2031100}
    amzn = dict()
    amzn['2017-09-25'] =\
    {'Open':949.309998, 'High':949.419983, 'Low':932.890015,
     'Close':939.789978, 'Adj Close':939.789978, 'Volume':5124000}
    amzn['2017-09-26'] =\
    {'Open':945.489990, 'High':948.630005, 'Low':931.750000,
     'Close':937.429993, 'Adj Close':938.599976, 'Volume':3564800}
    amzn['2017-09-27'] =\
    {'Open':948.000000, 'High':955.299988, 'Low':943.299988,
     'Close':950.869995, 'Adj Close':950.869995, 'Volume':3148900}
    amzn['2017-09-28'] =\
    {'Open':951.859985, 'High':959.700012, 'Low':950.099976,
     'Close':956.400024, 'Adj Close':956.400024, 'Volume':2522600}
    amzn['2017-09-29'] =\
    {'Open':960.109985, 'High':964.830017, 'Low':958.380005,
     'Close':961.349976, 'Adj Close':961.349976, 'Volume':2543800}
    mkl = dict()
    mkl['2017-09-25'] =\
    {'Open':1056.199951, 'High':1060.089966, 'Low':1047.930054,
     'Close':1050.250000, 'Adj Close':1050.250000, 'Volume':23300}
    mkl['2017-09-26'] =\
    {'Open':1052.729980, 'High':1058.520020, 'Low':1045.000000,
     'Close':1045.130005, 'Adj Close':1045.130005, 'Volume':25800}
    mkl['2017-09-27'] =\
    {'Open':1047.560059, 'High':1069.099976, 'Low':1047.010010,
     'Close':1064.040039, 'Adj Close':1064.040039, 'Volume':21100}
    mkl['2017-09-28'] =\
    {'Open':1064.130005, 'High':1073.000000, 'Low':1058.079956,
     'Close':1070.550049, 'Adj Close':1070.550049, 'Volume':23500}
    mkl['2017-09-29'] =\
    {'Open':1068.439941, 'High':1073.000000, 'Low':1060.069946,
     'Close':1067.979980, 'Adj Close':1067.979980 , 'Volume':20700}
    d['GOOGL'], d['AMZN'], d['MKL'] = googl, amzn, mkl
    json_file = 'data/cube.json'
    dump_json(json_file, d)
    d = read_json(json_file)
    s = ' '
    print ('\'Adj Close\' slice:')
    print (10*s, 'AMZN', s, 'GOOGL', s, 'MKL')
    print ('Date')
    print ('2017-09-25', rnd(d['AMZN']['2017-09-25']['Adj Close']),
           rnd(d['GOOGL']['2017-09-25']['Adj Close']),
           rnd(d['MKL']['2017-09-25']['Adj Close']))
    print ('2017-09-26', rnd(d['AMZN']['2017-09-26']['Adj Close']),
           rnd(d['GOOGL']['2017-09-26']['Adj Close']),
           rnd(d['MKL']['2017-09-26']['Adj Close']))
    print ('2017-09-27', rnd(d['AMZN']['2017-09-27']['Adj Close']),
           rnd(d['GOOGL']['2017-09-27']['Adj Close']),
           rnd(d['MKL']['2017-09-27']['Adj Close']))
    print ('2017-09-28', rnd(d['AMZN']['2017-09-28']['Adj Close']),
           rnd(d['GOOGL']['2017-09-28']['Adj Close']),
           rnd(d['MKL']['2017-09-28']['Adj Close']))
    print ('2017-09-29', rnd(d['AMZN']['2017-09-29']['Adj Close']),
           rnd(d['GOOGL']['2017-09-29']['Adj Close']),
           rnd(d['MKL']['2017-09-29']['Adj Close']))
