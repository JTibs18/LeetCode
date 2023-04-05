# You are a product manager and currently leading a team to develop a new product. Unfortunately, the latest version of your product fails the quality check. Since each version is developed based on the previous version, all the versions after a bad version are also bad.
# Suppose you have n versions [1, 2, ..., n] and you want to find out the first bad one, which causes all the following ones to be bad.
# You are given an API bool isBadVersion(version) which returns whether version is bad. Implement a function to find the first bad version. You should minimize the number of calls to the API.

# sample implementation of this function for testing purposes
def isBadVersion(version): 
    if version == 4: 
        return True 
    return False 

def firstBadVersion(n): 
    l = 1 

    while l < n: 
        mid = (l +(n - 1)) // 2 

        if isBadVersion(mid) == False: 
            l = mid + 1 
        else: 
            n = mid 

    return l 
        
# Test case
n = 5
print(firstBadVersion(n))
