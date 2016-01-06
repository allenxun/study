class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if target >nums[len(nums)-1]:
            return len(nums)
        for i in range(len(nums)):
            if target>nums[i]:
                continue
            else:
                return i

if __name__ == "__main__":
    test1 = [1,3,5,6]
    test2 = [5,2,7,0]
    a = Solution()
    for i in test2:
        print a.searchInsert(test1,i)
