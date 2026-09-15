import numpy as np
array=np.array([np.zeros(10),
                np.ones(10),
                np.arange(10),

                ])
print(array)
array1=np.array(np.linspace(0,12,num=5))#linspace is  count driver

print(array1)
array2=np.array(np.full(5,10))
print(array2)

array3=np.array(np.empty(5))
print(array3)