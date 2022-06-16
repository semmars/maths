from scipy.optimize import fsolve
import pylab
import numpy


def function_a(x):  # f(x)
    return (4 + numpy.sqrt(16 - (x - 4) ** 2) * (-1))


def function_b(x):  # g(x)
    return x * 0.5


result = fsolve(lambda x: function_a(x) - function_b(x), 0)
x = numpy.linspace(0, 8, 100)
print(result)

pylab.plot(x, [function_a(y) for y in x], x, [function_b(y) for y in x],result, function_a(result),'ro')
pylab.show()
