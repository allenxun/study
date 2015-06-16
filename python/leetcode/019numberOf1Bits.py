class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        num = 0
        while n:
            num = num+1
            n = (n-1)&n
        return num
        

if __name__ == "__main__":
    test = [2,3,54,99]
    a = Solution()
    for i in test:
        print a.hammingWeight(i)
