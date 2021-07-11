# Given the root of a binary tree, invert the tree, and return its root.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def invertTree(root):
    if root == None:
        return root

    q = []
    q.append(root)

    while(q):
        curNode = q.pop(0)

        if curNode.left != None:
            q.append(curNode.left)
            left = curNode.left
        else:
            left = None
        if curNode.right != None:
            q.append(curNode.right)
            right = curNode.right
        else:
            right = None
            
        curNode.left = right
        curNode.right = left
    return root

#Test cases
root = TreeNode(4)
node1 = TreeNode(2)
node2 = TreeNode(7)
node3 = TreeNode(1)
node4 = TreeNode(3)
node5 = TreeNode(6)
node6 = TreeNode(9)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
node2.right = node6
r = invertTree(root)
print(r.val, r.left.val, r.right.val)

root = TreeNode(2)
node1 = TreeNode(1)
node2 = TreeNode(3)
root.left = node1
root.right = node2
r = invertTree(root)
print(r.val, r.left.val, r.right.val)

root = TreeNode(1)
node1 = TreeNode(2)
root.left = node1
r = invertTree(root)
print(r.val, r.left, r.right.val)
