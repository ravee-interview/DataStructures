class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        
        max_size = 0
        
        index_map = {}
        
        start = 0   #window is from start to end
        
        for end in range(len(s)):
            if s[end] in index_map:
                start = max(start, index_map[s[end]]) #reset start to curren non-repeating elemtn

            max_size = max(max_size, end - start + 1)
            index_map[s[end]] = end + 1
        
        return max_size
    
    
    """
    Time complexity : O(n)
    Space complexity: O(1)
    """
    #Test Cases
#     str0 = ""
#     str1 = "a"
#     str2 = "abcdgabc"
#     str3 = "ac"
    
#     "abccgabc"
#         s
        
#     len = 8
#     start = 4
#     end = 4
#     max_size = 3
#     index_map = {a : 1 b: 2 c: 3 g: 4}
