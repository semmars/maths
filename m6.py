from turtle import color
import time
from datetime import datetime
from numba import njit, prange
import matplotlib.pyplot as plt
import numpy as np
import sympy as sy
import math
from math import cos, exp, pi
from scipy.integrate import quad
from scipy.optimize import fsolve
import pylab
import numpy
from scipy.optimize import fsolve
from scipy.optimize import root
from numpy import float32

x = np.linspace(0, 8, 1000)


def f(x):
    u = (4 + np.sqrt(16 - (x - 4) ** 2) * (-1))
    return u


def f2(x):
    return x * 0.5


print(f(4))

#
# plt.plot(x, f(x))
# plt.plot(x, f2(x))
# # plt.axline(color='black')
# plt.fill_between(x, f(x), f2(x), where=[(x >= 0) and (x <= 8) for x in x], color='green', alpha=0.3)


# x = sy.Symbol('x')
# pt = sy.integrate(f(x), (x, 8/5, 4))
# print(pt. evalf())
# pprint(pt)
start = time.time()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

result = fsolve(lambda x: f(x) - f2(x), 0)
x = np.linspace(0, 8, 100)
cr=result[0]
print(cr)

res, err = quad(f, cr, 4)
res2, err2 = quad(f2, 0, cr)
print("The numerical result is {:f} (+-{:g})".format(res + res2, err))
#
# pt2 = sy.integrate(f2(x), (x, 1, 2))
# print(pt2)
#
# pt3 = sy.integrate(f2(x) - f(x), (x, 1, 2))
# print(pt3)



print("Run4 with parallel and nogil The area under the curve is：" + str(res + res2))
end = time.time()
print('Run4 with parallel  parallel and nogil Operating time:' + str(end - start))


plt.show()
