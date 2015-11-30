class Solution(object):
    def canWinNim(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n%4==0:
            return False
        else:
            return True

if __name__ == "__mian__":
    a = Solution()
    t = a.canWinNim(12)
    print t
