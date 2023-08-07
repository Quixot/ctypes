import ctypes

clibrary = ctypes.CDLL("./clibrary.so")

addTwoNumbers = clibrary.add

addTwoNumbers.argtypes = [ctypes.c_int, ctypes.c_int]
addTwoNumbers.restype = ctypes.c_int

# Mutable strings
string = ctypes.create_string_buffer(100)
string.value = b"Hello, World!"
print(string)

string.__setitem__(3, b"T")
string[5] = b"A"
print(string.value)

print(string)

print(string.value.decode("utf8"))


class MyClass:

    def __init__(self, myString):
        self.myString = myString

    def mutator(self, value):
        self.myString[1] = value

mc = MyClass(string)
mc.mutator(b"U")

print(string, string.value)

