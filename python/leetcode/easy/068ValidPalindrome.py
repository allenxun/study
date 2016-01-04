import string
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.lower()
        i,j = 0,len(s)-1
        while i<=j:
            if self.isvalid(s[i]):
                i +=1
                continue
            if self.isvalid(s[j]):
                j -=1
                continue
            if s[i] != s[j]:
                return False
            else:
                i += 1
                j -= 1
        return True
    def isvalid(self,s):
        if (s>='a' and s<='z') or (s>='0' and s<='9'):
            return False
        else:
            return True

if __name__ == "__main__":
    a = Solution()
    test = ["A   man, a plan,a canal: panama","race a car","aba","ab , b a,,","0P"]

    for i in test:
        print a.isPalindrome(i)
