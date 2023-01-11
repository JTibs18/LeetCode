# Given an undirected tree consisting of n vertices numbered from 0 to n-1, which has some apples in their vertices. You spend 1 second to walk over one edge of the tree. Return the minimum time in seconds you have to spend to collect all apples in the tree, starting at vertex 0 and coming back to this vertex.
# The edges of the undirected tree are given in the array edges, where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi. Additionally, there is a boolean array hasApple, where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

def minTime(n, edges, hasApple): 
    time = 0 
    apples = []
    tree = dict() 
    collected = set()

    for indx, val in enumerate(hasApple): 
        if val == True:
            apples.append(indx)
    
    if len(apples) == 0: 
        return 0
    if len(apples) == n: 
        return (n - 1) * 2
        
    for i in edges: 
        if i[0] in tree:
            tree[i[0]].append(i[1])
        else: 
            tree[i[0]] = [i[1]]

        if i[1] in tree: 
            tree[i[1]].append(i[0])
        else: 
            tree[i[1]] = [i[0]]

    for i in apples: 
        curApple = i 
        while curApple: 
            if curApple not in collected: 
                time += 2 
                collected.add(curApple)
            curApple = min(tree[curApple])

    return time

# Test cases
n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,True,True,False]
print(minTime(n, edges, hasApple))

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,True,False,False,True,False]
print(minTime(n, edges, hasApple))

n = 7
edges = [[0,1],[0,2],[1,4],[1,5],[2,3],[2,6]]
hasApple = [False,False,False,False,False,False,False]
print(minTime(n, edges, hasApple))

n = 4
edges = [[0,2],[0,3],[1,2]]
hasApple = [False, True, False, False]
print(minTime(n, edges, hasApple))
