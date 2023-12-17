# You are given two 0-indexed integer permutations A and B of length n.
# A prefix common array of A and B is an array C such that C[i] is equal to the count of numbers that are present at or before the index i in both A and B.
# Return the prefix common array of A and B.
# A sequence of n integers is called a permutation if it contains all integers from 1 to n exactly once.

# naive solution 
def findThePrefixCommonArray1(A, B):
    numCount = dict()
    commonArr = []

    for indx, val in enumerate(A):
        if val in numCount:
            numCount[val] += 1
        else:
            numCount[val] = 1 

        if B[indx] in numCount:
            numCount[B[indx]] += 1
        else:
            numCount[B[indx]] = 1 

        count = 0
        for val in numCount.values():
            if val == 2: 
                count  += 1
        
        commonArr.append(count)

    return commonArr

# faster & more space efficient algorithm, works on the assumption that neither A nor B has duplicate numbers 
def findThePrefixCommonArray(A, B):
    numCount = set()
    commonArr = []
    count = 0

    for indx in range(len(A)):
        if A[indx] in numCount:
            count += 1 
        else:
            numCount.add(A[indx])

        if B[indx] in numCount:
            count += 1
        else:
            numCount.add(B[indx])
        
        commonArr.append(count)

    return commonArr

# Test cases
A = [1,3,2,4]
B = [3,1,2,4]
print(findThePrefixCommonArray(A, B))

A = [2,3,1]
B = [3,1,2]
print(findThePrefixCommonArray(A, B))
