# You are given the root of a binary tree with unique values, and an integer start. At minute 0, an infection starts from the node with value start.
# Each minute, a node becomes infected if:
#   The node is currently uninfected.
#   The node is adjacent to an infected node.
# Return the number of minutes needed for the entire tree to be infected.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def amountOfTime(root, start):
    graph = dict()

    def helper(curNode, prevNode):
        if prevNode.val in graph:
            graph[prevNode.val].append(curNode.val)
        else:
            graph[prevNode.val] = [curNode.val]

        if curNode.val in graph:
            graph[curNode.val].append(prevNode.val)
        else:
            graph[curNode.val] = [prevNode.val]
        
        if curNode.left:
            helper(curNode.left, curNode)

        if curNode.right:
            helper(curNode.right, curNode)

        return 

    if root.left:
        helper(root.left, root)
    
    if root.right:
        helper(root.right, root)

    if not graph:
        return 0

    queue = [(start, 0)]
    visited = set()

    while queue:
        curNode, iCount = queue.pop(0)
        iCount += 1 
        visited.add(curNode)
        
        for i in graph[curNode]:
            if i not in queue and i not in visited:
                queue.append((i, iCount))

    return iCount - 1

# Test cases
root = TreeNode(1)
n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(10)
n5 = TreeNode(6)
n6 = TreeNode(9)
n7 = TreeNode(2)
root.left = n1
root.right = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7
start = 3
print(amountOfTime(root, start))

root = TreeNode(1)
start = 1
print(amountOfTime(root, start))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
root.left = n1
n1.left = n2
n2.left = n3
n3.left = n4 
start = 2
print(amountOfTime(root, start))
