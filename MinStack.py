# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.
# Implement the MinStack class:
#   MinStack() initializes the stack object.
#   void push(int val) pushes the element val onto the stack.
#   void pop() removes the element on the top of the stack.
#   int top() gets the top element of the stack.
#   int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:
    def __init__(self):
        self.minStack = []
        self.stack = []
    
    def push(self, val):
        self.stack.append(val)
        if not self.minStack or val < self.minStack[-1]:
            self.minStack.append(val)
        else:
            self.minStack.append(self.minStack[-1])

    def pop(self):
        self.minStack.pop()
        self.stack.pop()
    
    def top(self):
        return self.stack[-1]

    def getMin(self):
        return self.minStack[-1]

# Test case
minStack = MinStack()
minStack.push(-2)
minStack.push(0)
minStack.push(-3)
print(minStack.getMin())
minStack.pop()
print(minStack.top())
print(minStack.getMin())
