class Solution():
    def containDuplicate(self,nums):
        flag = False
        if len(nums)<=1:
            return False
        for i in range(0,len(nums)-1):
            for j in range(i+1,len(nums)):
                print nums[i],nums[j]
                if nums[i]==nums[j]:
                    flag = True
        return flag

a = Solution()
test = [[3,1,4],[2,3,4,5,3]]
for i in test:
    print a.containDuplicate(i)
