# Given the root of a Binary Search Tree (BST), convert it to a Greater Tree such that every key of the original BST is changed to the original key plus the sum of all keys greater than the original key in BST.
# As a reminder, a binary search tree is a tree that satisfies these constraints:
#   The left subtree of a node contains only nodes with keys less than the node's key.
#   The right subtree of a node contains only nodes with keys greater than the node's key.
#   Both the left and right subtrees must also be binary search trees.
# Note: this question is the same as Binary Search Tree to Greater Sum Tree

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def convertBST(root):

    def helper(curNode, parVal):
        if curNode.right:
            curNode.val += helper(curNode.right, parVal)
        else:
            curNode.val += parVal

        if curNode.left:
            return helper(curNode.left, curNode.val)
        
        return curNode.val

    if root:
        helper(root, 0)

    return root 

# Test cases
root = TreeNode(4)
n1 = TreeNode(1)
n2 = TreeNode(6)
n3 = TreeNode(0)
n4 = TreeNode(2)
n5 = TreeNode(5)
n6 = TreeNode(7)
n7 = TreeNode(3)
n8 = TreeNode(8)
root.left = n1
root.right = n2
n1.left = n3
n1.right = n4
n2.left = n5
n2.right = n6
n4.right = n7
n6.right = n8
print(convertBST(root))

root = TreeNode(0)
n1 = TreeNode(1)
root.right = n1
print(convertBST(root))

root = TreeNode(3)
n1 = TreeNode(2)
n2 = TreeNode(4)
n3 = TreeNode(1)
root.left = n1
root.right = n2
n1.left = n3
print(convertBST(root))