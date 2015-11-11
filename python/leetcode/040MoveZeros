class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        j = 0
        for i in nums:
            if i !=0:
                nums[j]=i
                j = j+1
        for i in range(j,len(nums)):
            nums[i] = 0

if __name__ == "__main__":
    test = [[0,0,0],[1,2,5,0,2],[0,6,7]]
    a = Solution()
    for i in test:
        a.moveZeroes(i)
        print i 
