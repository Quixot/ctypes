import ctypes

clibrary = ctypes.CDLL("./clibrary.so")

addTwoNumbers = clibrary.add

addTwoNumbers.argtypes = [ctypes.c_int, ctypes.c_int]
addTwoNumbers.restype = ctypes.c_int

print(addTwoNumbers(13, 57))