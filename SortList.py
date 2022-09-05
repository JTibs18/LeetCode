# Given the head of a linked list, return the list after sorting it in ascending order.
# Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#ALGORITHM IS TOO SLOW

def sortList(head):
    if head == None or head.next == None:
        return head
    prev = ListNode(0)
    prev.next = head
    p1 = head
    p2 = head.next

    while(p1.val <= p2.val):
        prev = p1
        p1 = p2
        p2 = p2.next
        if p2 == None:
            return head

    prev.next = p2
    p1.next = p2.next
    p2.next = p1
    if p1 == head:
        head = p2

    return sortList(head)

#Test cases
head = ListNode(4)
node1 = ListNode(2)
node2 = ListNode(1)
node3 = ListNode(3)
head.next = node1
node1.next = node2
node2.next = node3
sorted = sortList(head)
print(sorted.val, sorted.next.val, sorted.next.next.val, sorted.next.next.next.val)

head = ListNode(-1)
node1 = ListNode(5)
node2 = ListNode(3)
node3 = ListNode(4)
node4 = ListNode(0)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
s = sortList(head)
print(s.val, s.next.val, s.next.next.val, s.next.next.next.val, s.next.next.next.next.val)

head = None
print(sortList(head))

head = ListNode(4)
node1 = ListNode(19)
node2 = ListNode(14)
node3 = ListNode(5)
node4 = ListNode(-3)
node5 = ListNode(1)
node6 = ListNode(8)
node7 = ListNode(5)
node8 = ListNode(11)
node9 = ListNode(15)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node4
node4.next = node5
node5.next = node6
node6.next = node7
node7.next = node8
node8.next = node9

s = sortList(head)
print(s.val, s.next.val, s.next.next.val, s.next.next.next.val, s.next.next.next.next.val)
