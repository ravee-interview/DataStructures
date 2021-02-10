class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])
        is_reach_end = False
        obstacle = 1
        #space = 0

        #Obstacle at beginning and end
        if obstacleGrid[0][0] == 1 or obstacleGrid[nrows-1][ncols-1] == 1:
            return 0
        
        #column vector
        if nrows == 1:
            for c in range(ncols):
                if obstacleGrid[0][c] == obstacle:
                    return 0
            return 1
        #row vector
        if ncols == 1:
            for r in range(nrows):
                if obstacleGrid[r][0] == obstacle:
                    return 0
            return 1
        
        #first row and column reachability
        for r in range(1,nrows):
            if obstacleGrid[r-1][0] == obstacle:
                obstacleGrid[r][0] = 1
        for c in range(1,ncols):
            if obstacleGrid[0][c-1] == obstacle:
                obstacleGrid[0][c] = 1        
        
        #revaluating obstacles to be 0 instead of 1       
        obstacle = 0
        #space = 1
        for r in range(nrows):
            for c in range(ncols):
                if obstacleGrid[r][c] == 1: #revaluating obstacles to be 0 instead of 1
                    obstacleGrid[r][c] = 0
                else:
                    obstacleGrid[r][c] = 1 #if no obstacle, then revalue to 1
                    
        for r in range(1,nrows):
            for c in range(1,ncols):
                if r == nrows-1 and c == ncols-1:
                    is_reach_end = True
                if obstacleGrid[r][c] != obstacle: #if there is a path
                    obstacleGrid[r][c] = obstacleGrid[r][c-1] + obstacleGrid[r-1][c]
        if not is_reach_end:
            return 0
        print is_reach_end
        return obstacleGrid[nrows-1][ncols-1]
    
    #Missed a few edge cases here:
        #Obstacle at beginning 
        #Obstacle at end
        #entire obstacle row
        #entire obstacled column
        #obstacle at first row and column
