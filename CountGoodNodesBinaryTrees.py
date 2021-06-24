# Given a binary tree root, a node X in the tree is named good if in the path from root to X there are no nodes with a value greater than X.
# Return the number of good nodes in the binary tree.
 
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def goodNodes(root):
    def helperFun(node, max):
        if node == None:
            return 0
        elif node.val >= max:
            max = node.val
            return helperFun (node.left, max) + helperFun(node.right, max) + 1
        else:
            return helperFun(node.left, max) + helperFun(node.right, max)

    m = root.val
    return helperFun(root.left, m) + helperFun(root.right, m) + 1

#Test cases
root = TreeNode(3)
node1 = TreeNode(1)
node2 = TreeNode(4)
node3 = TreeNode(3)
node4 = TreeNode(1)
node5 = TreeNode(5)
root.left = node1
root.right = node2
node1.left = node3
node2.right = node5
node2.left = node4
print(goodNodes(root))

root = TreeNode(3)
node1 = TreeNode(3)
node2 = TreeNode(4)
node3 = TreeNode(2)
root.left = node1
node1.left = node2
node1.right = node3
print(goodNodes(root))

root = TreeNode(1)
print(goodNodes(root))

root = TreeNode(2)
node1 = TreeNode(4)
node2 = TreeNode(4)
node3 = TreeNode(4)
node4 = TreeNode(1)
node5 = TreeNode(3)
node6 = TreeNode(5)
node7 = TreeNode(5)
node8 = TreeNode(4)
node9 = TreeNode(4)
root.left = node1
root.right = node2
node1.left = node3
node2.left = node4
node2.right = node5
node4.left = node6
node6.right = node7
node7.left = node8
node7.right = node9
print(goodNodes(root))
