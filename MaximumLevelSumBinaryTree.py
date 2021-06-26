# Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.
# Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

def maxLevelSum(root):
    q = []
    prevLev = 1
    levCount = 0
    largestCount = root.val
    smallestLev = 1
    q.append([root, 1])

    #looping through queue
    while(len(q) > 0):
        #info on the current node
        cur = q.pop(0)
        node = cur[0]
        l = cur[1]

        #summing values of nodes on same level
        if prevLev == l:
            levCount += node.val
        else:
            if levCount > largestCount:
                smallestLev = prevLev
                largestCount = levCount
            levCount = node.val
            prevLev = l

        #adding child nodes to queue
        if node.right != None:
            q.append([node.right, l + 1])
        if node.left != None:
            q.append([node.left, l + 1])

    #checking if the sum of the level is the largest sum and returning its level
    if levCount > largestCount:
        smallestLev = prevLev
    return smallestLev

#Test cases
root = TreeNode(1)
node1 = TreeNode(7)
node2 = TreeNode(0)
node3 = TreeNode(7)
node4 = TreeNode(-8)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
print(maxLevelSum(root))

root = TreeNode(989)
node1 = TreeNode(10250)
node2 = TreeNode(98693)
node3 = TreeNode(-89388)
node4 = TreeNode(-32127)
root.right = node1
node1.left = node2
node1.right = node3
node3.right = node4
print(maxLevelSum(root))

root=TreeNode(1)
node1 = TreeNode(2)
node2 = TreeNode(3)
root.left = node1
root.right = node2
print(maxLevelSum(root))

root = TreeNode(-100)
node1 = TreeNode(-200)
node2 = TreeNode(-300)
node3 = TreeNode(-20)
node4 = TreeNode(-5)
node5 = TreeNode(-10)
root.left = node1
root.right = node2
node1.left = node3
node1.right = node4
node2.left = node5
print(maxLevelSum(root))
