# You are given an integer limit and a 2D array queries of size n x 2.
# There are limit + 1 balls with distinct labels in the range [0, limit]. Initially, all balls are uncolored. For every query in queries that is of the form [x, y], you mark ball x with the color y. After each query, you need to find the number of distinct colors among the balls.
# Return an array result of length n, where result[i] denotes the number of distinct colors after ith query.
# Note that when answering a query, lack of a color will not be considered as a color.
# For Biweekly Contest #131 Question 3

def queryResults(limit, queries): 
    balls = {}
    colors = {}
    distinctColors = []

    for ball, color in queries: 
        if ball in balls: 
            colors[balls[ball]] -= 1 
            if colors[balls[ball]] == 0: 
                del colors[balls[ball]]
        balls[ball] = color 
        
        if color in colors: 
            colors[color] += 1 
        else: 
            colors[color] = 1 
    
        distinctColors.append(len(colors))
 
    return distinctColors

# Test Cases
limit = 4
queries = [[1, 4], [2, 5], [1, 3], [3, 4]]
print(queryResults(limit, queries))

limit = 4
queries = [[0, 1], [1, 2], [2, 2], [3, 4], [4, 5]]
print(queryResults(limit, queries))
