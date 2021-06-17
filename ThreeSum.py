# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.

def threeSum(nums):
    sortedNums = sorted(nums)
    solution = set()

    if len(sortedNums) < 3:
        return None
    elif len(sortedNums) == 3:
        if sum(sortedNums) == 0:
            triplet = (sortedNums[0], sortedNums[1], sortedNums[2])
            solution.add(triplet)
            return solution
    else:
        for index, value in enumerate (sortedNums):
            p1 = index + 1
            p2 = len(sortedNums) - 1
            while (p1 < p2):
                s = sortedNums[index] + sortedNums[p1] + sortedNums[p2]
                if s == 0:
                    triplet = (sortedNums[index], sortedNums[p1], sortedNums[p2])
                    solution.add(triplet)
                    p1 += 1
                elif s > 0:
                    p2 -= 1
                elif s < 0:
                    p1 += 1
        return solution

#Test cases
nums = [-1,0,1,2,-1,-4]
print(threeSum(nums))

nums = []
print(threeSum(nums))

nums = [0]
print(threeSum(nums))

nums = [0, 0, 0]
print(threeSum(nums))
