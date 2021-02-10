class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])     
        
        #for the first row and column, add the previous entry as it is the only possible path
        for r in range(1,m):
            grid[r][0] += grid[r-1][0]
        
        for c in range(1,n):
            grid[0][c] += grid[0][c-1]
        
        for r in range(1,m):
            for c in range(1,n):
                grid[r][c] += min(grid[r-1][c], grid[r][c-1])
        
        return grid[m-1][n-1]
                
        """
        TS
        O(m*n)
        O(1)
        
        """
