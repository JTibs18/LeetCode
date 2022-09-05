# Given the head of a sorted linked list, delete all nodes that have duplicate numbers, leaving only distinct numbers from the original list. Return the linked list sorted as well.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def deleteDuplicates(head):
    if head == None:
        return head

    previousVal = head.val
    dummy = ListNode(0)
    dummy.next = head
    cur = head.next
    prev = dummy
    skip = False

    while cur != None:
        if previousVal == cur.val:
            prev.next = cur.next
            skip = True
        else:
            previousVal = cur.val
            if skip == False:
                prev = prev.next
            else:
                skip = False
        cur = cur.next

    return dummy.next

#Test cases
head = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)
n4 = ListNode(3)
n5 = ListNode(4)
n6 = ListNode(4)
n7 = ListNode(5)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
print(deleteDuplicates(head))

head = ListNode(1)
n2 = ListNode(1)
n3 = ListNode(1)
n4 = ListNode(2)
n5 = ListNode(3)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(deleteDuplicates(head))

head = ListNode(-3)
n2 = ListNode(-3)
n3 = ListNode(-2)
n4 = ListNode(-1)
n5 = ListNode(-1)
n6 = ListNode(0)
n7 = ListNode(0)
n8 = ListNode(0)
n9 = ListNode(0)
n10 = ListNode(0)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
n8.next = n9
n9.next = n10
print(deleteDuplicates(head))
