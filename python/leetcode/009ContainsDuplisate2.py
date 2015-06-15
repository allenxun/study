class Solution:
    def containsNerbyDuplicate(self,nums,k):
        numDict = dict()
        for i in range(len(nums)):
            numDict[nums[i]] = i
        for i in range(len(nums)):
            x = numDict.get(nums[i])
            if x-i!=0 and x-i <= k:
                return True
        return False

if __name__ == "__main__":
    a = Solution()
    test = [[1,2,3,4,5,6],[],[1],[1,1,2],[1,2,3,4,1]]
    for i in test:
        print a.containsNerbyDuplicate(i,3)
                


