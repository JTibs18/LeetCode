# You are given a 0-indexed integer array nums representing the initial positions of some marbles. You are also given two 0-indexed integer arrays moveFrom and moveTo of equal length.
# Throughout moveFrom.length steps, you will change the positions of the marbles. On the ith step, you will move all marbles at position moveFrom[i] to position moveTo[i].
# After completing all the steps, return the sorted list of occupied positions.
# Notes:
#   We call a position occupied if there is at least one marble in that position.
#   There may be multiple marbles in a single position.

def relocateMarbles(nums, moveFrom, moveTo):
    nums = set(nums)

    for i in range(len(moveFrom)):
        if moveFrom[i] in nums:
            nums.remove(moveFrom[i])
            nums.add(moveTo[i])

    return sorted(nums)        

# Test cases
nums = [1, 6, 7, 8]
moveFrom = [1, 7, 2]
moveTo = [2, 9, 5]
print(relocateMarbles(nums, moveFrom, moveTo))

nums = [1, 1, 3, 3]
moveFrom = [1, 3]
moveTo = [2, 2]
print(relocateMarbles(nums, moveFrom, moveTo))

nums = [5, 7, 8, 15]
moveFrom = [5, 7, 8, 9]
moveTo = [9, 15, 2, 7]
print(relocateMarbles(nums, moveFrom, moveTo))