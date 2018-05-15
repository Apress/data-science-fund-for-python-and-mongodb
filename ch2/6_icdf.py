from scipy.stats import norm
import numpy as np

def np_rstrip(v):
    return np.char.rstrip(v.astype(str), '.0')

def transform(t):
    one, two = round(t[0]), round(t[1])
    return (np_rstrip(one), np_rstrip(two))

if __name__ == "__main__":
    mu, sigma = 1000, 30
    print ('Expected failure rates:')
    fail = np_rstrip(round(norm.ppf(0.05, loc=mu, scale=sigma)))
    print ('5% fail within', fail, 'hours')
    fail_range = norm.interval(0.95, loc=mu, scale=sigma)
    lo, hi = transform(fail_range)
    print ('95% fail between', lo, 'and', hi, end=' ')
    print ('hours of usage')
    print ('\nExpected survival rates:')    
    last = np_rstrip(round(norm.ppf(0.95, loc=mu, scale=sigma)))
    print ('5% survive up to', last, 'hours of usage')
    last_range = norm.interval(0.05, loc=mu, scale=sigma)
    lo, hi = transform(last_range)
    print ('95% survive between', lo, 'and', hi, 'hours of usage')
