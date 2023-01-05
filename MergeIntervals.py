# Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

def merge(intervals): 
    intervals = sorted(intervals)
    newIntervals = []
    newIntervals.append(intervals[0])

    for i in intervals[1:]: 
        if newIntervals[-1][0] <= i[0] and i[0] <= newIntervals[-1][-1]: 
            newIntervals[-1][-1] = max(newIntervals[-1][-1], i[-1])
        else: 
            newIntervals.append(i)
    
    return newIntervals

# Test cases 
intervals = [[1,3],[2,6],[8,10],[15,18]]
print(merge(intervals))

intervals = [[1,4],[4,5]]
print(merge(intervals))
