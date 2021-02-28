from collections import defaultdict
class Solution(object):
    def lengthOfLongestSubstringKDistinct(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        if k == 0:
            return 0
        
        left = 0
        right = 0
        counter = defaultdict(int)
        max_sub_len = 0
        curr_len = 0 #for calculating curr lenght of the valid substring found.
        
        while right < len(s): 
            right_char = s[right]
            counter[right_char] +=1
            curr_len +=1 #increment with eevry increment in right pointer
            
            if len(counter) <= k and curr_len > max_sub_len:
                max_sub_len = curr_len
               
            while left < right and len(counter) > k: #increment left pointer
                left_char = s[left]
                curr_len -=1 #subtract with every increment in left pointer
                counter[left_char] -=1
                if counter[left_char] == 0:
                    del(counter[left_char])
                left +=1
                
            right +=1
            
        return max_sub_len
                
            
        """
        Time complexity: O(n)
        Space complexity: O(n)
        """
            
            
