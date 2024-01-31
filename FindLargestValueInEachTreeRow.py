# Given the root of a binary tree, return an array of the largest value in each row of the tree (0-indexed).

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def largestValues(root):
    if not root:
        return []

    levels = dict()
    queue = [(root, 0)]
    maxNums = []    

    while queue:
        curNode, curLevel = queue.pop(0)

        if curLevel in levels:
            levels[curLevel].append(curNode.val)
        else:
            levels[curLevel] = [curNode.val]
        
        if curNode.left:
            queue.append((curNode.left, curLevel + 1))
        
        if curNode.right:
            queue.append((curNode.right, curLevel + 1))

    for value in levels.values():
        maxNums.append(max(value))

    return maxNums

# Test cases
root = TreeNode(1)
n1 = TreeNode(3)
n2 = TreeNode(2)
n3 = TreeNode(5)
n4 = TreeNode(3)
n5 = TreeNode(9)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.right = n5
print(largestValues(root))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
root.right = n2
print(largestValues(root))