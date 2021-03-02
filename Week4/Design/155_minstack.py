from collections import deque
class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        self.length = 0
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        #push on stack
        #update length
        if not self.stack:
            curr_min = x
        else:
            curr_min = self.stack[self.length-1][1]
        curr_min = min(curr_min,x)
        self.stack.append((x,curr_min))
        self.length +=1

    def pop(self):
        """
        :rtype: None
        """
        #return top
        #update length
        if not self.stack:
            raise Error("Failed ... Attempting to remove from emtpy stack")
        self.length -=1
        return self.stack.pop()[0]

    def top(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise Error("Stack is empty")
        return self.stack[self.length-1][0]
        

    def getMin(self):
        """
        :rtype: int
        """
        if not self.stack:
            raise Error("Stack is empty")
        return self.stack[self.length-1][1]
        
        

"""
time complexity : o(1) for all
space complexity : o(n) where n are number of elements
"""
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#Edge cases:

