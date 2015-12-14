class Solution(object):
    def removeDuplicates(self, nums):
        if nums==[]: return 0
        start=1;keyValue=nums[0];length=len(nums)
        for i in range(length):
            if nums[i]!=keyValue:
                keyValue=nums[i]
                nums[start]=nums[i]
                start+=1
        nums=nums[:start]
        return start
if __name__ == "__main__":
    test = [[],[1],[1,1,2],[1,2,2,4,4,5],[1,1,1]]
    a = Solution()
    for i in test:
        print a.removeDuplicates(i)
