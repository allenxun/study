class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = nums[0]
        for i in range(1,len(nums)):
            result = result^nums[i]
        low = result & (-result)
        a = 0
        b = 0
        for j in nums:
            if j & low:
                a ^= j
            else: 
                b ^= j
        return [a,b]

if __name__ == "__main__":
    test = [1,2,3,4,3,4]
    a = Solution()
    print a.singleNumber(test)
