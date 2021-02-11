class Solution(object):
    def longestPalindromeSubseq(self, text1):
        """
        :type s: str
        :rtype: int
        """
        text2 = text1[::-1] #reverse the string and find lcs
        #You want to find the longest subsequence which is also a palindrome
        
        lcs = [[[] for x in range(len(text2)+1)] for y in range(len(text1)+1)]
        
        for r in range(1,len(text1)+1):
            for c in range(1,len(text2)+1):
                
                if text1[r-1] == text2[c-1]:
                    lcs[r][c] = lcs[r-1][c-1] + [text1[r-1]]     
                else:
                    lcs[r][c] = max(lcs[r-1][c], lcs[r][c-1], key=len)
                    
        return len(lcs[len(text1)][len(text2)])
        
    

        
        
        '''

        '''

                    
        
        #[] + [b] -> [b]
        
        '''
        lcs
        r = 1
        c = 2
        bbbab <-text
        babbb <- r_text
        
           ""  b  b  b  a  b <-text
        "" [] [] [] [] [] []
        b  [] b  [] [] [] [] 
        a  [] [] [] [] [] []
        b  [] [] [] [] [] []
        b  [] [] [] [] [] [] 
        b  [] [] [] [] [] []
        
        
        '''

    
        
