import math, numpy as np

def sqrt_sum_squares(ls):
    return math.sqrt(sum(map(lambda x:x*x,ls)))

def mag(v):
    return np.linalg.norm(v)

def a_tang(v):
    return math.degrees(math.atan(v[1]/v[0]))

def dist(v, w):
    return math.sqrt(((w[0]-v[0])** 2) + ((w[1]-v[1])** 2))

def mags(v, w):
    return np.linalg.norm(v - w)

def a_tangs(v, w):
    val = (w[1] - v[1]) / (w[0] - v[0])
    return math.degrees(math.atan(val))

if __name__ == "__main__":
    v = np.array([3, 4])
    print ('single vector', str(v) + ':')
    print ('magnitude:', sqrt_sum_squares(v))
    print ('NumPY magnitude:', mag(v))
    print ('direction:', round(a_tang(v)), 'degrees\n')
    v1, v2 = np.array([2, 3]), np.array([5, 8])
    print ('two vectors', str(v1) + ' and ' + str(v2) + ':')
    print ('magnitude', round(dist(v1, v2),2))    
    print ('NumPY magnitude:', round(mags(v1, v2),2))
    print ('direction:', round(a_tangs(v1, v2)), 'degrees\n')
    v1, v2 = np.array([0, 0]), np.array([3, 4])
    print ('use origin (0,0) as 1st vector:')
    print ('"two vectors', str(v1) + ' and ' + str(v2) + '"')
    print ('magnitude:', round(mags(v1, v2),2))
    print ('direction:', round(a_tangs(v1, v2)), 'degrees')
