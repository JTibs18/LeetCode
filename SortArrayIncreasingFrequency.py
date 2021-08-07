# Given an array of integers nums, sort the array in increasing order based on the frequency of the values. If multiple values have the same frequency, sort them in decreasing order.
# Return the sorted array.

def frequencySort(nums):
    count = dict()
    ans = []

    for n in nums:
        if n not in count:
            count[n] = 1
        else:
            count[n] += 1

    val = sorted(count.items(), key = lambda x:(-x[1], x[0]), reverse=True)

    for i in val:
        for j in range(i[1]):
            ans.append(i[0])
    return ans

#Test cases
nums = [1,1,2,2,2,3]
print(frequencySort(nums))

nums = [2,3,1,3,2]
print(frequencySort(nums))

nums = [-1,1,-6,4,5,-6,1,4,1]
print(frequencySort(nums))
