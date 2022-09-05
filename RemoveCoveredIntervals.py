# Given a list of intervals, remove all intervals that are covered by another interval in the list.
# Interval [a,b) is covered by interval [c,d) if and only if c <= a and b <= d.
# After doing so, return the number of remaining intervals.

def removeCoveredIntervals(intervals):
    s = set()

    for i in intervals:
        s.add((i[0], i[1]))

    # for i in intervals:
    #     if i[0]

    return len(s)

#Test cases
intervals = [[1,4],[3,6],[2,8]]
print(removeCoveredIntervals(intervals))

intervals = [[1,4],[2,3]]
print(removeCoveredIntervals(intervals))

intervals = [[0,10],[5,12]]
print(removeCoveredIntervals(intervals))

intervals = [[3,10],[4,10],[5,11]]
print(removeCoveredIntervals(intervals))

intervals = [[1,2],[1,4],[3,4]]
print(removeCoveredIntervals(intervals))
