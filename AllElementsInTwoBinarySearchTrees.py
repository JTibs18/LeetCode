# Given two binary search trees root1 and root2, return a list containing all the integers from both trees sorted in ascending order.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def getAllElements(root1, root2):
    allInts = []

    def helper(curNode):
        allInts.append(curNode.val)

        if curNode.left:
            helper(curNode.left)

        if curNode.right:
            helper(curNode.right)

    if root1:
        helper(root1)
    
    if root2:
        helper(root2)
    
    return sorted(allInts)

# Test cases
root1 = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(4)
root1.left = n1
root1.right = n2 
root2 = TreeNode(1)
n1 = TreeNode(0)
n2 = TreeNode(3)
root2.left = n1
root2.right = n2
print(getAllElements(root1, root2))

root1 = TreeNode(1)
n1 = TreeNode(8)
root1.right = n1
root2 = TreeNode(8)
n1 = TreeNode(1)
root2.left = n1
print(getAllElements(root1, root2))