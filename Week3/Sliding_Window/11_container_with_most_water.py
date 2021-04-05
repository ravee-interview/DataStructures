class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        #area = (j-i) * min(height[j],height[i])
        #two pointers, run each and find the running max
        #incremenet/decrement the pointer holding the smaller values
        #start outward as we have max lengths there
        max_area = 0
        left_idx = 0
        right_idx = len(height) - 1
        
        while left_idx < right_idx:
            current_area = min(height[left_idx], height[right_idx]) * (right_idx -  left_idx) # calculating the current area
            max_area = max(max_area, current_area) # update the max_area
            if height[left_idx] < height[right_idx]:
                left_idx += 1
            else:
                right_idx -= 1
        
        return max_area
    
    
    #t/s o(n) / o(1)
