# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    if root.left.val == root.right.val:
        if root.left.left.val == root.right.right.val and root.left.right.val == root.right.left.val:
            print("HERE")
            return isSymmetric(root.left) and isSymmetric(root.right)
    else:
        return False

#IDK BIG QUESTION MARKS


#Test cases
r = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(4)
node5 = TreeNode(4)
node6 = TreeNode(3)
r.left = node1
r.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
print(isSymmetric(r))
