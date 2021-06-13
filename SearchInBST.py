# You are given the root of a binary search tree (BST) and an integer val.
# Find the node in the BST that the node's value equals val and return the subtree rooted with that node. If such a node does not exist, return null.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def searchBST(root, val):
    if root == None:
        return None
    elif root.val == val:
        return root
    else:
        return searchBST(root.left, val) or searchBST(root.right, val)

#Test case
r = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
r.left = node1
r.right = node2
node1.left = node3
node1.right = node4
val = 2
print(searchBST(r, val))

r1 = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
r1.left = node1
r1.right = node2
node1.left = node3
node1.right = node4
val = 5
print(searchBST(r1, val))
