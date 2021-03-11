class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix:
            return False
        if not matrix[0]:
            return False
        
        self.matrix = matrix
        #first find the row with first integer just smaller than target
        #in that row, apply binary search
        
        target_row = self.binary_search_column(target)
        return self.binary_search(self.matrix[target_row],target)
        
    def binary_search(self,array, target):
        start = 0
        end = len(array)-1
        while (start <= end):
            mid = (start+end)//2
            if target == array[mid]:
                return True
            elif target < array[mid]:
                end = mid-1
            else:
                start = mid+1
        return False
        
    def binary_search_column(self,target):
        R = len(self.matrix)
        
        left = 0
        right = R-1
        smaller_idx = left
        
        while left <= right:
            mid = (left+right)//2
            if target == self.matrix[mid][0]:
                return mid
            elif self.matrix[mid][0] < target: #search for a  smaller idx than target in the right
                smaller_idx = mid
                left = mid+1
            else: #search in left part
                right = mid-1
        return smaller_idx
"""
time complexity : o (logm + log n) for m rows and n cols
space complexity : o(1)
"""
                
