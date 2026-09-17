import numpy as np
from pyexpat import model

array=np.array([1,2,2,3,4,5,6,7,8,9,10,11,12,13,14,15])

#finding central tendency of this array
print(np.mean(array))
print(np.median(array))


print(np.max(array))
print(np.min(array))
print(np.mean(array,axis=0))