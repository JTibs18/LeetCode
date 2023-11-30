# Design a stack that supports increment operations on its elements.
# Implement the CustomStack class:
#   CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
#   void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
#   int pop() Pops and returns the top of the stack or -1 if the stack is empty.
#   void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.

class CustomStack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stack = []

    def push(self, x):
        if len(self.stack) < self.maxSize: 
            self.stack.append(x)
    
    def pop(self):
        if self.stack:
            return self.stack.pop()
        return -1 

    def increment(self, k, val):
        self.stack = [x + val for x in self.stack[:k]] + self.stack[k:]

# Test cases
customStack = CustomStack(3)
customStack.push(1)
customStack.push(2)
print(customStack.pop())
customStack.push(2)
customStack.push(3)
customStack.push(4)
customStack.increment(5, 100)
customStack.increment(2, 100)
print(customStack.pop())
print(customStack.pop())
print(customStack.pop())
print(customStack.pop())



