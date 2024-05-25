# You are given an integer array nums, an integer array queries, and an integer x.
# For each queries[i], you need to find the index of the queries[i]th occurrence of x in the nums array. If there are fewer than queries[i] occurrences of x, the answer should be -1 for that query.
# Return an integer array answer containing the answers to all queries.
# For Biweekly Contest #131 Question 2

def occurrencesOfElement(nums, queries, x): 
    indexes = []
    occurrences = []

    for indx, val in enumerate(nums): 
        if val == x:
            indexes.append(indx)

    for i in queries: 
        if i - 1 < len(indexes): 
            occurrences.append(indexes[i - 1])
        else:
            occurrences.append(-1)

    return occurrences

# Test cases
nums = [1, 3, 1, 7]
queries = [1, 3, 2, 4]
x = 1 
print(occurrencesOfElement(nums, queries, x))

nums = [1, 2, 3]
queries = [10]
x = 5 
print(occurrencesOfElement(nums, queries, x))
