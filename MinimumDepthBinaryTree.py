# Given a binary tree, find its minimum depth.
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
# Note: A leaf is a node with no children.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def minDepth(root):
    if root == None:
        return 0
    else:
        leftDepth = minDepth(root.left) + 1
        rightDepth = minDepth(root.right) + 1
        if rightDepth != 1 and leftDepth != 1:
            return min(leftDepth, rightDepth)
        elif rightDepth == 1:
            return leftDepth
        else:
            return rightDepth

#Test cases
root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
print(minDepth(root))

root = TreeNode(2)
node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(5)
node4 = TreeNode(6)
root.right = node1
node1.right = node2
node2.right = node3
node3.right = node4
print(minDepth(root))
