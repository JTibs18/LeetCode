# You are given an integer n and a 0-indexed 2D array queries where queries[i] = [typei, indexi, vali].
# Initially, there is a 0-indexed n x n matrix filled with 0's. For each query, you must apply one of the following changes:
#   if typei == 0, set the values in the row with indexi to vali, overwriting any previous values.
#   if typei == 1, set the values in the column with indexi to vali, overwriting any previous values.
# Return the sum of integers in the matrix after all queries are applied.

def matrixSumQueries(n, queries):
    sumVals = 0 
    colSeen = set()
    rowsSeen = set()
    queries = queries[::-1]

    for t, i, v in queries:
        if t == 0:
            if i not in rowsSeen:
                sumVals += v * (n - len(colSeen))
                rowsSeen.add(i)
        else:
            if i not in colSeen:
                sumVals += v * (n - len(rowsSeen))
                colSeen.add(i)

    return sumVals

# Test cases
n = 3
queries = [[0,0,1],[1,2,2],[0,2,3],[1,0,4]]
print(matrixSumQueries(n, queries))

n = 3
queries = [[0,0,4],[0,1,2],[1,0,1],[0,2,3],[1,2,1]]
print(matrixSumQueries(n, queries))

