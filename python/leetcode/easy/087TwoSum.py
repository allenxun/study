class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        numDict =  {}
        for i in range(len(nums)):
            numDict[nums[i]] = i
        for i in range(len(numDict)):
            temp = target - nums[i]
            if (temp) in numDict.keys():
                if i == numDict[temp]:
                    continue
                else:
                    return [i,numDict[temp]]
        
if __name__ == "__main__":
    a = Solution()
    testNum = [[1,2,3,4],[4,6,2,7],[2, 7, 11, 15],[3,2,1],[3,2,4]]
    testTarget = [5,9,13,3,6]
    for i in range(len(testNum)):
        print a.twoSum(testNum[i],testTarget[i])
