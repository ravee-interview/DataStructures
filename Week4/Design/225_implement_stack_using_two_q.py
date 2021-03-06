class MyStack(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = deque()
        

    def push(self, x): #o(n)
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        helper_queue = deque()
        while self.queue:
            helper_queue.append((self.queue.popleft()))
        self.queue.append(x)
        while helper_queue:
            self.queue.append(helper_queue.popleft())
        

    def pop(self): #o(1)
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        if self.empty():
            return
        return self.queue.popleft()
        

    def top(self): #o(1)
        """
        Get the top element.
        :rtype: int
        """
        if self.empty():
            return
        return self.queue[0]
        

    def empty(self): #o(1)
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        if not self.queue:
            return True
        return False
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()

#push elements in queue in helper queue
#push new element in queue
#push elements from helper queue to queue
