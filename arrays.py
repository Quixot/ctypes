import ctypes
import os

path = os.getcwd()
clibrary = ctypes.CDLL(os.path.join(path, "arrays.so"))

values = (ctypes.c_int * 10)()

for i in range(10):
    values[i] = i

print(values)

sum = clibrary.sumArray(values, len(values))

print(sum)

# return pointer

clibrary.incArray.restype = ctypes.POINTER(ctypes.c_int)
result = clibrary.incArray(values, len(values))
print(result.contents)
