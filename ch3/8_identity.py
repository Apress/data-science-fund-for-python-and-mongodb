import numpy as np

def slice_row(M, i):
    return M[i,:]

def slice_col(M, j):
    return M[:, j]

def to_int(M):
    return M.astype(np.int64)

if __name__ == "__main__":    
    A = [[1, 9, 3, 6, 7],
         [4, 8, 6, 2, 1],
         [9, 8, 7, 1, 2],
         [1, 1, 9, 2, 4],
         [9, 1, 1, 3, 5]]
    A = np.matrix(A)
    print ('A:\n', A)    
    print ('\n1st row: ', slice_row(A, 0))
    print ('\n3rd column:\n', slice_col(A, 2))
    shapeA = np.shape(A)
    I = np.identity(np.shape(A)[0])
    I = to_int(I)
    print ('\nI:\n', I)
    dot_product = np.dot(A, I)
    print ('\nA * I = A:\n', dot_product)
    print ('\nA\':\n', A.I)
    A_by_Ainv = np.round(np.dot(A, A.I), decimals=0, out=None)
    A_by_Ainv = to_int(A_by_Ainv)
    print ('\nA * A\':\n', A_by_Ainv)
