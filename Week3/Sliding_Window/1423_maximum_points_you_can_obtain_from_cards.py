class Solution(object):
    def maxScore(self, cardPoints, k):
        """
        :type cardPoints: List[int]
        :type k: int
        :rtype: int
        """
        #edge cases: k == len, k > len
        n = len(cardPoints)
        max_sum = float("-inf")
        curr_sum = 0
        #K can be a circular window ; evaluate sum of first k
        curr_sum = sum(cardPoints[:k]) #first k elemetn
        max_sum = curr_sum 
        
        curr_sum = sum(cardPoints[(n-k):n]) #last k elements
        max_sum = max(curr_sum, max_sum)
        for start in range(n-k+1,n):
            #calculate end
            end = (start+k-1) % len(cardPoints) #wrap around
            curr_sum -= cardPoints[start-1]
            curr_sum += cardPoints[end]
            max_sum = max(curr_sum, max_sum)
        
        return max_sum
            
        """
        Time complexity: O(k)
        Space complexity: O(1)
        """
