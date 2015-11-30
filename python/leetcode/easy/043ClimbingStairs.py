class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 1:
            return 1
        if n == 2:
            return 2
        return self.climbStairs(n-1)+self.climbStairs(n-2)

    def climbStairs2(self,n):
        if n<4:
           return n
        a = 2
        b = 3
        c = 5
        for i in range(5,n+1):
            a = c
            c = c+b
            b = a
        return c

if __name__ == "__main__":
    test = [2,3,45,5]
    a = Solution()

    for i  in test:
        print a.climbStairs2(i)
