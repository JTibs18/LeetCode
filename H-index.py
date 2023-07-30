# Given an array of integers citations where citations[i] is the number of citations a researcher received for their ith paper, return the researcher's h-index.
# According to the definition of h-index on Wikipedia: The h-index is defined as the maximum value of h such that the given researcher has published at least h papers that have each been cited at least h times.

def hIndex(citations): 
    c = sorted(citations, reverse=True)

    for index, val in enumerate(c): 
        if val <= index + 1: 
            return max(val, index)
    return len(c)

# Test cases
citations = [3, 0, 6, 1, 5]
print(hIndex(citations))

citations = [1, 3, 1]
print(hIndex(citations))

citations = [100]
print(hIndex(citations))

citations = [4, 4, 0, 0]
print(hIndex(citations))
