class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        #Build a 2d grid
        grid = [([1] * n)] * m #QUESTION: is this a good way to declare?
        #Alternate declaration
        #[[1 for x in range(n)] for x in range(m)]
        
        for r in range(1,m):
            for c in range(1,n):
                grid[r][c] = grid[r-1][c] + grid[r][c-1]
        return grid[m-1][n-1]
        
    

                                               
        
        
        '''
        m = 3
        n = 4
        r2
        c3
        
        c0  c1 c2 c3
      r0 10  6  3  1
      r1 4  3  2  1
      r2 1  1  1  1
      
      
        
    recursion stack = r0c0,r0c1
     
        if bottom right is reached, return 1
        
        for every position, calculate the
        up(r,c) = up(r+1,c)+up(r,c+1)
        return up(0,0)
        
        '''
