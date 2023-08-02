# Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

def permutations(nums):
    def backtrack(track):
        if (len(nums) == len(track)): 
            result.append(track[:])
            return 
        
        for i in nums: 
            if i not in track: 
                track.append(i)
            else: 
                continue
            backtrack(track)
            track.pop()

    result = []
    track = []

    backtrack(track)
    return result 

# Test cases
nums = [1, 2, 3]
print(permutations(nums))

nums = [0, 1]
print(permutations(nums))

nums = [1]
print(permutations(nums))
