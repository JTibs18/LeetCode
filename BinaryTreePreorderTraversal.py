# Given the root of a binary tree, return the preorder traversal of its nodes' values.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def preorder(root):
    def helperFun(node, order):
        if node:
            order.append(node.val)
            helperFun(node.left, order)
            helperFun(node.right, order)
    order = []
    helperFun(root, order)
    return order

#Test cases
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.right = node1
node1.left = node2
print(preorder(root))

root = None
print(preorder(root))

root = TreeNode(1)
print(preorder(root))

root = TreeNode(1)
node1 = TreeNode(2)
root.left = node1
print(preorder(root))

root = TreeNode(1)
node1 = TreeNode(2)
root.right = node1
print(preorder(root))
