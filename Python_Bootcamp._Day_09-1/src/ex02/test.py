import time
from random import choices

from cyth.c_matrix_mul import mul as c_mul
from pyth.p_matrix_mul import mul as p_mul


def make_random_martix(rows, columns):
    return [choices(range(0, 1000), k=columns) for _ in range(rows)]


if __name__ == '__main__':
    # print('Test invalid matrix:')
    # a = make_random_martix(100, 90)
    # b = make_random_martix(80, 100)
    # c_mul(a, b)

    # print('Test matrix larger then 100x100:')
    # a = make_random_martix(101, 100)
    # b = make_random_martix(100, 100)
    # c_mul(a, b)

    x = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]]
    y = [[1, 2], [1, 2], [3, 4]]
    print(c_mul(x, y))
    print(p_mul(x, y))

    print('Test matrix 1x1:')
    a = make_random_martix(1, 1)
    b = make_random_martix(1, 1)
    start = time.monotonic_ns()
    c_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Cython function: {finish - start} nanoseconds')
    start = time.monotonic_ns()
    p_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Python function: {finish - start} nanoseconds')

    print('Test matrix 10x10:')
    a = make_random_martix(10, 10)
    b = make_random_martix(10, 10)
    start = time.monotonic_ns()
    c_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Cython function: {finish - start} nanoseconds')
    start = time.monotonic_ns()
    p_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Python function: {finish - start} nanoseconds')

    print('Test matrix 100x100:')
    a = make_random_martix(100, 100)
    b = make_random_martix(100, 100)
    start = time.monotonic_ns()
    c_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Cython function: {finish - start} nanoseconds')
    start = time.monotonic_ns()
    p_mul(a, b)
    finish = time.monotonic_ns()
    print(f'Speed of Python function: {finish - start} nanoseconds')
