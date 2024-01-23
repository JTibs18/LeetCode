# You are given the root of a binary tree containing digits from 0 to 9 only.
# Each root-to-leaf path in the tree represents a number.
#   For example, the root-to-leaf path 1 -> 2 -> 3 represents the number 123.
# Return the total sum of all root-to-leaf numbers. Test cases are generated so that the answer will fit in a 32-bit integer.
# A leaf node is a node with no children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def sumNumbers(root):
    if not root:
        return 0

    def helper(curNode, curNum):
        if not curNode.left and not curNode.right:
            return int(curNum + str(curNode.val))
        
        if curNode.right and curNode.left:
            return helper(curNode.left, curNum + str(curNode.val)) + helper(curNode.right, curNum + str(curNode.val))
        
        if curNode.right:
            return helper(curNode.right, curNum + str(curNode.val))
        
        if curNode.left: 
            return helper(curNode.left, curNum + str(curNode.val))
        
    return helper(root, "")

# Test cases
root = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
root.left = n1
root.right = n2
print(sumNumbers(root))

root = TreeNode(4)
n1 = TreeNode(9)
n2 = TreeNode(0)
n3 = TreeNode(5)
n4 = TreeNode(1)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
print(sumNumbers(root))