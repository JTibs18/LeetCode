# Given a linked list, return the node where the cycle begins. If there is no cycle, return null.
# There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to.
# Note that pos is not passed as a parameter.
# Notice that you should not modify the linked list.

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def ListCycle(head):
    nodes = set()
    if head == None:
        return None
    else:
        cur = head
        nodes.add(cur)
        while(cur.next):
            cur = cur.next
            if (cur not in nodes):
                nodes.add(cur)
            else:
                 return cur
        return None

#Test case
head = ListNode(3)
node1 = ListNode(2)
node2 = ListNode(0)
node3 = ListNode(-4)
head.next = node1
node1.next = node2
node2.next = node3
node3.next = node1
print(ListCycle(head))

head = ListNode(1)
node1 = ListNode(2)
head.next = node1
node1.next = head
print(ListCycle(head))

head = ListNode(1)
print(ListCycle(head))
