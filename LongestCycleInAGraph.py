# You are given a directed graph of n nodes numbered from 0 to n - 1, where each node has at most one outgoing edge.
# The graph is represented with a given 0-indexed array edges of size n, indicating that there is a directed edge from node i to node edges[i]. If there is no outgoing edge from node i, then edges[i] == -1.
# Return the length of the longest cycle in the graph. If no cycle exists, return -1.
# A cycle is a path that starts and ends at the same node.

#First attempt: TIME LIMIT EXCEEDED 
def longestCycle1(edges): 
    visited = [-1 for i in range(len(edges))]
    curNode = 0 
    curLen = 0 
    longestCycle = -1 
    visitedNodeCount = 0 
    curCycle = set() 

    while curNode < len(edges) and edges[curNode] == -1: 
        visited[curNode] = -2
        curNode += 1 
        visitedNodeCount += 1 

    while visitedNodeCount <= len(edges): 
        if visited[curNode] == -1 and curNode != -1: 
            visited[curNode] = curLen 
            curCycle.add(curNode)
            curNode = edges[curNode]
            curLen += 1  
            visitedNodeCount += 1
        else: 
            if curNode != -1 and curNode in curCycle and curLen - visited[curNode] > longestCycle:
                longestCycle = curLen - visited[curNode] 
            
            if -1 not in visited: 
                break
            curNode = visited.index(-1)
            curLen = 0 
            curCycle = set()

    return longestCycle

# Second attempt with inspiration from https://leetcode.com/problems/longest-cycle-in-a-graph/solutions/3341638/python-java-c-simple-solution-easy-to-understand/
def longestCycle(edges): 
    longestCycleLength = -1 
    distance = 1
    visited = [0 for i in range(len(edges))]

    for curNode in range(len(edges)):
        if visited[curNode] > 0: 
            continue 

        startDistance = distance 
        u = curNode 
        
        while u != -1 and visited[u] == 0: 
            visited[u] = distance
            distance += 1 
            u = edges[u] 
        
        if u != -1 and visited[u] >= startDistance: 
            longestCycleLength = max(longestCycleLength, distance - visited[u])

    return longestCycleLength

# Test cases
edges = [3,3,4,2,3]
print(longestCycle(edges))

edges = [2,-1,3,1]
print(longestCycle(edges))

edges = [-1, 2, -1, -1]
print(longestCycle(edges))

edges = [-1,4,-1,2,0,4]
print(longestCycle(edges))

edges = [1,2,0,4,5,6,3,8,9,7]
print(longestCycle(edges))

edges = [1, 0]
print(longestCycle(edges))

edges = [-1,2,-1,5,3,3]
print(longestCycle(edges))
