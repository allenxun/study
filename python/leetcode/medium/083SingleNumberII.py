class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n1 = n2 = n3 = 0
        for i in nums:
            n3 = n2 & i
            n2 = n2 | (n1 & i)
            n1 = n1 | i
            n1 = n1 & ~n3
            n2 = n2 & ~n3
        return n1

if __name__ == "__main__":
    test = [1,1,1,2],[1,2,3,4,1,2,3,3,1,2],[1,2,3,2,4,3,2,1,3,1]
    a = Solution()
    for i in test:
        print a.singleNumber(i)
