# A sequence of numbers is called an arithmetic progression if the difference between any two consecutive elements is the same.
# Given an array of numbers arr, return true if the array can be rearranged to form an arithmetic progression. Otherwise, return false.

#Faster algorithm but uses more memory
def canMakeArithmeticProgression(arr):
    arr = sorted(arr)
    arrOfDiffs = []
    length = len(arr)

    for indx, num in enumerate(arr):
        if indx + 1 < length:
            diff = arr[indx + 1] - num
            arrOfDiffs.append(diff)

    length =len(arrOfDiffs)

    for indx, d in enumerate(arrOfDiffs):
        if indx + 1 < length and arrOfDiffs[indx + 1] != d:
            return False
    return True

#Slower algorithm but uses less memory
def canMakeArithmeticProgression2(arr):
    arr = sorted(arr)
    arrOfDiffs = []

    for indx, num in enumerate(arr):
        if indx + 1 < len(arr):
            diff = arr[indx + 1] - num
            arrOfDiffs.append(diff)

    for indx, d in enumerate(arrOfDiffs):
        if indx + 1 < len(arrOfDiffs) and arrOfDiffs[indx + 1] != d:
            return False
    return True

#Test cases
arr = [3, 5, 1]
print(canMakeArithmeticProgression(arr))
print(canMakeArithmeticProgression2(arr))

arr = [1, 2, 4]
print(canMakeArithmeticProgression(arr))
print(canMakeArithmeticProgression2(arr))
