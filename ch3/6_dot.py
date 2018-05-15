import numpy as np

def dot(v, w):
    return np.dot(v, w)

def display(m):
    for i, row in enumerate(m):
        print ('total sales by day:\n', end='')
        for v in np.nditer(row):
            print (v, end=' ')
        print()

if __name__ == "__main__":
    a = [3, 4, 2]
    A = np.matrix([a])
    print ('cost matrix A:\n', A)
    v1, v2, v3 = [13, 9, 7, 15], [8, 7, 4, 6], [6, 4, 0, 3]
    B = np.matrix([v1, v2, v3])
    print ('\ndaily sales by item matrix B:\n', B)    
    C = A.dot(B)
    print ('\ndot product matrix C:\n', C, '\n')
    display(C)
