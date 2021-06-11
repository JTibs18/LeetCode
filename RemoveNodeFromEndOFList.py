# Given the head of a linked list, remove the nth node from the end of the list and return its head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

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

def removeFromEnd(head, n):
    cur = head
    count = 0
    while (cur.next):
        count += 1
        cur = cur.next
    removeNode = count - n
    if (count == 0 and n == 1):
        return None
    else:
        cur = head
    if n == count + 1:
        head = cur.next
        return head
    else:
        for num in range(removeNode):
            cur = cur.next
        cur.next = cur.next.next
        return head

#Test cases
headL = MyLinkedList()
headL.addAtHead(1)
headL.addAtTail(2)
headL.addAtTail(3)
headL.addAtTail(4)
headL.addAtTail(5)

x = removeFromEnd(headL.head, 2)
print(x.val, x.next.val, x.next.next.val, x.next.next.next.val)


headL = MyLinkedList()
headL.addAtHead(1)

x = removeFromEnd(headL.head, 1)
print(x)


headL = MyLinkedList()
headL.addAtHead(1)
headL.addAtTail(2)
x = removeFromEnd(headL.head, 2)
print(x.val)
