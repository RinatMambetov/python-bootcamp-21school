cimport cython

# Disabling bounds checking can improve the performance of the code, but it also makes it more susceptible to buffer
# overflows and underflows.
@cython.boundscheck(False)
# It is a decorator in Cython that disables negative indexing for array indexing in the function it decorates.
@cython.wraparound(False)
def mul(list a, list b):
    if len(a[0]) != len(b):
        raise ValueError("The width of the first matrix should be equal to the height of the second one")

    if len(a) > 100 or len(a[0]) > 100:
        raise ValueError("Input matrices cannot be larger than 100x100")

    if len(b) > 100 or len(b[0]) > 100:
        raise ValueError("Input matrices cannot be larger than 100x100")

    for i in range(len(a)):
        for j in range(len(a[0])):
            if not isinstance(a[i][j], int):
                raise TypeError("Input matrix must contain integers only")

    for i in range(len(b)):
        for j in range(len(b[0])):
            if not isinstance(b[i][j], int):
                raise TypeError("Input matrix must contain integers only")

    cdef int m = len(a)
    cdef int n = len(b[0])
    cdef int p = len(b)
    cdef list result = [[0] * n for _ in range(m)]

    for i in range(m):
        for j in range(n):
            s = 0
            for k in range(p):
                s += a[i][k] * b[k][j]
            result[i][j] = s

    return result
