# There is a bi-directional graph with n vertices, where each vertex is labeled from 0 to n - 1 (inclusive). The edges in the graph are represented as a 2D integer array edges, where each edges[i] = [ui, vi] denotes a bi-directional edge between vertex ui and vertex vi. Every vertex pair is connected by at most one edge, and no vertex has an edge to itself.
# You want to determine if there is a valid path that exists from vertex source to vertex destination.
# Given edges and the integers n, source, and destination, return true if there is a valid path from source to destination, or false otherwise.

def validPath(n, edges, source, destination):
    graph = dict()
    visited = set()

    for n1, n2 in edges: 
        if n1 not in graph:
            graph[n1] = [n2]
        else:
            graph[n1].append(n2)
        
        if n2 not in graph:
            graph[n2] = [n1]
        else:
            graph[n2].append(n1)

    queue = [source] 

    while queue:
        curNode = queue.pop(0)
        visited.add(curNode)

        if curNode == destination:
            return True 

        for i in graph[curNode]:
            if i not in visited and i not in queue:
                queue.append(i)
    
    return False 

# Test cases
n = 3
edges = [[0,1],[1,2],[2,0]]
source = 0
destination = 2
print(validPath(n, edges, source, destination))

n = 6
edges = [[0,1],[0,2],[3,5],[5,4],[4,3]]
source = 0
destination = 5
print(validPath(n, edges, source, destination))

n = 10
edges = [[4,3],[1,4],[4,8],[1,7],[6,4],[4,2],[7,4],[4,0],[0,9],[5,4]]
source = 5
destination = 9
print(validPath(n, edges, source, destination))
