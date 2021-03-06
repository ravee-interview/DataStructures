from collections import deque
class MyQueue(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = deque()
        

    def push(self, x): #o(n)
        """
        Push element x to the back of queue.
        :type x: int
        :rtype: None
        """
        helper_stack = deque()
        while self.stack:
            helper_stack.append(self.stack.pop())
        self.stack.append(x)
        #transfer back
        while helper_stack:
            self.stack.append(helper_stack.pop())
            

    def pop(self): #o(1)
        """
        Removes the element from in front of queue and returns that element.
        :rtype: int
        """
        #pop from empty stack
        if self.empty():
            return
        return self.stack.pop()
        

    def peek(self): #o(1)
        """
        Get the front element.
        :rtype: int
        """
        if self.empty():
            return
        return self.stack[-1]
        

    def empty(self): #o(1)
        """
        Returns whether the queue is empty.
        :rtype: bool
        """
        if not self.stack:
            return True
        return False
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()


# push elements from stack in helper_stack
# push new element in stack
# push elements from helper stack into stack

