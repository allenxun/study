class Solution(object):
    def productExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        result = [1]*len(nums)
        left = right = 1
        for i in range(len(nums)-1):
            left *= nums[i]
            result[i+1] *= left
            
        for i in range(len(nums)-1,0,-1):
            right *= nums[i]
            result[i-1] *= right
            
        return result

if __name__ == "__main__":
    test = [1,2,3,4,5,6]
    a = Solution()
    print a.productExceptSelf(test)
