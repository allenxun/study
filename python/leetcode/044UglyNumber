class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <=0:
            return False

        while num%2 == 0:
            num = num / 2
        while num%3 == 0:
            num = num / 3
        while num%5 == 0:
            num = num / 5

        if num == 1:
            return True
        else:
            return False

if __name__ == "__main__":
    test = [2,4,5,6,23,13]

    a = Solution()

    for i in test:
        print a.isUgly(i)
