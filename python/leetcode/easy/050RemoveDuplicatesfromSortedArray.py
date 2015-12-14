class Solution(object):
    def removeDuplicates(self,nums):
        if len(nums) == 0:
            return 0
        if len(nums) == 1:
            return 1
        key = nums[1]
        for i in nums:
            if i == key:
                nums.remove(i)
            key = key+1
        print nums
        return len(nums)
if __name__ == "__main__":
    test = [[],[1],[1,1,2],[1,2,2,4,4,5]]
    a = Solution()
    for i in test:
        print a.removeDuplicates(i)
