import numpy as np

def sum_cols(matrix):
    return np.sum(matrix, axis=0)

def sum_rows(matrix):
    return np.sum(matrix, axis=1)

def dot(v, w):
    return np.dot(v, w)

if __name__ == "__main__":
    v1, v2, v3 = [1, 7, -4], [2, -3, 10], [3, 5, 6]
    A = np.matrix([v1, v2, v3])
    print ('matrix A:\n', A)
    v_cols = sum_cols(A)
    print ('\nsum A by column:\n', v_cols)
    v_rows = sum_rows(A)
    print ('\nsum A by row:\n', v_rows)
    dot_product = dot(v1, v2)
    print ('\nvector 1:', v1)
    print ('vector 2:', v2)
    print ('\ndot product v1 and v2:')
    print (dot_product)
    v1, v2, v3 = [-2, 5, 4], [1, 2, 9], [10, -9, 3]
    B = np.matrix([v1, v2, v3])
    print ('\nmatrix B:\n', B)
    C = A.dot(B)
    print ('\nmatrix C (dot product A and B):\n', C)
    print ('\nC by row:')
    for i, row in enumerate(C):
        print ('row', str(i) + ': ', end='') 
        for v in np.nditer(row):
            print (v, end=' ')
        print()
