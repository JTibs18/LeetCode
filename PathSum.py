# Given the root of a binary tree and an integer targetSum, return true if the tree has a root-to-leaf path such that adding up all the values along the path equals targetSum.
# A leaf is a node with no children.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def hasPathSum(root, targetSum):
    if not root:
        return False

    def helperFun(root, curSum):
        if not root.left and not root.right and curSum + root.val == targetSum:
            return True 
        
        return (root.right and helperFun(root.right, curSum + root.val)) or (root.left and helperFun(root.left, curSum + root.val))

    return helperFun(root, 0) or False

# Test cases
root = TreeNode(5)
node1 = TreeNode(4)
node2 = TreeNode (8)
node3 = TreeNode(11)
node4 = TreeNode(13)
node5 = TreeNode(4)
node6 = TreeNode(7)
node7 = TreeNode(2)
node8 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node3.left = node6
node3.right = node7
node5.right = node8
targetSum = 22
print(hasPathSum(root, targetSum))

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
targetSum = 5
print(hasPathSum(root, targetSum))

root = None
targetSum = 0 
print(hasPathSum(root, targetSum))