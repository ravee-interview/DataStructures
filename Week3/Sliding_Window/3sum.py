class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if len(nums) <=2:
            return []
        nums.sort()
        result = []
        for i in range(len(nums)-2):
            if nums[i] > 0:
                break
            if i > 0 and nums[i-1] == nums[i]:
                continue
            left = i+1
            right = len(nums)-1
            while left < right:
                target = -1 * nums[i]
                two_sum = nums[left] + nums[right]
                if two_sum == target:
                    print i
                    result.append([nums[i],nums[left],nums[right]])
                    left +=1
                    right -=1
                    while left < right and nums[left] == nums[left-1]:
                        left +=1
                elif two_sum > target:
                    right -=1
                else:
                    left +=1
        return result
                    
"""
time complexity : O(n^2)
space complexity : O(n) or nlogn for sorting algorithm, O(n) for holding result
"""
