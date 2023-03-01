# Given the head of a linked list and an integer val, remove all the nodes of the linked list that has Node.val == val, and return the new head.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeElements(head, val):
    dummy = ListNode(-1)
    dummy.next = head

    def findElements(dummy, prev, head, val): 
        if head == None or head.next == None:
            if head != None and head.val == val: 
                prev.next = None 
            if dummy.next == None: 
                return None
            return dummy.next
        if head.val == val: 
            prev.next = head.next 
            return findElements(dummy, prev, prev.next, val)
        else: 
            return findElements(dummy, head, head.next, val)
        
    return findElements(dummy, dummy, head, val)

#Test cases
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(6)
node3 = ListNode(3)
node4 = ListNode(4)
node5 = ListNode(5)
node6 = ListNode(6)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6 
val = 6
print(removeElements(head, val))

head = ListNode(7)
n1 = ListNode(7)
n2 = ListNode(7)
n3 = ListNode(7)
head.next = n1
n1.next = n2
n2.next = n3
val = 7
print(removeElements(head, val))

head = ListNode()
val = 1
print(removeElements(head, val))
