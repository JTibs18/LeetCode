# Given the root of a binary tree, return the leftmost value in the last row of the tree.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def findBottomLeftValue(root):
    leftMost = 0
    level = -1 
    q = [(root, 0)]

    while q:
        curNode, lev = q.pop(0)

        if lev > level: 
            level = lev 
            leftMost = curNode.val 

        if curNode.left:
            q.append((curNode.left, lev + 1))
        
        if curNode.right:
            q.append((curNode.right, lev + 1))

    return leftMost

# Test cases
root = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
root.left = n1
root.right = n2 
print(findBottomLeftValue(root))

root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(5)
n5 = TreeNode(6)
n6 = TreeNode(7)
root.left = n1
root.right = n2
n1.left = n3
n2.left = n4
n2.right = n5
n4.left = n6
print(findBottomLeftValue(root))