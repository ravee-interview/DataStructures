class Solution(object):
    
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        squares = [i**2 for i in range(1, int(math.sqrt(n)+1))]
        memo = {}
        
        def min_squares(num):
            if num in squares:
                return 1
        
            min_count = float("inf") #inf
            for square in squares:
                if num < square:
                    break
                if num in memo:
                    return memo[num]
                count = min_squares(num-square) + 1
                min_count = min(min_count, count)
            memo[num] = min_count
            return min_count
        
        
        return min_squares(n)
