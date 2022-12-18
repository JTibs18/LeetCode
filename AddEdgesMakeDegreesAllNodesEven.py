# For weekly contest #324 Question #3

# There is an undirected graph consisting of n nodes numbered from 1 to n. You are given the integer n and a 2D array edges where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi. The graph can be disconnected.
# You can add at most two additional edges (possibly none) to this graph so that there are no repeated edges and no self-loops.
# Return true if it is possible to make the degree of each node in the graph even, otherwise return false.
# The degree of a node is the number of edges connected to it.

def isPossible(n, edges):
    edgeCount = dict() 
    oddEdges = []
    indx1 = 0
    indx2 = 1 
    notPossibleEdges = 0

    for i in edges: 
        if i[0] in edgeCount: 
            edgeCount[i[0]] += 1
        else: 
            edgeCount[i[0]] = 1 
        
        if i[1] in edgeCount: 
            edgeCount[i[1]] += 1
        else: 
            edgeCount[i[1]] = 1
    
    for key in edgeCount: 
        if n - edgeCount[key] == 1 and edgeCount[key] % 2 != 0:
            return False 
        if edgeCount[key] % 2 != 0: 
            oddEdges.append(key)
   
    while indx1 < len(oddEdges) - 1: 
        if [oddEdges[indx1], oddEdges[indx2]] in edges: 
            notPossibleEdges += 1 
        if indx2 + 1 > len(oddEdges) - 1: 
            indx1 += 1 
            indx2 = indx1 + 1 
        else: 
            indx2 += 1

    if len(oddEdges) == 0 or len(oddEdges) == 2 or len(oddEdges) == 4 and notPossibleEdges % 2 == 0: 
        return True 
    else: 
        return False
        
# Test cases
n = 5
edges = [[1,2],[2,3],[3,4],[4,2],[1,4],[2,5]]
print(isPossible(n, edges))

n = 4
edges = [[1,2],[3,4]]
print(isPossible(n, edges))

n = 4
edges = [[1,2],[1,3],[1,4]]
print(isPossible(n, edges))

n = 11
edges = [[5,9],[8,1],[2,3],[7,10],[3,6],[6,7],[7,8],[5,1],[5,7],[10,11],[3,7],[6,11],[8,11],[3,4],[8,9],[9,1],[2,10],[9,11],[5,11],[2,5],[8,10],[2,7],[4,1],[3,10],[6,1],[4,9],[4,6],[4,5],[2,4],[2,11],[5,8],[6,9],[4,10],[3,11],[4,7],[3,5],[7,1],[2,9],[6,10],[10,1],[5,6],[3,9],[2,6],[7,9],[4,11],[4,8],[6,8],[3,8],[9,10],[5,10],[2,8],[7,11]]
print(isPossible(n, edges))
