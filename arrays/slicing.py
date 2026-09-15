import numpy as np

slicing_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(slicing_array[1:])#after row one all rows
print(slicing_array[:])#all the rows
print(slicing_array[:2])#all rows accept row 2
print(slicing_array[2:])#all rows of 2

print(slicing_array[1:2,2])
print(slicing_array[0,0:1])
print(slicing_array[2:,2])