import random

from numba import jit, njit, vectorize, cuda, uint32, f8, uint8


@jit(nopython=True)
def monte_carlo_pi(n):
    acc = 0
    for i in range(n):
        x = random.random()
        y = random.random()
        if (x ** 2 + y ** 2) < 1.0:
            acc += 1
    print( 4.0 * acc / n)


monte_carlo_pi(10000)
monte_carlo_pi(10000)