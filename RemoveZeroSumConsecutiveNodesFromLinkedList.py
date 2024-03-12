# Given the head of a linked list, we repeatedly delete consecutive sequences of nodes that sum to 0 until there are no such sequences.
# After doing so, return the head of the final linked list.  You may return any such answer.

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def removeZeroSumSublists(head):
    curSum = 0
    prefixSum = dict()
    dummyNode = ListNode(0)

    dummyNode.next = head 
    curNode = dummyNode

    while curNode:
        curSum += curNode.val 

        if curSum in prefixSum:
            toDelete = prefixSum[curSum].next
            newSum = curSum + toDelete.val 

            while toDelete != curNode:
                del prefixSum[newSum]
                toDelete = toDelete.next 
                newSum += toDelete.val

            prefixSum[curSum].next = curNode.next 
        else:
            prefixSum[curSum] = curNode 

        curNode = curNode.next 

    return dummyNode.next
        
# Test cases
head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(-3)
n3 = ListNode(3)
n4 = ListNode(1)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
print(removeZeroSumSublists(head))

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(-3)
n4 = ListNode(4)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4 
print(removeZeroSumSublists(head))

head = ListNode(1)
n1 = ListNode(2)
n2 = ListNode(3)
n3 = ListNode(-3)
n4 = ListNode(-2)
head.next = n1
n1.next = n2
n2.next = n3
n3.next = n4 
print(removeZeroSumSublists(head))
