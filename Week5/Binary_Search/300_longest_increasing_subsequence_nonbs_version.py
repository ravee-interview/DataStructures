class Solution(object):
    def lengthOfLIS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        result = [0 for _ in range(len(nums))]
        result[-1] = 1
        
        
        for curr_idx in range(len(nums)-2,-1,-1):
            max_len = 0
            for next_idx in range(curr_idx+1,len(nums)):
                if nums[curr_idx] < nums[next_idx]:
                    if result[next_idx] > max_len:
                        max_len = result[next_idx]
            result[curr_idx] = 1 + max_len
            
        return max(result)
            
"""
time complexity o(n^2)
space complexity o(n)
"""
