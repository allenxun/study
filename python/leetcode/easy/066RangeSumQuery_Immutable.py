class NumArray(object):
    def __init__(self, nums):
        """
        initialize your data structure here.
        :type nums: List[int]
        """
        self.sums = [0] * (len(nums)+1)
        for i in range(len(nums)):
            self.sums[i+1] += self.sums[i] + nums[i]
    def sumRange(self, i, j):
        """
        sum of elements nums[i..j], inclusive.
        :type i: int
        :type j: int
        :rtype: int
        """
        return self.sums[j+1] - self.sums[i]

if __name__ == "__main__":
    test = [-2, 0, 3, -5, 2, -1]
    a = NumArray(test)
    print a.sumRange(0,2)
    print a.sumRange(2,5)
    print a.sumRange(0,5)
# Your NumArray object will be instantiated and called as such:
# numArray = NumArray(nums)
# numArray.sumRange(0, 1)
# numArray.sumRange(1, 2)
