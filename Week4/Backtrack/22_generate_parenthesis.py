from collections import deque
class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        result = []
        def generate(n, combination, num_open):
            if num_open < 0: #cannot ever start with a closing bracket
                return
            elif n == 0:
                if num_open == 0:
                    result.append(combination)
                return
                
            generate(n-1, combination+'(',num_open+1)
            generate(n-1, combination+')',num_open-1)
        
        
        m = 2*n
        generate(m, '',0)
        return result
    
    
    """
        def is_valid(self, brackets):
        num_open = 0
        
        for bracket in brackets:
            if num_open < 0:
                return False
            if bracket == '(':
                num_open +=1
            elif bracket == ')':
                num_open -=1
        
        return num_open == 0
    
    """

            
"""
3 ( 
2  )
2 (

"""
