class MovingAverage(object):

    def __init__(self, size):
        """
        Initialize your data structure here.
        :type size: int
        """
        self.window_size = size
        self.queue = deque()
        self.total = 0
        self.curr_size = 0
        

    def next(self, val):
        """
        :type val: int
        :rtype: float
        """
        
        if self.curr_size == self.window_size:
            self.total -= self.queue.popleft()
            self.curr_size -= 1
        self.queue.append(val)
        self.total += val
        self.curr_size += 1
        avg = float(float(self.total)/self.curr_size)
        return avg
            
"""
time complexity: O(1)
space complexity: 0(n)
"""
        
        
        
        


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
