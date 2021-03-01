class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        #edge cases
        i = 0
        j = 0
        intersect = []
        
        #Assuming arrays are already sorted by themselves
        while i < len(firstList) and j < len(secondList):
            start1 = firstList[i][0]
            end1 = firstList[i][1]
            start2 = secondList[j][0]
            end2 = secondList[j][1]
            higher_start = max(start1,start2)
            lower_end = min(end1,end2)
            
            if higher_start <= lower_end:
                intersect.append([higher_start, lower_end])
            if end1 > end2:
                j +=1
            else:
                i +=1
        return intersect
        
"""
time complexity : O(n+m)
space complexity : O(1) extra space, O(n+m) total space
"""       
        
        
        #increment the index with lower end
#         [0,2],[5,10],[13,23],[24,25]
#                        i
#         [1,5],[8,12],[15,24],[25,26]
#                j
            
#         [1 2][5,5]
