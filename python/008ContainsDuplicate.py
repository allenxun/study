class Solution():
    def containDuplicate(self,nums):
        if len(nums)<=1:
            return False
        for i in range(0,len(nums)):
            for j in range(0,len(nums)):
                if nums[i]==nums[j]:
                    return True
                else:
                    return False

a = Solution()
test = [1,2,3,4,5,3]
print a.containDuplicate(test)
