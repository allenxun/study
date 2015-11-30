class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        j = len(nums)-1
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] == val:
                nums[i], nums[j] = nums[j], nums[i]
                j -= 1
        return j+1

if __name__ == "__main__":
    test = [[1,2,3,4,5,1,4],[4,5],[4],[4,4]]
    a = Solution()
    for i in test:
        print a.removeElement(i,4),i
