# Given the head of a linked list, return the list after sorting it in ascending order.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def getMiddle(head):
    if head == None:
        return head

    slowPTR = head
    fastPTR = head

    while(fastPTR.next != None and fastPTR.next.next != None):
        slowPTR = slowPTR.next
        fastPTR = fastPTR.next.next

    return slowPTR

def sortedMerge(left, right):
    result = None

    if left == None:
        return right
    if right == None:
        return left

    if left.val <= right.val:
        result = left
        result.next = sortedMerge(left.next, right)
    else:
        result = right
        result.next = sortedMerge(left, right.next)

    return result

def sortList(head):
    if head == None or head.next == None:
        return head

    middle = getMiddle(head)
    nextMid = middle.next

    middle.next = None

    left = sortList(head)
    right = sortList(nextMid)

    sortedList = sortedMerge(left, right)
    return sortedList

# Test Cases
head = ListNode(4)
n2 = ListNode(2)
n3 = ListNode(1)
n4 = ListNode(3)
head.next = n2
n2.next = n3
n3.next = n4
print(sortList(head))

head = ListNode(-1)
n2 = ListNode(5)
n3 = ListNode(3)
n4 = ListNode(4)
n5 = ListNode(0)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
print(sortList(head))

head = ListNode(None)
print(sortList(head))
