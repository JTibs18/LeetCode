# Given the head of a sorted linked list, delete all duplicates such that each element appears only once. Return the linked list sorted as well.

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

def removeDups(head):
    cur = head
    nums = set()
    if head != None:
        nums.add(head.val)
        prev = cur
        while(cur.next):
            cur = cur.next
            if (cur.val not in nums):
                nums.add(cur.val)
                prev = cur
            else:
                prev.next = cur.next
    return head

#Test cases
headL = MyLinkedList()
headL.addAtHead(1)
headL.addAtTail(1)
headL.addAtTail(2)
x = removeDups(headL.head)
print(x.val, x.next.val)


headL = MyLinkedList()
headL.addAtHead(1)
headL.addAtTail(1)
headL.addAtTail(2)
headL.addAtTail(3)
headL.addAtTail(3)
x = removeDups(headL.head)
print(x.val, x.next.val, x.next.next.val)
