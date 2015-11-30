class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        Ls = list(s)
        Lt = list(t)
        Ls.sort()
        Lt.sort()
        return Ls == Lt

if __name__ == "__main__":
    test1 = "bg"
    test2 = "gd"
    a = Solution()
    print a.isAnagram(test1,test2)
