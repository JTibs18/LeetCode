# Merge two sorted linked lists and return it as a sorted list.
# The list should be made by splicing together the nodes of the first two lists.




#loop through one list
#Compare first element in each list
#If element in list1 >= list2 continue looping
#otherwise add element from list2 after element in list1 and increase comparison pointer to next element in list2

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

def mergeTwoLists(l1: ListNode, l2:ListNode) -> ListNode:
    curNode = l1.head
    l2Node = l2.head
    p = ListNode(0)
    dummyHead = p
    if (l1.head == None and l2.head == None): return None
    elif (l1.head == None and l2.head != None): return l2
    elif (l1.head != None and l2.head == None): return l1
    else:
        while(curNode and l2Node):
            if (curNode.val <= l2Node.val):
                p.next = curNode
                curNode = curNode.next
                p = p.next
            else:
                p.next = l2Node
                l2Node = l2Node.next
                p = p.next
        while(curNode):
            p.next = curNode
            curNode = curNode.next
            p = p.next
        while(l2Node):
            p.next = l2Node
            l2Node = l2Node.next
            p = p.next
        return dummyHead.next

#Test cases
l1 = MyLinkedList()
l1.addAtHead(1)
l1.addAtTail(2)
l1.addAtTail(4)

l2 = MyLinkedList()
l2.addAtHead(1)
l2.addAtTail(3)
l2.addAtTail(4)

mergeTwoLists(l1, l2)
# Output: [1,1,2,3,4,4]
