<<<<<<< HEAD
# Given the roots of two binary trees p and q, write a function to check if they are the same or not
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value
=======
# Given the roots of two binary trees p and q, write a function to check if they are the same or not.
# Two binary trees are considered the same if they are structurally identical, and the nodes have the same value.
>>>>>>> a0ce9b00455f5fa040d88919524bada338a7a2d0

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isSameTree(p, q):
    if p == None and q == None:
        return True
    elif (p != None and q == None) or (p == None and q != None):
        return False
    elif (p.val == q.val):
        return isSameTree(p.left, q.left) and isSameTree(p.right, q.right)
    else:
        return False

#Test cases
r1 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
r1.left = node1
r1.right = node2
r2 = TreeNode(1)
n1 = TreeNode(2)
n2 = TreeNode(3)
r2.left = n1
r2.right =  n2
print(isSameTree(r1, r2))

r3 = TreeNode(1)
node1 = TreeNode(2)
r3.left = node1
r4 = TreeNode(1)
n1 = TreeNode(2)
r4.right =  n1
print(isSameTree(r3, r4))

r5 = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(1)
r5.left = node1
r5.right = node2
r6 = TreeNode(1)
n1 = TreeNode(1)
n2 = TreeNode(2)
r6.right =  n2
r6.left =  n1
print(isSameTree(r5, r6))
