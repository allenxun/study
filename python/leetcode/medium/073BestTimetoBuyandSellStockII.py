class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        result = 0
        for i in range(0,len(prices)-1):
            if prices[i+1]- prices[i]>0:
                result  += prices[i+1]- prices[i]
        return result

if __name__ == "__main__":
    test = [1,2,6,3,4,5]
    a = Solution()
    print a.maxProfit(test)
