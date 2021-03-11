# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int
        """
        #find the mid version
        #if it's a bad version log it as potential first bad version, search for earlier version in the left
        #else search for bad version in right

        start = 1 #1 based
        end = n
        
        first_bad_version = 0
        while start <= end:
            mid = (start+end)//2
            if isBadVersion(mid):
                first_bad_version = mid
                end = mid - 1
            else:
                start = mid + 1
        return first_bad_version

"""
time complexity: o(logn)
space complexity: o(1)
"""
