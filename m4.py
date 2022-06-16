from turtle import color

import matplotlib.pyplot as plt
import numpy as np
import sympy as sy

x = np.linspace(-1, 3, 1000)
y = np.linspace(-1, 3, 1000)


def f(x):
    return x ** 2


def f2(x):
    return (3 * x ** 2 + 2)


plt.plot(x, f(x))
plt.plot(x, f2(x))
# plt.axline(color='black')
plt.fill_between(x, f(x), f2(x), where=[(x > 0) and (x < 2) for x in x] \
                 , color='green', alpha=0.3)

x = sy.Symbol('x')
y = sy.Symbol('y')
pt = sy.integrate(f(x), (x, 0, 10))
print(pt)

pt2 = sy.integrate(f2(x), (x, 1, 2))
print(pt2)


pt3 = sy.integrate(f2(x)-f(x), (x, 1, 2))
print(pt3)

plt.show()
