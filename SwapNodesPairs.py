# Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def swapPairs(head):
    dummy = ListNode(0)
    dummy.next = head

    prev = dummy
    p1 = head
    if head == None:
        return None
    else:
        p1 = head
        p2 = head.next

    if p1 != None and p2 != None:
        prev.next = p2
        p1.next = p2.next
        p2.next = p1
    else:
        return head

    while p1.next != None:
        prev = p1
        p2 = p1.next.next
        p1 = p1.next

        if p2 == None:
            return dummy.next
        if p2 != None:
            prev.next = p2
        if p2.next != None:
            p1.next = p2.next
        else:
            p1.next = None
        p2.next = p1

    return dummy.next

#Test cases
head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
head.next = node1
node1.next = node2
node2.next = node3
h = swapPairs(head)
print(h.val, h.next.val, h.next.next.val, h.next.next.next.val)

head = ListNode(1)
node1 = ListNode(2)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(5)
head.next = node1
node1.next = node2
node2.next = node3
node3.next= node4
h = swapPairs(head)
print(h.val, h.next.val, h.next.next.val, h.next.next.next.val, h.next.next.next.next.val)

h = ListNode(None)
print(swapPairs(h).val)

h1 = ListNode(1)
print(swapPairs(h1).val)
