# You are given two non-empty linked lists representing two non-negative integers.
# The digits are stored in reverse order, and each of their nodes contains a single digit.
# Add the two numbers and return the sum as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def addTwoNums(l1, l2):
    dummy = ListNode(0)

    def addNums(l1, l2, d, carry):
        if l1 != None and l2 != None:
            sum = l1.val + l2.val + carry
            dNext, carry = singleDigit(sum, carry, d)
            return addNums(l1.next, l2.next, dNext, carry)
        elif l1 != None and l2 == None:
            sum = l1.val + carry
            dNext, carry = singleDigit(sum, carry, d)
            return addNums(l1.next, l2, dNext, carry)
        elif l1 == None and l2 != None:
            sum = l2.val + carry
            dNext, carry = singleDigit(sum, carry, d)
            return addNums(l1, l2.next, dNext, carry)
        elif carry != 0:
            sum = carry
            dNext, carry = singleDigit(sum, carry, d)
            return dummy.next
        else:
            return dummy.next

    def singleDigit(sum, carry, d):
        if sum / 10 < 1:
            d.next = ListNode(sum)
            c = 0
            return d.next, c
        else:
            d.next = ListNode(sum % 10)
            c = sum // 10
            return d.next, c

    return addNums(l1, l2, dummy, 0)

#Test cases
l1 = ListNode(2)
node1 = ListNode(4)
node2 = ListNode(9)
l1.next = node1
node1.next = node2
l2 = ListNode(5)
n1 = ListNode(6)
n2 = ListNode(4)
n3 = ListNode(9)
l2.next = n1
n1.next = n2
n2.next = n3
print(addTwoNums(l1, l2))
