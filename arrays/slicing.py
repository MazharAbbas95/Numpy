import numpy as np

slicing_array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(slicing_array[1:])#after row one all rows
print(slicing_array[:])#all the rows
print(slicing_array[:2])#all rows accept row 2
print(slicing_array[2:])#all rows of 2

print(slicing_array[1:2,2])
print(slicing_array[0,0:1])
print(slicing_array[2:,2])

#boolean slicing
print(slicing_array[slicing_array>5])
mask=slicing_array>5
print(mask)
print(slicing_array[mask])

#conditional slicing
print(slicing_array[(slicing_array>1)&(slicing_array<5)])

#modify data by condition
slicing_array[slicing_array>7] = 78
print(slicing_array)

#strict condition
print(np.where(slicing_array>7,"pass","fail"))

