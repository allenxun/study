class Solution:
    # @param {integer[]} nums
    # @return {string[]}
    def summaryRanges(self, nums):
        result = []
        for n in nums:
            if not result or n > result[-1][-1] + 1:
                result += [],
            result[-1][1:] = n,
        return ['->'.join(map(str, r)) for r in result]
'''
['->'.join(map(str, r)) for r in [[1,2],[4,5]]]
["1->2","4->5"]

'''
if __name__ == "__main__":
    test = [[1,2,3,4,6,7,8,9],[1,2,3,4,5,67,68,69]]
    a = Solution()
    for i in test:
        print a.summaryRanges(i)
