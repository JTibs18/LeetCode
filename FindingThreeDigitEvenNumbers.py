# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
# You need to find all the unique integers that follow the given requirements:
#   The integer consists of the concatenation of three elements from digits in any arbitrary order.
#   The integer does not have leading zeros.
#   The integer is even.
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
# Return a sorted array of the unique integers.

import itertools

def findEvenNumbers(digits):
    possibleInts = set()

    for i in itertools.permutations(digits, 3):
        if i[2] % 2 == 0 and i[0] != 0:
            possibleInts.add(int("".join(str(x) for x in i)))

    return sorted(possibleInts)

# Test cases
digits = [2, 1, 3, 0]
print(findEvenNumbers(digits))

digits = [2, 2, 8, 8, 2]
print(findEvenNumbers(digits))

digits = [3, 7, 5]
print(findEvenNumbers(digits))
