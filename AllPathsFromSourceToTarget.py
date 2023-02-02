# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1, find all possible paths from node 0 to node n - 1 and return them in any order.
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i (i.e., there is a directed edge from node i to node graph[i][j]).

def allPathsSourceTarget(graph): 
    neighbours = dict() 
    paths = []

    for indx, val in enumerate(graph): 
        neighbours[indx] = val 

    queue = [[0]]

    while queue: 
        curPath = queue.pop(0)
        lastElement = curPath[len(curPath) - 1]

        if lastElement == len(graph) - 1: 
            paths.append(curPath)
        else: 
            for i in neighbours[lastElement]: 
                queue.append(curPath + [i])

    return paths

# Test cases 
graph = [[1,2],[3],[3],[]]
print(allPathsSourceTarget(graph))

graph = [[4,3,1],[3,2,4],[3],[4],[]]
print(allPathsSourceTarget(graph))
