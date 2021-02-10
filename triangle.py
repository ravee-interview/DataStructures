class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for level in range(1,len(triangle)):
            for i in range(len(triangle[level])):
                triangle[level][i] += self.get_min_path(triangle,level,i) #3,0
                print triangle[level][i]
        
        return min(triangle[len(triangle)-1])
    
    def get_min_path(self,triangle,level,i):
        prev_level = triangle[level-1]
        
        if i-1 < 0:
            return prev_level[i]   
        if i >= len(prev_level):
            return prev_level[i-1]   

        return min(prev_level[i], prev_level[i-1])
        
                
       #Got very confused with the constraints
    
                
        
    
    
    
'''
  
   2
  5 6
 11 10 13
15 11 18 16

t_len = 4
level = 2
len = 3
i = 0
  
'''  



#level 0 is the top of the triangle
#start from level 1
#t[level][i] = min(t[level-1][i], t[level][i-1])

'''
TS
n(n+1)/2 where n is the number of levels
'''
