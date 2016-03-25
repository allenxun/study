import math
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        return n>0 and (3 ** round(math.log(n,3)) == n)

if __name__ == "__main__":
    a = Solution()
    test = [1,2,4,5,9,27,8]
    for i in test:
        print a.isPowerOfThree(i)
