# Given the root of a binary tree, check whether it is a mirror of itself (i.e., symmetric around its center).

# Reference: https://www.youtube.com/watch?v=-5E5Jt_HKLc
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSymmetric(root):
    def isMirror(t1, t2): 
        if t1 == None and t2 == None:
            return True 

        if t1 == None or t2 == None: 
            return False 

        return t1.val == t2.val and isMirror(t1.left, t2.right) and isMirror(t1.right, t2.left)

    return isMirror(root, root) 

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

root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(3)
node4 = TreeNode(3)
root.left = node1 
root.right = node2
node1.right = node3
node2.right = node4 
print(isSymmetric(root))