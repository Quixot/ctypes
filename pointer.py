import ctypes


clibrary = ctypes.CDLL("./pointer.so")

# Allocate memory

alloc_func = clibrary.alloc_memory
alloc_func.restype = ctypes.POINTER(ctypes.c_char_p)

free_func = clibrary.free_memory
free_func.argtypes = [ctypes.POINTER(ctypes.c_char_p)]


cstring_pointer = alloc_func()
cstring = ctypes.c_char_p.from_buffer(cstring_pointer)
print(cstring_pointer, cstring, cstring.value)

free_func(cstring_pointer)

# Pointer content - print content using pointer:

num = ctypes.c_int(100)
pointer = ctypes.pointer(num)
print(pointer.contents, type(pointer))


# Create empty POINTER and assign contens (works faster)

pointer2 = ctypes.POINTER(ctypes.c_int)
pointer2.contents = num
print(pointer2.contents, type(pointer2), id(pointer2))

num2 = ctypes.c_int(200)
pointer2.contents = num2
print(pointer2.contents, type(pointer2), id(pointer2))

# Alloc and realloc memory with malloc

malloc_func = clibrary.alloc_memory_with_malloc
malloc_func.restype = None
malloc_func()
