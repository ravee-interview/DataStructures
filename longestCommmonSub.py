class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        """
        :type text1: str
        :type text2: str
        :rtype: int
        """
        lcs = [[[] for x in range(len(text2)+1)] for y in range(len(text1)+1)]
       
        
        for r in range(1,len(text1)+1):
            for c in range(1,len(text2)+1):
                #if equal characters, current entry = char + diagonal entry
                if text1[r-1] == text2[c-1]:
                    lcs[r][c] = lcs[r-1][c-1] + [text1[r-1]]
                else:
                    lcs[r][c] = max(lcs[r-1][c], lcs[r][c-1],key=len)
        
        #sequence = reversed("".join(lcs[len(text1)][len(text2)]))
        #print sequence
        return len(lcs[len(text1)][len(text2)])
                    
        '''
        abcde   r = 1
        ace     c = 2
        
          ""  a  c  e
       "" "" "" "" ""
        a "" a  a  a
        b "" a  a  a
        c "" a  ac ac
        d "" a  ac ac
        e "" a  ac ace
        
        o(m*n)
        o(m*n)
        
        '''
