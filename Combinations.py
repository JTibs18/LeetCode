# Given two integers n and k, return all possible combinations of k numbers chosen from the range [1, n].
# You may return the answer in any order. 
# With help from: https://labuladong.gitbook.io/algo-en/iii.-algorithmic-thinking/subset_permutation_combination

def combine(n, k): 
    def backtrack(n, k, start, track): 
        if (k == len(track)): 
            result.append(track[:])
            return 

        for i in range(start, n + 1): 
            track.append(i)
            backtrack(n, k, i+1, track)
            track.pop()

    result = []
    track = [] 
    
    backtrack(n, k, 1, track)
    return result


# Test cases
n = 4
k = 2
print(combine(n, k))

n = 1
k = 1 
print(combine(n, k))
