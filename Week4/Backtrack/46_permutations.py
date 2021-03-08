class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        
        result = []
        def backtrack(pos=0):
            if pos == len(nums):
                result.append(nums[:])
            #fix curr_pos for position pos and then backtrack
            for curr_pos in range(pos,len(nums)):
                nums[pos],nums[curr_pos] = nums[curr_pos],nums[pos]
                backtrack(pos+1)
                nums[pos],nums[curr_pos] = nums[curr_pos],nums[pos]
        backtrack()
        return result
    
    
        """
        time complexity : loose upper bound - o(n*n!)
        space complexity : n!
        
        """
