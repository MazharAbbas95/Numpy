import os
import numpy as np

filename = "large_dataset.dat"
array_shape = (125000000,)
dtype = "int64"

print(" CREATING A MEMORY-MAPPED ARRAY ON DISK")
mmap_array = np.memmap(filename, dtype=dtype, mode="w+", shape=array_shape)
print(f"File created on disk: {filename}")
print(f"Array size in virtual memory: {mmap_array.nbytes / (1024**2):.2f} MB")
print("\n WRITING DATA (LAZY WRITING)")
mmap_array[0] = 999999999  # Large peak value
mmap_array[1:100] = 5  # Small values
mmap_array.flush()
print("Data successfully flushed to disk.")
print("\n READING DATA IN READ-ONLY MODE")
read_mmap = np.memmap(filename, dtype=dtype, mode="r", shape=array_shape)
print(f"Peak value at index 0: {read_mmap[0]}")
print(f"Small value at index 50: {read_mmap[50]}")

print("\n CLEANUP")
del mmap_array
del read_mmap
if os.path.exists(filename):
    os.remove(filename)
    print("Temporary disk file cleaned up successfully.")
