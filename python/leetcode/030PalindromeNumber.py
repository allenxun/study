class Solution:
    # @param {integer} x
    # @return {boolean}
    def isPalindrome(self, x):
        if x<0:
            return False
        if x==0:
            return True
        num = 1
        while x/num >= 10:
            num *=10
        while x:
            high = x/num
            low = x%10
            if high!=low:
                return False
            x -= high*num
            num /= 100
            x /=10
        return True

if __name__ == "__main__":
    a = Solution()
    test = [1221,12344321,121,12]
    for i in test:
        print a.isPalindrome(i)
