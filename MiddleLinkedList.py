# Given a non-empty, singly linked list with head node head, return a middle node of linked list.
# If there are two middle nodes, return the second middle node.

class ListNode:
    def __init__(self, val):
        self.val = val
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
                    return cur.val
                elif (cur.next == None):
                    return -1
                else:
                    count += 1
                    cur = cur.next
        else:
            return -1

    def addAtHead(self, val):
        newNode = ListNode(val)
        if (self.head):
            newNode.next = self.head
            self.head = newNode
        else:
            self.head = newNode

    def addAtTail(self, val):
        newNode = ListNode(val)
        if (self.head):
            cur = self.head
            while(cur.next):
                cur = cur.next
            cur.next = newNode
        else:
            self.head = newNode

    def addAtIndex(self, index, val):
        newNode = ListNode(val)
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

def Middle(head):
    p1 = head
    p2 = head.next
    while (p1 and p2):
        if (p2.next and p2.next.next):
            p2 = p2.next.next
            p1 = p1.next
        elif (p1.next):
            return p1.next
    return p1

#Test cases
headL = MyLinkedList()
headL.addAtHead(1)
headL.addAtTail(2)
headL.addAtTail(3)
headL.addAtTail(4)
headL.addAtTail(5)
headL.addAtTail(6)

x = Middle(headL.head)
print("MIDDLE: ", x.val)
