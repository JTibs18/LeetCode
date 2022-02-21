# Given an array intervals where intervals[i] = [li, ri] represent the interval [li, ri), remove all intervals that are covered by another interval in the list
# The interval [a, b) is covered by the interval [c, d) if and only if c <= a and b <= d.
# Return the number of remaining intervals.

def removeCoveredIntervals(intervals):
    ptr1 = 0
    ptr2 = 1
    subsumed = set()

    while (ptr1 < len(intervals) - 1):
        if intervals[ptr1][0] <= intervals[ptr2][0] and intervals[ptr2][1] <= intervals[ptr1][1]:
            subsumed.add(ptr2)
        elif intervals[ptr2][0] <= intervals[ptr1][0] and intervals[ptr1][1] <= intervals[ptr2][1]:
            subsumed.add(ptr1)

        if ptr2 + 1 == len(intervals):
            ptr1 += 1
            ptr2 = ptr1 + 1
        else:
            ptr2 += 1

    return len(intervals) - len(subsumed)

#Test cases
intervals = [[1, 4], [3, 6], [2, 8]]
print(removeCoveredIntervals(intervals))

intervals = [[1, 4], [2, 3]]
print(removeCoveredIntervals(intervals))

intervals = [[34335,39239],[15875,91969],[29673,66453],[53548,69161],[40618,93111]]
print(removeCoveredIntervals(intervals))
