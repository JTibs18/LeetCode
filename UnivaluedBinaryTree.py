# A binary tree is univalued if every node in the tree has the same value.
# Return true if and only if the given tree is univalued.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def isUniTree(root):
    if root == None:
        return True

    q = []
    q.append(root)

    while q:
        curNode = q.pop(0)

        if curNode.left != None:
            q.append(curNode.left)
            if curNode.val != curNode.left.val:
                return False
        if curNode.right != None:
            q.append(curNode.right)
            if curNode.val != curNode.right.val:
                return False
    return True

#Test cases
root = TreeNode(1)
node1 = TreeNode(1)
node2 = TreeNode(1)
node3 = TreeNode(1)
node4 = TreeNode(1)
node5 = TreeNode(1)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
print(isUniTree(root))

root = TreeNode(2)
node1 = TreeNode(2)
node2 = TreeNode(2)
node3 = TreeNode(5)
node4 = TreeNode(2)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print(isUniTree(root))
