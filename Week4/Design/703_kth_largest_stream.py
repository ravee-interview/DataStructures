class KthLargest(object):

    def __init__(self, k, nums):    #o((n-k)logk)
        """
        :type k: int
        :type nums: List[int]
        """
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums)
        while len(nums) > k:
            heapq.heappop(self.nums)
        
        

    def add(self, val): #o(logk)
        """
        :type val: int
        :rtype: int
        """
        if len(self.nums) < self.k:
            heapq.heappush(self.nums,val)
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums,val)
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
