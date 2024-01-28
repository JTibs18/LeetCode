# Given the head of a linked list head, in which each node contains an integer value.
# Between every pair of adjacent nodes, insert a new node with a value equal to the greatest common divisor of them.
# Return the linked list after insertion.
# The greatest common divisor of two numbers is the largest positive integer that evenly divides both numbers.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def insertGreatestCommonDivisors(head):
    prevNode = head
    curNode = head.next 

    while curNode:
        for i in range(min(curNode.val, prevNode.val), -1, -1):
            if curNode.val % i == 0 and prevNode.val % i == 0:
                prevNode.next = ListNode(i, curNode)
                prevNode = curNode
                curNode = curNode.next
                break

    return head 

# Test cases
l1 = ListNode(18)
l2 = ListNode(6)
l3 = ListNode(10)
l4 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
print(insertGreatestCommonDivisors(l1))

l1 = ListNode(7)
print(insertGreatestCommonDivisors(l1))
