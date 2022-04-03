# You are given two strings current and correct representing two 24-hour times.
# 24-hour times are formatted as "HH:MM", where HH is between 00 and 23, and MM is between 00 and 59. The earliest 24-hour time is 00:00, and the latest is 23:59.
# In one operation you can increase the time current by 1, 5, 15, or 60 minutes. You can perform this operation any number of times.
# Return the minimum number of operations needed to convert current to correct.
# Q1 of Weekly Contest 287

import math

def convertTime(current, correct):
    operationCount = 0
    diff = 0

    curHour = int(current[:2])
    corHour = int(correct[:2])
    curMin = int(current[3:5])
    corMin = int(correct[3:5])

    if corMin >= curMin:
        operationCount += corHour - curHour
        diff = corMin - curMin
    else:
        if corHour - curHour - 1 > 0:
            operationCount += corHour - curHour - 1
        diff = 60 - curMin
        diff += corMin

    if diff >= 15:
        operationCount += math.floor(diff / 15)
        diff = diff % 15
    if diff >= 5:
        operationCount += math.floor(diff / 5)
        diff = diff % 5

    operationCount += diff

    return int(operationCount)

#Test Cases
current = "02:30"
correct = "04:35"
print(convertTime(current, correct))

current = "11:00"
correct = "11:01"
print(convertTime(current, correct))

current = "00:00"
correct = "23:59"
print(convertTime(current, correct))

current = "09:41"
correct = "10:34"
print(convertTime(current, correct))

current = "13:55"
correct = "15:13"
print(convertTime(current, correct))
