class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)== 0:
            return 0
        result = 0
        for i in nums:
            result  = result ^ i
        return result

if __name__ == "__main__":
    test = [[1,2,3,4,5,1,2,3,4]]
    a = Solution()
    for i in test:
        print a.singleNumber(i)
