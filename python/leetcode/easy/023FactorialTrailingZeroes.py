class Solution:
    # @param {integer} n
    # @return {integer}
    def trailingZeroes(self, n):
        result = 0
        while n:
            result += n/5;
            n /=5
        return result

if __name__ == "__main__":
    test = [5,15,10]
    a = Solution()
    for i in test:
        print a.trailingZeroes(i)
