class Solution(object):
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return 0
        else:
            sum = max = 0
            min = nums[0]
        
            for i in nums:
                sum += i
                if max < i:
                    max =i
                if min > i:
                    min = i
            sums = (min+max)*(max+1)/2
            
            if min!=0:
                return 0

            if sums - sum == 0:
                return max+1
            
            return sums-sum

if __name__=="__main__":
    test = [[0,1,2,4],[0,1,2,3,4,5],[1,2],[0],[1,0]]
    a = Solution()
    for i in test:
        print a.missingNumber(i)
