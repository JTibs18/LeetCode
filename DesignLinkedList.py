# Design your implementation of the linked list. You can choose to use a singly or doubly linked list.
# A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
# If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.
#
# Implement the MyLinkedList class:
#
# MyLinkedList() Initializes the MyLinkedList object.
# int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
# void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
# void addAtTail(int val) Append a node of value val as the last element of the linked list.
# void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
# void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList(object):

    def __init__(self):
        self.head = None

    def get(self, index):
        if (self.head):
            count = 0
            cur = self.head
            while(count <= index):
                if (count == index):
                    return cur.data
                elif (cur.next == None):
                    return -1
                else:
                    count += 1
                    cur = cur.next
        else:
            return -1

    def addAtHead(self, val):
        newNode = Node(val)
        if (self.head):
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def addAtTail(self, val):
        newNode = Node(val)
        if (self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, index, val):
        newNode = Node(val)
        if (self.head):
            count = 0
            cur = self.head
            if (index == 0):
                newNode.next = self.head
                self.head = newNode
                return
            while (cur.next and count <= index):
                if (count == (index - 1)):
                    newNode.next = cur.next
                    cur.next = newNode
                    break
                cur = cur.next
                count += 1
            if (count + 1 == index):
                cur.next = newNode
        else:
            self.head = newNode

    def deleteAtIndex(self, index):
        if (self.head):
            prev = self.head
            count = 0
            if (index == 0):
                self.head = self.head.next
                return
            elif (self.head.next):
                cur = self.head.next
                count += 1
                while (count <= index):
                    if (index == count):
                        if (cur.next):
                            prev.next = cur.next
                            return
                        else:
                            prev.next = None
                            return
                    else:
                        count += 1
                        prev = cur
                        if (cur.next):
                            cur = cur.next
                        else:
                            return


#Test cases
myLinkedList = MyLinkedList()
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(3)
myLinkedList.addAtIndex(1, 2)    #linked list becomes 1->2->3
print(myLinkedList.get(1))              # return 2
myLinkedList.deleteAtIndex(1)    # now the linked list is 1->3
print(myLinkedList.get(1))           # return 3

myLinkedList.addAtHead(7)
myLinkedList.addAtTail(7)
myLinkedList.addAtHead(9)
myLinkedList.addAtTail(8)
myLinkedList.addAtHead(6)
myLinkedList.addAtHead(0)
print(myLinkedList.get(5))
myLinkedList.addAtHead(0)
print(myLinkedList.get(2))
print(myLinkedList.get(5))
myLinkedList.addAtTail(4)
myLinkedList.addAtHead(84)
myLinkedList.addAtTail(2)
myLinkedList.addAtTail(39)
print(myLinkedList.get(3))
print(myLinkedList.get(1))
myLinkedList.addAtTail(42)
myLinkedList.addAtIndex(1, 80)
myLinkedList.addAtHead(14)
myLinkedList.addAtHead(1)
myLinkedList.addAtTail(53)
myLinkedList.addAtTail(98)
myLinkedList.addAtTail(19)
myLinkedList.addAtTail(12)
print(myLinkedList.get(2))
myLinkedList.addAtHead(16)
myLinkedList.addAtHead(33)
myLinkedList.addAtIndex(4, 17)
myLinkedList.addAtIndex(6, 8)
myLinkedList.addAtHead(37)
myLinkedList.addAtTail(43)
myLinkedList.deleteAtIndex(11)
myLinkedList.addAtHead(80)
myLinkedList.addAtHead(31)
myLinkedList.addAtIndex(13, 23)
myLinkedList.addAtTail(17)
print(myLinkedList.get(4))
myLinkedList.addAtIndex(10, 0)
myLinkedList.addAtTail(21)
myLinkedList.addAtHead(73)
myLinkedList.addAtHead(22)
myLinkedList.addAtIndex(24, 37)
myLinkedList.addAtTail(14)
myLinkedList.addAtHead(97)
myLinkedList.addAtHead(8)
print(myLinkedList.get(6))
myLinkedList.deleteAtIndex(17)
myLinkedList.addAtTail(50)
myLinkedList.addAtTail(28)
myLinkedList.addAtHead(76)
myLinkedList.addAtTail(79)
print(myLinkedList.get(18))
myLinkedList.deleteAtIndex(30)
myLinkedList.addAtTail(5)
myLinkedList.addAtHead(9)
myLinkedList.addAtTail(83)
myLinkedList.deleteAtIndex(3)
myLinkedList.addAtTail(40)
myLinkedList.deleteAtIndex(26)
myLinkedList.addAtIndex(20, 90)
myLinkedList.deleteAtIndex(30)
myLinkedList.addAtTail(40)
myLinkedList.addAtHead(56)
myLinkedList.addAtIndex(15, 23)
myLinkedList.addAtHead(51)
myLinkedList.addAtHead(21)
print(myLinkedList.get(26))
myLinkedList.addAtHead(83)
print(myLinkedList.get(30))
myLinkedList.addAtHead(12)
myLinkedList.deleteAtIndex(8)
print(myLinkedList.get(4))
myLinkedList.addAtHead(20)
myLinkedList.addAtTail(45)
print(myLinkedList.get(10))
myLinkedList.addAtHead(56)
print(myLinkedList.get(18))
myLinkedList.addAtTail(33)
print(myLinkedList.get(2))
myLinkedList.addAtTail(70)
myLinkedList.addAtHead(57)
myLinkedList.addAtIndex(31, 24)
myLinkedList.addAtIndex(16, 92)
myLinkedList.addAtHead(40)
myLinkedList.addAtHead(23)
myLinkedList.deleteAtIndex(26)
print(myLinkedList.get(1))
myLinkedList.addAtHead(92)
myLinkedList.addAtIndex(3, 78)
myLinkedList.addAtTail(42)
print(myLinkedList.get(18))
myLinkedList.addAtIndex(39, 9)
print(myLinkedList.get(13))
myLinkedList.addAtIndex(33, 17)
print(myLinkedList.get(51))
myLinkedList.addAtIndex(18, 95)
myLinkedList.addAtIndex(18, 33)
myLinkedList.addAtHead(80)
myLinkedList.addAtHead(21)
myLinkedList.addAtTail(7)
myLinkedList.addAtIndex(17, 46)
print(myLinkedList.get(33))
myLinkedList.addAtHead(60)
myLinkedList.addAtTail(26)
myLinkedList.addAtTail(4)
myLinkedList.addAtHead(9)
print(myLinkedList.get(45))
myLinkedList.addAtTail(38)
myLinkedList.addAtHead(95)
myLinkedList.addAtTail(78)
print(myLinkedList.get(54))
myLinkedList.addAtIndex(42, 86)
