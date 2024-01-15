# Given the head of a singly linked list, reverse the list, and return the reversed list.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseList(head):
    if not head:
        return None
    
    dummy = ListNode(-1)
    
    def helper(curNode, newLL):
        if curNode.next:
            newLL = helper(curNode.next, newLL)
        newNode = ListNode(curNode.val)
        newLL.next = newNode
        return newNode
    
    helper(head, dummy)
    return dummy

# Test cases
head = ListNode(1)
l1 = ListNode(2)
l2 = ListNode(3)
l3 = ListNode(4)
l4 = ListNode(5)
head.next = l1
l1.next = l2
l2.next = l3
l3.next = l4
print(reverseList(head))

# head = ListNode(1)
# l1 = ListNode(2)
# head.next = l1
# print(reverseList(head))

# print(reverseList(None))