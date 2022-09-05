# Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.
import operator

def topKFrequent(nums, k):
    count = dict()
    out = []

    for i in nums:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1

    newDict = sorted(count.items(), key=operator.itemgetter(1), reverse=True)

    for key, value in newDict:
        out.append(key)

    return out[:k]

#Test Cases
nums = [1,1,1,2,2,3]
k = 2
print(topKFrequent(nums, k))

nums = [1]
k = 1
print(topKFrequent(nums, k))

nums = [4,1,-1,2,-1,2,3]
k = 2
print(topKFrequent(nums, k))
