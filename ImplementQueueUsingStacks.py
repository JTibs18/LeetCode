# Implement a first in first out (FIFO) queue using only two stacks. The implemented queue should support all the functions of a normal queue (push, peek, pop, and empty).
# Implement the MyQueue class:
#   void push(int x) Pushes element x to the back of the queue.
#   int pop() Removes the element from the front of the queue and returns it.
#   int peek() Returns the element at the front of the queue.
#   boolean empty() Returns true if the queue is empty, false otherwise.
# Notes:
#   You must use only standard operations of a stack, which means only push to top, peek/pop from top, size, and is empty operations are valid.
#   Depending on your language, the stack may not be supported natively. You may simulate a stack using a list or deque (double-ended queue) as long as you use only a stack's standard operations.
 
class MyQueue:
    def __init__(self):
        self.stack = []
        self.queue = []

    def push(self, x):
        self.stack.append(x)
    
    def pop(self):
        if not self.queue:    
            while self.stack:
                self.queue.append(self.stack.pop())

        return self.queue.pop()
    
    def peek(self):
        if not self.queue: 
            while self.stack:
                self.queue.append(self.stack.pop())

        return self.queue[-1]

    def empty(self):
        if self.stack or self.queue:
            return False
        return True 

# Test cases
myQueue = MyQueue()
myQueue.push(1)
myQueue.push(2)
print(myQueue.peek())
print(myQueue.pop())
print(myQueue.empty())