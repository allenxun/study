class Solution(object):
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """
        nums = []
        nums.append(1)
        for i in range(1,n+1):
            nums.append(0)
            if i < 3:
                nums[i] = i
            else:
                for  j  in range(1,i+1):
                    nums[i] += nums[j-1]* nums[i-j]
        return nums[n]

if __name__ == "__main__":
    test  = [1,2,3,4,5]
    a = Solution()

    for i in test:
        print a.numTrees(i)
