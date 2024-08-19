import numpy as np
import pandas as pd

# 1. Create an empty and full numpy array.
arr1=np.array([])
print("Empty array:",arr1)

arr2=np.array([1,5,2,0,5,1,1,0,2,3,8])
print("Full numpy arary:",arr2) 

# 2.Most frequent value in NumPy array.
print("Most frequent value:",np.bincount(arr2).argmax())

# 3.Number of non zero elements.
print("Non zero:",np.count_nonzero(arr2))

# 4.Reverse NumPy array.
revarr=arr2[::-1]
print('Reverse array:',np.flip(arr2))
print('Reverse array:',revarr)

# 5.Replace all negatives with zero.
neg=np.array([1,1,2,5,-8,8,-9,7,-47,23,2,9])
neg[neg<0]=0
print('Before:',neg)
print('After:',neg)

# 6.Floor,Ceil and Truncate.
dec=np.array([1.22,2.6,6.8,9.781,5.2,2])
print('Array before operations:',dec)
print('Array after operation:')
print("Floor:",np.floor(dec))
print('Ceil:',np.ceil(dec))
print('Truncate:',np.trunc(dec))