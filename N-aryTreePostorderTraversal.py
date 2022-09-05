# Given the root of an n-ary tree, return the postorder traversal of its nodes' values.
# Nary-Tree input serialization is represented in their level order traversal. Each group of children is separated by the null value (See examples)

# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

def postorder(root):

    def helperFun(node, output):
        if node == None:
            return None

        if node.children != None:
            for i in node.children:
                output.append(helperFun(i, output))

        if root == node:
            output.append(node.val)
            return output

        return node.val

    return helperFun(root, [])

#Test Cases:
root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
root.children = [n3, n2, n4]
n3.children = [n5, n6]
print(postorder(root))

root = Node(1)
n2 = Node(2)
n3 = Node(3)
n4 = Node(4)
n5 = Node(5)
n6 = Node(6)
n7 = Node(7)
n8 = Node(8)
n9 = Node(9)
n10 = Node(10)
n11 = Node(11)
n12 = Node(12)
n13 = Node(13)
n14 = Node(14)
root.children = [n2, n3, n4, n5]
n3.children = [n6, n7]
n7.children = [n11]
n11.children = [n14]
n4.children = [n8]
n8.children = [n12]
n5.children = [n9, n10]
n9.children = [n13]
print(postorder(root))
