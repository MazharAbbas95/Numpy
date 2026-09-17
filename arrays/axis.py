import numpy as np

array=np.array([[1,2,3],[4,5,6],[7,8,9]])
print(array.sum(axis=0))#colums collaps with each like 1+4+7
print(array.sum(axis=1))#rows collaps with each other like 1+2+3

print(array.shape)
print(array.ndim)
array1=np.array([[1,2,3],[4,5,6]])
print(array1.sum(axis=0))
print(array1.sum(axis=1))