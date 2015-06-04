class Solution():
    def containDuplicate(self,nums):
        nums.sort()
        if len(nums)<=1:
            return False
        for i in range(1,len(nums)):
            if nums[i-1]==nums[i]:
                return True
        return False
a = Solution()
test = [[3,1,4],[2,3,4,5,3]]
for i in test:
    print a.containDuplicate(i)
