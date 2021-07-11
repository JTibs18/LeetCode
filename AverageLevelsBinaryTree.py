# Given the root of a binary tree, return the average value of the nodes on each level in the form of an array. Answers within 10-5 of the actual answer will be accepted.

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def averageLevels(root):
    q = []
    average = []

    q.append(root)

    while q:
        levelSize = len(q)
        levelNodes = []

        for n in range(levelSize):
            curNode = q.pop(0)
            levelNodes.append(curNode.val)

            if curNode.left != None:
                q.append(curNode.left)
            if curNode.right != None:
                q.append(curNode.right)

        average.append(sum(levelNodes) / len(levelNodes))

    return average

#Test cases
root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
root.left = node1
root.right = node2
node2.left = node3
node2.right = node4
print(averageLevels(root))

root = TreeNode(3)
node1 = TreeNode(9)
node2 = TreeNode(20)
node3 = TreeNode(15)
node4 = TreeNode(7)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print(averageLevels(root))
