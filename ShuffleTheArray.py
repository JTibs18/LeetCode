# Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
# Return the array in the form [x1,y1,x2,y2,...,xn,yn].

def shuffle(nums, n):
    shuff = []

    for i in range(n):
        shuff.append(nums[i])
        shuff.append(nums[i + n])
    return shuff

#Test Cases
nums = [2,5,1,3,4,7]
n = 3
print(shuffle(nums, n))

nums = [1,2,3,4,4,3,2,1]
n = 4
print(shuffle(nums, n))

nums = [1,1,2,2]
n = 2
print(shuffle(nums, n))
