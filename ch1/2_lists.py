import numpy as np

if __name__ == "__main__":
    ls = ['orange', 'banana', 10, 'leaf', 77.009, 'tree', 'cat']
    print ('list length:', len(ls), 'items')
    print ('cat count:', ls.count('cat'), ',', 'cat index:', ls.index('cat'))
    print ('\nmanipulate list:')
    cat = ls.pop(6)
    print ('cat:', cat, ', list:', ls)
    ls.insert(0, 'cat')
    ls.append(99)
    print (ls)
    ls[7] = '11'
    print (ls)
    ls.pop(1)
    print (ls)
    ls.pop()
    print (ls)
    print ('\nslice list:')
    print ('1st 3 elements:', ls[:3])
    print ('last 3 elements:', ls[3:])
    print ('start at 2nd to index 5:', ls[1:5])
    print ('start 3 from end to end of list:', ls[-3:])
    print ('start from 2nd to next to end of list:', ls[1:-1])
    print ('\ncreate new list from another list:')
    print ('list:', ls)
    fruit = ['orange']
    more_fruit = ['apple', 'kiwi', 'pear']
    fruit.append(more_fruit)
    print ('appended:', fruit)
    fruit.pop(1)
    fruit.extend(more_fruit)
    print ('extended:', fruit)
    a, b = fruit[2], fruit[1]
    print ('slices:', a, b)
    print ('\ncreate matrix from two lists:')
    matrix = np.array([ls, fruit])
    print (matrix)
    print ('1st row:', matrix[0])
    print ('2nd row:', matrix[1])
