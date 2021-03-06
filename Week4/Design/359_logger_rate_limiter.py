from collections import deque
class Logger(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.messages = set()
        self.queue = deque()
        

    def shouldPrintMessage(self, timestamp, message):
        """
        Returns true if the message should be printed in the given timestamp, otherwise returns false.
        If this method returns false, the message will not be printed.
        The timestamp is in seconds granularity.
        :type timestamp: int
        :type message: str
        :rtype: bool
        """
        #non-empty queue
        #flush the queue first
        while self.queue and timestamp >= (self.queue[0][0] + 10):
            curr_message = self.queue.popleft()[1]
            self.messages.remove(curr_message)
        if message in self.messages:
            return False
        #update queue
        self.queue.append((timestamp,message))
        self.messages.add(message)
        return True
        
"""
time complexity : o(1) <- at most, we will be flushing 10
space complexity : o(1) <- constant, at most we will be storing 10
"""
        
        
# Your Logger object will be instantiated and called as such:
# obj = Logger()
# param_1 = obj.shouldPrintMessage(timestamp,message)
