# Given the root of a binary tree, imagine yourself standing on the right side of it, return the values of the nodes you can see ordered from top to bottom.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def rightSideView(root):
    rightSide = []
    q = []

    if root == None:
        return rightSide
    q.append(root)

    while q:
        levelSize = len(q)
        level = []

        for x in range(levelSize):
            curNode = q.pop(0)
            level.append(curNode)

            if curNode.left:
                q.append(curNode.left)
            if curNode.right:
                q.append(curNode.right)

        rightSide.append(level[len(level) - 1].val)
    return rightSide

#Test cases
root = TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
node3 = TreeNode(5)
node4 = TreeNode(4)
root.left = node1
root.right = node2
node1.right = node3
node2.right = node4
print(rightSideView(root))

r = TreeNode(1)
node1 = TreeNode(2)
r.left = node1
print(rightSideView(r))
