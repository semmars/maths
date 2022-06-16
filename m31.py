from numba import njit, prange
import time
import numpy as np
import sympy as sy
from scipy.optimize import fsolve

@njit(nopython=True, fastmath=True, parallel=True, nogil=True)
def f(x):
    u = (4 + np.sqrt(16 - (x - 4) ** 2) * (-1))
    return u

@njit(nopython=True, fastmath=True, parallel=True, nogil=True)
def f2(x):
    return x * 0.5


result = fsolve(lambda x: f(x) - f2(x), 0)
x = np.linspace(0, 8, 100)
cr = result[0]
print(cr)

@njit(nopython=True, fastmath=True, parallel=True, nogil=True)
def sumg():
    N = 100000000
    x1 = 0
    x2 = cr
    dx = (x2 - x1) / N
    A = 0
    x = x1
    while x <= x2:
        dA = f2(x) * dx
        A = A + dA
        x = x + dx
    return A

@njit(nopython=True, fastmath=True, parallel=True, nogil=True)
def sumg2():
    N = 100000000
    x1 = cr
    x2 = 4
    dx = (x2 - x1) / N
    A = 0
    x = x1
    while x <= x2:
        dA = f(x) * dx
        A = A + dA
        x = x + dx
    return A


A1 = sumg()
A2 = sumg2()

#print("Area equals:", sumg())
start = time.time()
A1 = sumg()
A2 = sumg2()
print(A1)
print(A2)

print("Run31 with parallel and nogil The area under the curve is：" + str(A1 + A2))
end = time.time()
print('Run4 with parallel  parallel and nogil Operating time:' + str(end - start))
