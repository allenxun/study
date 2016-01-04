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
        low = 1
        high = n
        version =0
        while low < high:
            version = low+(high - low )/2
            if self.isBadVersion(version):
                high = version
            else:
                low = version+1
        return low
