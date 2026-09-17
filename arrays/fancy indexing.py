import numpy as np

array=np.array([1,2,3,4,5,6,7,8,9,10,11,12,13,14,15])
index=[0,2,3,4]
print(array[index])

array1=np.array(
    [[1,2,3,5],
    [4,5,6,7]]
)

rows=[0,1]
cols=[1,3]
print(array1[rows,cols])

array[[0,1]]=90
print(array)

array1[0,1]=90
print(array1)

array1[[0,1],[1,1]]=50
print(array1)
