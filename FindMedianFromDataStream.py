# The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle value, and the median is the mean of the two middle values.
#   For example, for arr = [2,3,4], the median is 3.
#   For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
# Implement the MedianFinder class:
#   MedianFinder() initializes the MedianFinder object.
#   void addNum(int num) adds the integer num from the data stream to the data structure.
#   double findMedian() returns the median of all elements so far. Answers within 10-5 of the actual answer will be accepted.
# sorted containers from https://grantjenks.com/docs/sortedcontainers/introduction.html 

from sortedcontainers import SortedList 

# slow runtime but uses minimal memory
class MedianFinder1:
    def __init__(self):
        self.stream = []

    def addNum(self, num):
        self.stream.append(num)

    def findMedian(self):
        self.stream.sort()
        midPoint = len(self.stream) // 2
        if len(self.stream) % 2 == 0:
            return (self.stream[midPoint] + self.stream[(midPoint) - 1]) / 2 
        return (self.stream[midPoint])  

# faster runtime but uses more memory 
class MedianFinder:
    def __init__(self): 
        self.stream = SortedList()

    def addNum(self, num):
        self.stream.add(num)

    def findMedian(self):
        midPoint = len(self.stream) // 2
        if len(self.stream) % 2:
            return (self.stream[midPoint]) 
        return (self.stream[midPoint] + self.stream[(midPoint) - 1]) / 2 

# Test cases
medianFinder = MedianFinder()
medianFinder.addNum(1)
medianFinder.addNum(2)
print(medianFinder.findMedian())
medianFinder.addNum(3)
print(medianFinder.findMedian())

medianFinder = MedianFinder()
medianFinder.addNum(-1)
print(medianFinder.findMedian())
medianFinder.addNum(-2)
print(medianFinder.findMedian())
medianFinder.addNum(-3)
print(medianFinder.findMedian())
medianFinder.addNum(-4)
print(medianFinder.findMedian())
medianFinder.addNum(-5)
print(medianFinder.findMedian())
