# import js2py
# js2py.translate_file('m2.js', 'm2.py')
import math
import time
from datetime import datetime

CellArea = (8 / 100000) * (4 / 50000)
Result = 0
start = time.time()
now = datetime.now()
current_time = now.strftime("%H:%M:%S")
print("Current Time =", current_time)

for x in range(1, 100000):
    for y in range(1, 50000):
        xCoordinate = x / 100000 * 8
        yCoordinate = y / 50000 * 4
        if xCoordinate <= 4 and (yCoordinate / xCoordinate) <= 0.5 and math.sqrt(
                (abs(xCoordinate - 4) ** 2) + (abs(yCoordinate - 4) ** 2)) >= 4:
            Result += CellArea

end = time.time()
print("The area under the curve is：" + str(Result))
print('Operating time:' + str(end - start))
