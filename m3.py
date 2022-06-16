from numba import njit, prange
import time

@njit(nopython=True, fastmath=True, parallel=True)
def f(x):
    return (3 * x ** 2 + 2)


@njit(nopython=True, fastmath=True, parallel=True)
def sumg():
    N = 10000000
    x1 = 1
    x2 = 2
    dx = (x2 - x1) / N
    A = 0
    x = x1
    while x <= x2:
        dA = (3 * x ** 2 + 2) * dx
        A = A + dA
        x = x + dx
    return A


print("Area equals:", sumg())

start = time.time()
print("Run4 with parallel and nogil The area under the curve is：" + str(sumg()))
end = time.time()
print('Run4 with parallel  parallel and nogil Operating time:' + str(end - start))

