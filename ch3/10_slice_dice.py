import numpy as np

if __name__ == "__main__":
    points_3D_space = [
        [0, 0, 0],
        [1, 2, 3],
        [2, 2, 2],
        [9, 9, 9] ]
    A = np.matrix(points_3D_space)
    print ('slice entire A:')
    print (A[:])
    print ('\nslice 2nd column:')
    print (A[0:4, 1])
    print ('\nslice 2nd column (alt method):')
    print (A[:, 1])
    print ('\nslice 2nd & 3rd value 3rd column:')
    print (A[1:3, 2])
    print ('\nslice last row:')
    print (A[-1])
    print ('\nslice last row (alt method):')
    print (A[3])
    print ('\nslice 1st row:')
    print (A[0, :])
    print ('\nslice 2nd row; 2nd & 3rd value:')
    print (A[1, 1:3])
