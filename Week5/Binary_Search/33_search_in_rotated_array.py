class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        #edge case
        if not nums:
            raise ValueError("empty array")
        start = 0
        end = len(nums) - 1
        
        while start <= end:
            mid = (start+end) //2 
            if target == nums[mid]:
                return mid
            elif nums[start] <= nums[mid]: #non-rotated first half
                if target >= nums[start] and target < nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if target <= nums[end] and target > nums[mid]:
                    start = mid + 1
                else:
                    end = mid - 1
            
        return -1
    
'''
t o(logn)
s o(1)
'''
#     nums0 = []
#     nums1 = [4] target = 4
#     nums2 = [4] target = 5
#     nums3 = [4 5 6 7 0 1 2], target = 2
#     nums4 = [4 5 6 7 0 1 2], target = 4
#     nums5 = [5 6 7 8 9 0 1 2 4], target = 6
#     nums7 = [3 1 2], target = 2
        
#     [5 6 7 0 1 2 4]
#              | |  |
