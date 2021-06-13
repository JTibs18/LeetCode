# You are given two binary trees root1 and root2.
# Imagine that when you put one of them to cover the other, some nodes of the two trees are overlapped while the others are not.
# You need to merge the two trees into a new binary tree. The merge rule is that if two nodes overlap, then sum node values up as the new value of the merged node.
# Otherwise, the NOT null node will be used as the node of the new tree.
# Return the merged tree.
# Note: The merging process must start from the root nodes of both trees.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def mergeTrees(root1, root2):
    if root1 == None and root2 == None:
        return root1
    elif root1 != None and root2 == None:
        return root1
    elif root1 == None and root2 != None:
        return root2
    else:
        root1.left = mergeTrees(root1.left, root2.left)
        root1.right = mergeTrees(root1.right, root2.right)
        root1.val = root1.val + root2.val
        return root1

#Test cases
r1 = TreeNode(1)
node1 = TreeNode(3)
node2 = TreeNode(2)
node3 = TreeNode(5)
r1.left = node1
r1.right = node2
node1.left = node3
r2 = TreeNode(2)
n1 = TreeNode(1)
n2 = TreeNode(3)
n3 = TreeNode(4)
n4 = TreeNode(7)
r2.left = n1
r2.right = n2
n1.right = n3
n2.right = n4
x = mergeTrees(r1, r2)
print(x.val, x.left.val, x.right.val)
