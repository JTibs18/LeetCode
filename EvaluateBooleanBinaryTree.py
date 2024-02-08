# You are given the root of a full binary tree with the following properties:
#   Leaf nodes have either the value 0 or 1, where 0 represents False and 1 represents True.
#   Non-leaf nodes have either the value 2 or 3, where 2 represents the boolean OR and 3 represents the boolean AND.
# The evaluation of a node is as follows:
#   If the node is a leaf node, the evaluation is the value of the node, i.e. True or False.
#   Otherwise, evaluate the node's two children and apply the boolean operation of its value with the children's evaluations.
# Return the boolean result of evaluating the root node.
# A full binary tree is a binary tree where each node has either 0 or 2 children.
# A leaf node is a node that has zero children.

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def evaluateTree(root):
    if not root.left and not root.right:
        return bool(root.val) 
    
    if root.val == 2:
        return bool(evaluateTree(root.left) or evaluateTree(root.right))
    return bool(evaluateTree(root.left) and evaluateTree(root.right))
    
# Test cases
root = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(0)
n4 = TreeNode(1)
root.left = n1 
root.right = n2
n2.left = n3 
n2.right = n4
print(evaluateTree(root))

root = TreeNode(0)
print(evaluateTree(root))
