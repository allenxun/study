class Solution:
    # @param {integer} x
    # @return {integer}
    def reverse(self, x):
        res = 0
        flag = 1 if x>0 else -1
        min = -2147483648
        max = 2147483647
        x = flag*x 
        while x:
            res = res*10 + x%10
            x = x/10
        sum = flag*res
        if min<=sum and sum <= max: 
            return sum
        else:
            return 0
        
if __name__ == "__main__":
    test = [10,1265123,1000000003,-2147483412,1534236469,-1534236469]
    a = Solution()
    for i in test:
        print a.reverse(i)
