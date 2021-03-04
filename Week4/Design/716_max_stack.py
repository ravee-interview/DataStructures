from collections import deque
class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = deque()
        

    def push(self, x):
        """
        :type x: int
        :rtype: None
        """
        
        if not self.stack: #push when stack empty
            curr_max = x
        else:              #push when stack is full
            curr_max = max(x,self.peekMax())
        self.stack.append((x,curr_max))
        

    def pop(self):
        """
        :rtype: int
        """
        #pop when stack empty
        #pop when stack full
        if not self.stack:
            return #throw exception
        return self.stack.pop()[0]
        
        

    def top(self):
        """
        :rtype: int
        """
        #top when stack empty
        #top when stack full
        if not self.stack:
            return #throw exception
        return self.stack[-1][0]
        

    def peekMax(self):
        """
        :rtype: int
        """
        #peek when stack empty
        #peek when stack full
        if not self.stack:
            return #throw exception
        curr_max = self.stack[-1][1]
        return curr_max
        

    def popMax(self):
        """
        :rtype: int
        """
        #pop max when stack empty
        #pop max when stack full
        if not self.stack:
            return #throw exception
        max_in_stack = self.peekMax()
        stack2 = deque()
        num = self.pop()
        stack2.append(num)
        
        while num != max_in_stack:
            num = self.pop()
            stack2.append(num)
        
        popped_max = stack2.pop() #now stack2 top points to max_in_stack
        while stack2:
            num = stack2.pop()
            self.push(num)
        return popped_max
        


# Your MaxStack object will be instantiated and called as such:
# obj = MaxStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.peekMax()
# param_5 = obj.popMax()
