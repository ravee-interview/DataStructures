class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """
        #edge cases
        if len(s) == 0:
            return 0
        memo = [-1 for x in range(len(s))]
        return self.num_decoding_helper(s,0,memo)
        
    
    def num_decoding_helper(self,s,index,memo):
        if index < len(s) and int(s[index]) == 0:
            return 0
        
        if index == len(s):
            return 1
        
        if memo[index] != -1:
            return memo[index]
        count = (self.num_decoding_helper(s,index+1,memo)) #call the next index  
        
        if index+1 < len(s) and int(s[index]+s[index+1]) < 27:
            count += (self.num_decoding_helper(s,index+2,memo))
        memo[index] = count
        
        return count 
            
