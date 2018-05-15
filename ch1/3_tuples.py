import numpy as np

if __name__ == "__main__":
    tup = ('orange', 'banana', 'grape', 'apple', 'grape')
    print ('tuple length:', len(tup))
    print ('grape count:', tup.count('grape'))
    print ('\nslice tuple:')
    print ('1st 3 elements:', tup[:3])
    print ('last 3 elements', tup[3:])
    print ('start at 2nd to index 5', tup[1:5])
    print ('start 3 from end to end of tuple:', tup[-3:])
    print ('start from 2nd to next to end of tuple:', tup[1:-1])
    print ('\ncreate list and create matrix from it and tuple:')    
    fruit = ['pear', 'grapefruit', 'cantaloupe', 'kiwi', 'plum']
    matrix = np.array([tup, fruit])
    print (matrix)
