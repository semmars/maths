# import js2py
# js2py.translate_file('m2.js', 'm2.py')
import math
import time
from datetime import datetime
from numba import njit, prange

global CellArea
global Result


@njit(nopython=True, fastmath=True)
def run():
    CellArea = (8 / 100000) * (4 / 50000)
    Result = 0
    for x in range(1, 100000):
        for y in range(1, 50000):
            xCoordinate = x / 100000 * 8
            yCoordinate = y / 50000 * 4
            if xCoordinate <= 4 and (yCoordinate / xCoordinate) <= 0.5 and math.sqrt(
                    (abs(xCoordinate - 4) ** 2) + (abs(yCoordinate - 4) ** 2)) >= 4:
                Result += CellArea

    return Result


def run2():
    CellArea = (8 / 100000) * (4 / 50000)
    Result = 0
    for x in range(1, 100000):
        for y in range(1, 50000):
            xCoordinate = x / 100000 * 8
            yCoordinate = y / 50000 * 4
            if xCoordinate <= 4 and (yCoordinate / xCoordinate) <= 0.5 and math.sqrt(
                    (abs(xCoordinate - 4) ** 2) + (abs(yCoordinate - 4) ** 2)) >= 4:
                Result += CellArea

    return Result


@njit(nopython=True, fastmath=True, parallel=True)
def run3():
    CellArea = (8 / 100000) * (4 / 50000)
    Result = 0
    for x in prange(1, 100000):
        for y in prange(1, 50000):
            xCoordinate = x / 100000 * 8
            yCoordinate = y / 50000 * 4
            if xCoordinate <= 4 and (yCoordinate / xCoordinate) <= 0.5 and math.sqrt(
                    (abs(xCoordinate - 4) ** 2) + (abs(yCoordinate - 4) ** 2)) >= 4:
                Result += CellArea

    return Result

@njit(nopython=True, fastmath=True, parallel=True, nogil=True)
def run4():
    CellArea = (8 / 100000) * (4 / 50000)
    Result = 0
    for x in prange(1, 100000):
        for y in prange(1, 50000):
            xCoordinate = x / 100000 * 8
            yCoordinate = y / 50000 * 4
            if xCoordinate <= 4 and (yCoordinate / xCoordinate) <= 0.5 and math.sqrt(
                    (abs(xCoordinate - 4) ** 2) + (abs(yCoordinate - 4) ** 2)) >= 4:
                Result += CellArea

    return Result


def measurerun():
    start = time.time()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    Result = run()
    print("The area under the curve is：" + str(Result))
    end = time.time()
    print('Operating time:' + str(end - start))


def measurerun2():
    start = time.time()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    Result = run2()
    print("Run2 The area under the curve is：" + str(Result))
    end = time.time()
    print('Run2 Operating time:' + str(end - start))

def measurerun3():
    start = time.time()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    Result = run3()
    print("Run3 with parallel The area under the curve is：" + str(Result))
    end = time.time()
    print('Run3 with parallel Operating time:' + str(end - start))

def measurerun4():
    start = time.time()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    print("Current Time =", current_time)
    Result = run4()
    print("Run4 with parallel and nogil The area under the curve is：" + str(Result))
    end = time.time()
    print('Run4 with parallel  parallel and nogil Operating time:' + str(end - start))

measurerun()
# measurerun2()
measurerun3()
measurerun4()

print("warm up done! /n")

measurerun()
# measurerun2()
measurerun3()
measurerun4()

