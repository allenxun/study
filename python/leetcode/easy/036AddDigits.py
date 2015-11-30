class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        if num == 0:
            return 0
        else:
            return (num-1)%9+1
if __name__ =="__main__":
    a = Solution()
    test = [12,3423,120,10,2,0]
    for i in test:
        t = a.addDigits(i)
        print t
