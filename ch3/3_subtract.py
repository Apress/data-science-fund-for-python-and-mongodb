import numpy as np

def vector_add(a, b):
    return np.add(a, b)

def vector_sub(a, b):
    return np.subtract(a, b)

if __name__ == "__main__":
    v1, v2 = np.array([3, -1]), np.array([2, 3])
    add = vector_add(v1, v2)
    sub = vector_sub(v1, v2)
    print ('2D vectors:')
    print (v1, '+', v2, '=', add)
    print (v1, '-', v2, '=', sub)
    v1 = np.array([1, 3, -5])
    v2 = np.array([2, -1, 3])
    add = vector_add(v1, v2)
    sub = vector_sub(v1, v2)
    print ('\n3D vectors:')
    print (v1, '+', v2, '=', add)
    print (v1, '-', v2, '=', sub)
