# You are given a 0-indexed array mountain. Your task is to find all the peaks in the mountain array.
# Return an array that consists of indices of peaks in the given array in any order.
# Notes:
#   A peak is defined as an element that is strictly greater than its neighboring elements.
#   The first and last elements of the array are not a peak.

def findPeaks(mountain):
    peaks = []

    for indx in range(1, len(mountain) - 1):
        if mountain[indx - 1] < mountain[indx] and mountain[indx + 1] < mountain[indx]:
            peaks.append(indx)

    return peaks

# Test cases
mountain = [2,4,4]
print(findPeaks(mountain))

mountain = [1,4,3,8,5]
print(findPeaks(mountain))
