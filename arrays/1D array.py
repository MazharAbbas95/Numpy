import numpy as np

array=np.array(
    [1,2,3,4,5,6,7,8,9],dtype='int16'
)
print(array)
actual_size=array.itemsize
print(actual_size)#8 bytes
total_bytes=array.nbytes
print(total_bytes) #optimize memory from 72 bytes to 18 bytes

# numpy array of string
array1=np.array(
    ["ali","ahemd","subhan","fahad"]
)
print(array1)

# check dimentions day 2
print(array1.dtype)#type of array
print(array1.shape)#shape of array how many rows and columns
print(array1.ndim)#number of dimentions
print(array1.size) #size of array
print(array1.itemsize) #size of byte of one element on the base of datatype
(array.astype("<u8"))
# numpy array of float

array2=np.array(
    [12.1,12.3,23.5]

)
print(array2)

# numpy array of boolean
array3=np.array(
    [True,True,True,True,False, False]

)

print(array3)
changearray=array3.astype("int8" )#change array from boolien to integer
print(changearray)
