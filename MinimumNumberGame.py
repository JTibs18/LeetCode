# You are given a 0-indexed integer array nums of even length and there is also an empty array arr. Alice and Bob decided to play a game where in every round Alice and Bob will do one move. The rules of the game are as follows:
# Every round, first Alice will remove the minimum element from nums, and then Bob does the same.
# Now, first Bob will append the removed element in the array arr, and then Alice does the same.
# The game continues until nums becomes empty.
# Return the resulting array arr.
# For weekly contest #377 Question #1

def numberGame(nums):
    newArr = []
    nums.sort()

    for i in range(0, len(nums), 2):
        newArr.append(nums[i + 1])
        newArr.append(nums[i])

    return newArr
    
# Test cases
nums = [5,4,2,3]
print(numberGame(nums))

nums = [2,5]
print(numberGame(nums))
