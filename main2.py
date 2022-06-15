# import js2py
# js2py.translate_file('m2.js', 'm2.py')
import math
import time
import numpy as np
from datetime import datetime
CellArea = np.float64((8 / 100000) * (4 / 50000))
Result = np.float64(0)
start = time.time()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)
xCoordinate = np.float64(0)
yCoordinate = np.float64(0)

xrange = np.arange(start=1, stop=100000, step=1)
yrange = np.arange(start=1, stop=50000, step=1)
print("here we go")
for x in xrange:
    for y in yrange:
        xCoordinate = x / 100000 * 8
        yCoordinate = y / 50000 * 4
        if xCoordinate <= 4 and np.divide(yCoordinate, xCoordinate) <= 0.5 and np.sqrt(
                (np.square(np.abs(xCoordinate - 4))) + (np.square(np.abs(yCoordinate - 4)))) >= 4:
            Result += CellArea

end = time.time()
print("The area under the curve is：" + str(Result))
print('Operating time:' + str(end - start))
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)