class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def majorityElement(self, nums):
        time = 0
        result = 0
        for i in nums:
            if time == 0:
                result = i
                time = 1
            else:
                if result == i:
                    time +=1
                else:
                    time -=1
        return result

if __name__ == "__main__":
    test = [[1,2,3,2,2],[4,5,6,3,3,3,4,3]]
    a = Solution()
    for i in test:
        print a.majorityElement(i)
