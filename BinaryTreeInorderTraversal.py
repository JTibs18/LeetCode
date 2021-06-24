# Given the root of a binary tree, return the inorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def inorderTraversal(root):
    def helperFun(node, order):
        if node:
            helperFun(node.left, order)
            order.append(node.val)
            helperFun(node.right, order)

    inorder = []
    helperFun(root, inorder)
    return inorder

#Test cases
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2
print(inorderTraversal(root))

root = None
print(inorderTraversal(root))

root = TreeNode(1)
print(inorderTraversal(root))

root = TreeNode(1)
node1 = TreeNode(2)
root.left = node1
print(inorderTraversal(root))

root = TreeNode(1)
node1 = TreeNode(2)
root.right = node1
print(inorderTraversal(root))
