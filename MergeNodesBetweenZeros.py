# You are given the head of a linked list, which contains a series of integers separated by 0's. The beginning and end of the linked list will have Node.val == 0.
# For every two consecutive 0's, merge all the nodes lying in between them into a single node whose value is the sum of all the merged nodes. The modified list should not contain any 0's.
# Return the head of the modified linked list.

#For weekly contest 281. Accepted

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def mergeNodes(head):
    cur = head.next
    sums = []
    sum = 0

    while (cur != None):
        if cur.val == 0:
            sums.append(sum)
            sum = 0
        else:
            sum += cur.val
        cur = cur.next

    node = ListNode(0)
    head = node

    for i in sums:
        node.next = ListNode(i)
        node = node.next

    return head.next

#Test cases
head = ListNode(0)
n2 = ListNode(3)
n3 = ListNode(1)
n4 = ListNode(0)
n5 = ListNode(4)
n6 = ListNode(5)
n7 = ListNode(2)
n8 = ListNode(0)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
print(mergeNodes(head))

head = ListNode(0)
n2 = ListNode(1)
n3 = ListNode(0)
n4 = ListNode(3)
n5 = ListNode(0)
n6 = ListNode(2)
n7 = ListNode(2)
n8 = ListNode(0)
head.next = n2
n2.next = n3
n3.next = n4
n4.next = n5
n5.next = n6
n6.next = n7
n7.next = n8
print(mergeNodes(head))
