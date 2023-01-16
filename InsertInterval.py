# You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.
# Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).
# Return intervals after the insertion.

def insert(intervals, newInterval): 
    newIntervalList = []
    inserted = False 

    for indx, val in enumerate(intervals):
        if ((newInterval[0] >= val[0] and newInterval[0] <= val[1]) or (newInterval[1] >=val[0] and newInterval[1] <= val[1]) or (val[0] >= newInterval[0] and val[0] <= newInterval[1]) or (val[1] >= newInterval[0] and val[1] <= newInterval[1])) and inserted == False: 
            newIntervalList.append([min(val[0], newInterval[0]), max(val[1], newInterval[1])])
            inserted = True 
        elif inserted == False and newInterval[1] < val[0]: 
            newIntervalList.append(newInterval)
            newIntervalList.append(val)
            inserted = True
        elif indx != 0 and newIntervalList[-1][0] <= val[0] and val[0] <= newIntervalList[-1][-1]: 
            newIntervalList[-1][-1] = max(newIntervalList[-1][-1], val[-1])
        else: 
            newIntervalList.append(val)
    
    if inserted == False: 
        if len(newIntervalList) != 0 and newInterval[1] < newIntervalList[0][1]: 
            newIntervalList.insert(0, newInterval)
        else: 
            newIntervalList.append(newInterval)

    return newIntervalList

# Test cases 
intervals = [[1,3],[6,9]]
newInterval = [2,5]
print(insert(intervals, newInterval))

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))

intervals = []
newInterval = [5, 7]
print(insert(intervals, newInterval))

intervals = [[1, 5]]
newInterval = [0,3]
print(insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [0,0]
print(insert(intervals, newInterval))

intervals = [[1,5]]
newInterval = [0,6]
print(insert(intervals, newInterval))

intervals = [[3,5], [12,15]]
newInterval = [6,6]
print(insert(intervals, newInterval))
