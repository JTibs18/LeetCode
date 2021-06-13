# Given the root of a binary tree, return its maximum depth.
# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxDepth(root):
    if root == None:
        return 0
    else:
        leftDepth = maxDepth(root.left) + 1
        rightDepth = maxDepth(root.right) + 1
        if rightDepth > leftDepth:
            return rightDepth
        else:
            return leftDepth

#Test cases
r = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
r.left = node1
r.right = node2
node2.right = node4
node2.left = node3
print(maxDepth(r))

r1 = TreeNode(1)
node1 = TreeNode(2)
r1.right = node1
r1.left = None
print(maxDepth(r1))

r2 = None
print(maxDepth(r2))

r3 = TreeNode(0)
print(maxDepth(r3))
